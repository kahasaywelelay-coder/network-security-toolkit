import socket
import struct

def get_ip_class(ip_address):
    first_octet = int(ip_address.split('.')[0])
    if 1 <= first_octet <= 126:
        return 'Class A', '255.0.0.0'
    elif 128 <= first_octet <= 191:
        return 'Class B', '255.255.0.0'
    elif 192 <= first_octet <= 223:
        return 'Class C', '255.255.255.0'
    elif 224 <= first_octet <= 239:
        return 'Class D (Multicast)', 'N/A'
    else:
        return 'Class E (Experimental)', 'N/A'

def get_default_gateway():
    try:
        with open("/proc/net/route", "r") as fh:
            for line in fh:
                fields = line.strip().split()
                if fields[1] != '00000000' or not int(fields[3], 16) & 2:
                    continue
                gateway_hex = fields[2]
                gateway_ip = socket.inet_ntoa(struct.pack("<L", int(gateway_hex, 16)))
                return gateway_ip
    except Exception:
        return "Unable to determine gateway (non-Linux OS)"

if __name__ == "__main__":
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    ip_class, subnet = get_ip_class(local_ip)
    gateway = get_default_gateway()

    print(f"[*] Local IP Address : {local_ip}")
    print(f"[*] IP Class         : {ip_class}")
    print(f"[*] Default Subnet   : {subnet}")
    print(f"[*] Default Gateway  : {gateway}")