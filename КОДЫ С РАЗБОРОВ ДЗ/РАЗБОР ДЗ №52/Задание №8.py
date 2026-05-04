from ipaddress import *

def proverka(ip):
    b = bin(int(ip))[2:].zfill(32)
    return b.count('1') > 15

for A in range(0, 256):
    net = ip_network(f'192.214.{A}.184/255.255.255.224', False)

    if all(proverka(ip) == 1 for ip in net):
        print(A)
        break