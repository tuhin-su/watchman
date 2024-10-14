import ipaddress

def is_ip_in_network(ip_str, cidr_str):
    network = ipaddress.ip_network(cidr_str, strict=False)
    ip = ipaddress.ip_address(ip_str)
    return ip in network