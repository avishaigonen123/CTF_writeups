---
layout: default
title: another_file
---

# 🛡️ WiFi Hacking Recon & Targeting Summary (Without Evil Twin)

## 🔍 1. Discovering Devices with `arp-scan`

We used `arp-scan` to discover devices on the local network. This tool sends ARP requests to the subnet and lists active devices with their IP and MAC addresses.

### Command:
```bash
sudo arp-scan --interface=eth0 --localnet
```

- `--interface=eth0`: Set the network interface (e.g., use `wlan0` for WiFi).
- `--localnet`: Automatically scans the subnet you're on.

> ⚠️ If your interface has no IP address (e.g., `wlan0` in monitor mode), `arp-scan` might not work unless you specify the spoofed address using `--arpspa`.

---

## 📡 2. Scanning a Target Device with Nmap

Once we identify a target IP (from `arp-scan`, DHCP leases, or router interface), we use `nmap` to fingerprint the OS and check for open ports.

### Command:
```bash
sudo nmap -O <target-ip>
```

- `-O`: Attempts to detect the operating system.
- Requires root to send raw TCP packets.
- Useful for determining if a device is a Windows machine, Linux, Android, etc.

---

## 🎯 3. Getting MAC Address from IP and Vice Versa

### A. From Your Own PC:
Use the `arp` tool after pinging the device.

```bash
ping <target-ip>
arp -a
```

### B. From Within Scripts / Tools:
- `arp-scan` returns both IPs and MACs.
- Routers also often expose DHCP lease tables.

---

## 🔬 4. Observing Devices with `airodump-ng`

To passively monitor WiFi traffic, we used:

```bash
sudo airodump-ng wlan0mon
```

Once BSSIDs and STATION MACs are visible, you can identify connected clients and signal strength (PWR).

> If your phone doesn’t appear, ensure:
> - It’s actively transmitting packets.
> - It’s not using WiFi isolation or client isolation features.
> - You’re monitoring the correct channel.

---

## 🚫 5. Attempting Deauthentication (for Educational Use)

We attempted to deauthenticate a specific client from a known AP.

### Command:
```bash
sudo aireplay-ng --deauth 10 -a <AP_MAC> -c <CLIENT_MAC> wlan0mon
```

- `-a`: AP MAC address.
- `-c`: Client MAC address.
- `10`: Number of deauth packets to send.

> ✅ This worked when your phone was connected to a hotspot, but not reliably on some modern access points (due to protection mechanisms like 802.11w, deauth protection, etc.).

---

## ⚙️ 6. MAC Address Tracking & Identification Techniques

When facing many clients on the same WiFi:
- Use `airodump-ng` to see which STATIONs are talking most to the AP.
- Look at:
  - `#Data` frames exchanged.
  - PWR to estimate distance.
  - Probes to guess device names/OS (e.g., Windows, iPhone).

You can then:
- Track their IP via `arp-scan`.
- OS fingerprint via `nmap`.
- Optionally spoof or target only that MAC.

---

## ✅ Summary of Tools Used

| Tool        | Purpose                                   |
|-------------|-------------------------------------------|
| arp-scan    | Discover IP/MAC on local network          |
| airodump-ng | Sniff wireless traffic and client list    |
| aireplay-ng | Send deauth frames to clients             |
| nmap        | Port and OS scanning                      |
| arp         | View IP ↔ MAC mapping after ping          |
| ettercap    | (Planned) for MITM sniffing and spoofing  |

---

> ⚠️ **Legal Note:** All actions discussed here should only be performed in lab environments or on networks you own/have permission to test. Unauthorized network interference is illegal.
