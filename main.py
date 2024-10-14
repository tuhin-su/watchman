from scapy.all import sniff, IP, TCP
from collections import defaultdict
import time
import signal
import sys
from modules.firewall import block_ip, backup_iptables, restore_iptables
from modules.espeak import text_to_speech
from modules.notify import notify
from modules.config_loader import load_config
from modules.network import is_ip_in_network
import os


attack_ips = []
config = load_config('watchman.conf')
print(config)
PORT_SCAN_THRESHOLD=config['PORT_SCAN_THRESHOLD']
DOS_THRESHOLD=config['DOS_THRESHOLD']

port_access_count = defaultdict(int)
packet_count = defaultdict(int)
last_check_time = time.time()

def not_in_bypass(ip:str):
    for i in config['BYPASS']:
        if is_ip_in_network(ip, i):
            if config['BYPASS_NOTIFY']:
                notify(f'ATACK FROM {ip}')
            return False
    return True

def detect_port_scan(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        src_ip = packet[IP].src
        dst_port = packet[TCP].dport
        port_access_count[(src_ip, dst_port)] += 1

        if not_in_bypass(src_ip) and(src_ip not in attack_ips) and (len({port for (ip, port) in port_access_count if ip == src_ip}) > PORT_SCAN_THRESHOLD):
            
            if config['voice']:
                text_to_speech(f"Attack Detected")

            if config['notify']:
                notify(f"scaning performed by {src_ip}")
                
            if config['blocker']:
                block_ip(src_ip, reason=str(f":PORT"))

            attack_ips.append(str(src_ip))
            for (ip, port) in list(port_access_count):
                if ip == src_ip:
                    del port_access_count[(ip, port)]

def detect_dos_attack(packet):
    global last_check_time

    if packet.haslayer(IP):
        src_ip = packet[IP].src
        packet_count[src_ip] += 1

        current_time = time.time()
        if not_in_bypass(src_ip) and (src_ip not in attack_ips) and (current_time - last_check_time > 1):  # Check every 1 second
            for ip, count in list(packet_count.items()):
                if count > DOS_THRESHOLD:
                    attack_ips.append(str(src_ip))

                    if config['blocker']:
                        block_ip(ip, reason=str(f":DoS"))

                    if config['voice']:
                        text_to_speech(f"DoS Attack Detected")

                    if config['notify']:
                        notify(f"DOS performed by {src_ip}")

                packet_count[ip] = 0
            last_check_time = current_time

def packet_callback(packet):
    detect_port_scan(packet)
    detect_dos_attack(packet)

def stopping(signum, frame):
    backup_iptables("firewall/backup.text")
    sys.exit(0)

if __name__ == "__main__":
    if not os.path.exists("firewall"):
        os.makedirs("firewall")

    if os.path.exists("firewall/backup.text"):
       restore_iptables("firewall/backup.text")

    signal.signal(signal.SIGINT, stopping)
    signal.signal(signal.SIGTERM, stopping)
    signal.signal(signal.SIGQUIT, stopping)

    print("Starting packet sniffing...")
    sniff(filter="ip", prn=packet_callback, store=0)
