#!/bin/bash
set -e

# Default ports
PROXY_HOST="localhost"
PROXY_PORT=3333
BURP_PORT=8082

usage() {
    echo "Usage:"
    echo "  $0 --setup-proxy [--proxy-port <port>] [--burp-port <port>]"
    echo "  $0 --cleanup-proxy [--proxy-port <port>]"
    echo "  $0 --setup-cert --cert <certificate.der>"
    echo "  $0 --cleanup-cert --cert <certificate.der>"
    exit 1
}

# Parse arguments
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
        *)
            usage
            ;;
    esac
done

if [[ -z "$MODE" ]]; then
    usage
fi

# Functions
setup_proxy() {
    echo "[Proxy] Setting proxy..."
    adb shell settings put global http_proxy $PROXY_HOST:$PROXY_PORT
    adb reverse tcp:$PROXY_PORT tcp:$BURP_PORT
    echo "✅ Proxy setup complete"
}

cleanup_proxy() {
    echo "[Proxy] Removing proxy..."
    adb shell settings delete global http_proxy
    adb shell settings delete global global_http_proxy_host
    adb shell settings delete global global_http_proxy_port
    adb reverse --remove tcp:$PROXY_PORT || true
    echo "✅ Proxy removed"
}

setup_cert() {
    if [ -z "$CERT_DER" ]; then
        echo "❌ Certificate file is required"
        exit 1
    fi
    if [ ! -f "$CERT_DER" ]; then
        echo "❌ Certificate file not found: $CERT_DER"
        exit 1
    fi

    echo "[Cert] Converting certificate..."
    openssl x509 -inform DER -in "$CERT_DER" -out burp.pem
    HASH=$(openssl x509 -inform PEM -subject_hash_old -in burp.pem | head -1)
    CERT_HASHED="$HASH.0"
    mv burp.pem "$CERT_HASHED"

    echo "[Cert] Installing certificate..."
    adb root
    adb shell mount -o rw,remount /
    adb push "$CERT_HASHED" /system/etc/security/cacerts/
    adb shell chmod 644 /system/etc/security/cacerts/"$CERT_HASHED"
    adb reboot
    echo "✅ Certificate installed"
}

cleanup_cert() {
    if [ -z "$CERT_DER" ]; then
        echo "❌ Certificate file is required"
        exit 1
    fi
    if [ ! -f "$CERT_DER" ]; then
        echo "❌ Certificate file not found: $CERT_DER"
        exit 1
    fi

    echo "[Cert] Removing certificate..."
    openssl x509 -inform DER -in "$CERT_DER" -out burp.pem
    HASH=$(openssl x509 -inform PEM -subject_hash_old -in burp.pem | head -1)
    CERT_HASHED="$HASH.0"
    adb root
    adb shell mount -o rw,remount /
    adb shell rm -f /system/etc/security/cacerts/"$CERT_HASHED"
    adb reboot
    echo "✅ Certificate removed"
}

# Execute
case $MODE in
    setup-proxy) setup_proxy ;;
    cleanup-proxy) cleanup_proxy ;;
    setup-cert) setup_cert ;;
    cleanup-cert) cleanup_cert ;;
    *) usage ;;
esac
