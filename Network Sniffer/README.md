# Network Sniffer

A simple, educational packet sniffer built with **Python 3** and **Scapy**.
Designed for learning packet inspection and traffic analysis (IP/TCP/UDP/DNS).

## Features
- Real-time packet capture and tidy console output
- Identifies TCP / UDP / DNS packets and shows source/destination IP and ports
- Supports BPF filtering (e.g., `tcp`, `port 53`)
- Optional PCAP export with `-o filename.pcap`
- Graceful Ctrl+C handling and safe exit

## Requirements
- Python 3.x
- scapy
Install dependency:
  ```bash
  pip install scapy --break-system-packages
  ```
- rich
Install dependency:
  ```bash
  pip install rich --break-system-packages
  ```

## How to Run
- Run until Ctrl+C on default interface
  ```bash
  python Network_Sniffer_Mr.py
  ```
- Capture 200 TCP packets on interface eth0 and save to capture.pcap
  ```bash
  sudo python3 Network_Sniffer_Mr.py -i eth0 -c 200 -f "tcp" -o capture.pcap
  ```


