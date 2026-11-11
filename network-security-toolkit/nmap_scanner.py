import nmap

scanner = nmap.PortScanner()
target = input("Enter target IP: ")
ports = '21,22,80,443,8080'

print(f"Nmap Version: {scanner.nmap_version()}")
scanner.scan(target, ports, arguments='-sV')

for host in scanner.all_hosts():
    print(f"\nHost: {host} ({scanner[host].hostname()})")
    print(f"State: {scanner[host].state()}")
    for proto in scanner[host].all_protocols():
        print(f"Protocol: {proto}")
        lport = scanner[host][proto].keys()
        for port in lport:
            state = scanner[host][proto][port]['state']
            service = scanner[host][proto][port]['name']
            print(f"  Port: {port}\tState: {state}\tService: {service}")