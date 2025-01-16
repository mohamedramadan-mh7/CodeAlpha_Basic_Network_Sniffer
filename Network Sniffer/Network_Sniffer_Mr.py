from scapy.all import sniff

def process_packet(packet):
    if packet.haslayer('IP'):
        print(f"[+] Packet Captured:")
        print(f"    Source IP: {packet['IP'].src}")
        print(f"    Destination IP: {packet['IP'].dst}")
        if packet.haslayer('TCP'):
            print("    Protocol: TCP")
        elif packet.haslayer('UDP'):
            print("    Protocol: UDP")
        elif packet.haslayer('DNS'):
            print("    Protocol: DNS")
        print("-" * 30)

print("Capturing network traffic...")
sniff(prn=process_packet, count=10)
