from ipaddress import *

def proverka(ip):
    binary = bin(int(ip))[2:].zfill(32)
    return binary[:16].count('0') <= binary[16:].count('0')


for A in range(0, 256):
    net = ip_network(f'217.109.{A}.94/255.255.254.0', False)

    if all(proverka(ip) == 1 for ip in net):
        print(A)


