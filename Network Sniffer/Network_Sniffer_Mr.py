#!/usr/bin/env python3

"""
Network Sniffer Mr
Professional & Colored Packet Sniffer (Educational Use)
Author: Mohamed Ramadan
"""

from scapy.all import sniff
from datetime import datetime
from rich import print
from rich.console import Console
from rich.table import Table

console = Console()

def print_packet(packet):
    ts = datetime.now().strftime("%H:%M:%S")

    if not packet.haslayer('IP'):
        console.print(f"[bold red][NON-IP][/] Packet captured at {ts}")
        return

    src = packet['IP'].src
    dst = packet['IP'].dst

    protocol = "OTHER"
    sport = ""
    dport = ""

    if packet.haslayer('TCP'):
        protocol = "[cyan]TCP[/]"
        sport = packet['TCP'].sport
        dport = packet['TCP'].dport
    elif packet.haslayer('UDP'):
        protocol = "[yellow]UDP[/]"
        sport = packet['UDP'].sport
        dport = packet['UDP'].dport
    elif packet.haslayer('DNS'):
        protocol = "[magenta]DNS[/]"

    
    table = Table(show_header=True, header_style="bold red", border_style="bright_black")

    table.add_column("Time", style="white")
    table.add_column("Protocol", style="bold")
    table.add_column("Source", style="green")
    table.add_column("Destination", style="blue")

    src_str = f"{src}:{sport}" if sport else src
    dst_str = f"{dst}:{dport}" if dport else dst

    table.add_row(ts, protocol, src_str, dst_str)

    console.print(table)
    console.print("-" * 60)


def main():
    console.print("[bold red]=== Packet Sniffer Started ===[/]")
    console.print("[yellow]Press CTRL + C to stop\n[/]")

    sniff(prn=print_packet, store=False)


if __name__ == "__main__":
    main()
