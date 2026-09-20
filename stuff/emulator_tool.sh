#!/bin/bash
set -e

# ==========================================
# Defaults
# ==========================================

PROXY_HOST="localhost"
PROXY_PORT=3333
BURP_PORT=8082
DEVICE=""

# ==========================================
# Usage
# ==========================================

usage() {
    echo "Usage:"
    echo ""
    echo "  Proxy:"
    echo "    $0 --setup-proxy [--proxy-port <port>] [--burp-port <port>] [--device <adb_serial>]"
    echo "    $0 --cleanup-proxy [--proxy-port <port>] [--device <adb_serial>]"
    echo ""
    echo "  Flutter Transparent Proxy:"
    echo "    $0 --setup-flutter-proxy [--burp-port <port>] [--device <adb_serial>]"
    echo "    $0 --cleanup-flutter-proxy [--device <adb_serial>]"
    echo ""
    echo "  Certificate:"
    echo "    $0 --setup-cert --cert <certificate.der> [--device <adb_serial>]"
    echo "    $0 --cleanup-cert --cert <certificate.der> [--device <adb_serial>]"
    echo ""
    echo "Optional:"
    echo "    --device <adb_device_serial>"
    echo ""

    exit 1
}

# ==========================================
# Parse Arguments
# ==========================================

MODE=""
CERT_DER=""

while [[ $# -gt 0 ]]; do
    case $1 in

        --setup-proxy)
            MODE="setup-proxy"
            shift
            ;;

        --cleanup-proxy)
            MODE="cleanup-proxy"
            shift
            ;;

        --setup-flutter-proxy)
            MODE="setup-flutter-proxy"
            shift
            ;;

        --cleanup-flutter-proxy)
            MODE="cleanup-flutter-proxy"
            shift
            ;;

        --setup-cert)
            MODE="setup-cert"
            shift
            ;;

        --cleanup-cert)
            MODE="cleanup-cert"
            shift
            ;;

        --cert)
            CERT_DER="$2"
            shift 2
            ;;

        --proxy-port)
            PROXY_PORT="$2"
            shift 2
            ;;

        --burp-port)
            BURP_PORT="$2"
            shift 2
            ;;

        --device)
            DEVICE="$2"
            shift 2
            ;;

        *)
            usage
            ;;
    esac
done

if [[ -z "$MODE" ]]; then
    usage
fi

# ==========================================
# Helpers
# ==========================================

require_adb() {
    command -v adb >/dev/null 2>&1 || {
        echo "❌ adb not found"
        exit 1
    }
}

adb_cmd() {
    if [[ -n "$DEVICE" ]]; then
        adb -s "$DEVICE" "$@"
    else
        adb "$@"
    fi
}

adb_root() {
    adb_cmd root >/dev/null 2>&1 || true
}

# ==========================================
# Standard Android Proxy
# ==========================================

setup_proxy() {
    echo "[Proxy] Setting Android proxy..."

    adb_cmd shell settings put global http_proxy \
        $PROXY_HOST:$PROXY_PORT

    adb_cmd reverse tcp:$PROXY_PORT tcp:$BURP_PORT

    echo "✅ Android proxy configured"
}

cleanup_proxy() {
    echo "[Proxy] Removing Android proxy..."

    adb_cmd shell settings delete global http_proxy || true
    adb_cmd shell settings delete global global_http_proxy_host || true
    adb_cmd shell settings delete global global_http_proxy_port || true

    adb_cmd reverse --remove tcp:$PROXY_PORT || true

    echo "✅ Android proxy removed"
}

# ==========================================
# Flutter Transparent Proxy (iptables)
# ==========================================

setup_flutter_proxy() {
    echo "[Flutter Proxy] Setting transparent proxy..."

    adb_root

    adb_cmd shell "
        iptables -t nat -N BURP 2>/dev/null || true
        iptables -t nat -F BURP

        iptables -t nat -C OUTPUT -p tcp -j BURP 2>/dev/null || \
            iptables -t nat -A OUTPUT -p tcp -j BURP

        iptables -t nat -A BURP -p tcp --dport 80 \
            -j REDIRECT --to-ports $BURP_PORT

        iptables -t nat -A BURP -p tcp --dport 443 \
            -j REDIRECT --to-ports $BURP_PORT
    "

    echo "✅ Flutter transparent proxy enabled"
    echo ""
    echo "⚠️  Burp must have:"
    echo "   Proxy Listener -> Support invisible proxying"
}

cleanup_flutter_proxy() {
    echo "[Flutter Proxy] Removing transparent proxy..."

    adb_root

    adb_cmd shell "
        iptables -t nat -D OUTPUT -p tcp -j BURP 2>/dev/null || true
        iptables -t nat -F BURP 2>/dev/null || true
        iptables -t nat -X BURP 2>/dev/null || true
    "

    echo "✅ Flutter transparent proxy removed"
}

# ==========================================
# Certificate Install
# ==========================================

setup_cert() {

    if [[ -z "$CERT_DER" ]]; then
        echo "❌ Certificate file is required"
        exit 1
    fi

    if [[ ! -f "$CERT_DER" ]]; then
        echo "❌ Certificate file not found: $CERT_DER"
        exit 1
    fi

    echo "[Cert] Converting certificate..."

    TMP_PEM=$(mktemp)

    openssl x509 \
        -inform DER \
        -in "$CERT_DER" \
        -out "$TMP_PEM"

    HASH=$(openssl x509 \
        -inform PEM \
        -subject_hash_old \
        -in "$TMP_PEM" | head -1)

    CERT_HASHED="$HASH.0"

    mv "$TMP_PEM" "$CERT_HASHED"

    echo "[Cert] Installing certificate..."

    adb_root

    adb_cmd shell mount -o rw,remount / || true
    adb_cmd remount || true

    adb_cmd push "$CERT_HASHED" \
        /system/etc/security/cacerts/

    adb_cmd shell chmod 644 \
        /system/etc/security/cacerts/"$CERT_HASHED"

    adb_cmd reboot

    echo "✅ Certificate installed"
}

cleanup_cert() {

    if [[ -z "$CERT_DER" ]]; then
        echo "❌ Certificate file is required"
        exit 1
    fi

    if [[ ! -f "$CERT_DER" ]]; then
        echo "❌ Certificate file not found: $CERT_DER"
        exit 1
    fi

    echo "[Cert] Removing certificate..."

    TMP_PEM=$(mktemp)

    openssl x509 \
        -inform DER \
        -in "$CERT_DER" \
        -out "$TMP_PEM"

    HASH=$(openssl x509 \
        -inform PEM \
        -subject_hash_old \
        -in "$TMP_PEM" | head -1)

    CERT_HASHED="$HASH.0"

    adb_root

    adb_cmd shell mount -o rw,remount / || true
    adb_cmd remount || true

    adb_cmd shell rm -f \
        /system/etc/security/cacerts/"$CERT_HASHED"

    adb_cmd reboot

    rm -f "$TMP_PEM"

    echo "✅ Certificate removed"
}

# ==========================================
# Main
# ==========================================

require_adb

case $MODE in

    setup-proxy)
        setup_proxy
        ;;

    cleanup-proxy)
        cleanup_proxy
        ;;

    setup-flutter-proxy)
        setup_flutter_proxy
        ;;

    cleanup-flutter-proxy)
        cleanup_flutter_proxy
        ;;

    setup-cert)
        setup_cert
        ;;

    cleanup-cert)
        cleanup_cert
        ;;

    *)
        usage
        ;;
esac
