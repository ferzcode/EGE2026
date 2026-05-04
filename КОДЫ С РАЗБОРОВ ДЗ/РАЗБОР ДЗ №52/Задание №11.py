from ipaddress import *

def proverka(ip):
    b = bin(int(ip))[2:].zfill(32)
    levie = b[:16]
    pravei = b[16:]

    return levie.count('0') <= pravei.count('0')

for A in range(0, 256):
    net = ip_network(f'217.109.{A}.94/255.255.254.0', False)

    if all(proverka(ip) == 1 for ip in net):
        print(A)
