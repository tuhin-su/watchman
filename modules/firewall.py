import os
from modules.logger import log
from modules.espeak import text_to_speech

def check_rule_exists(ip_address):
    command = f"sudo iptables -C INPUT -s {ip_address} -j REJECT"
    try:
        exit_code = os.system(command)
        return exit_code == 0
    except Exception as e:
        return False

def block_ip(ip_address, reason):
    if not check_rule_exists(ip_address):
        try:
            command = f"sudo iptables -A INPUT -s {ip_address} -j REJECT"
            os.system(command)
            log(f"IP {ip_address} address added to block list for {reason}")
        except Exception as e:
            log(f"Failed to block IP address {ip_address}: {e}")

def backup_iptables(backup_file_path):
    try:
        command = f"sudo iptables-save > {backup_file_path}"
        os.system(command)
        log("Iptables backup completed successfully")
    except Exception as e:
        log(f"Failed to backup iptables: {e}")

def restore_iptables(backup_file_path):
    try:
        command = f"sudo iptables-restore < {backup_file_path}"
        os.system(command)
        log("Iptables restored from backup successfully")
    except Exception as e:
        log(f"Failed to restore iptables: {e}")
