from ipaddress import *

def proverka(ip):
    binary = bin(int(ip))[2:].zfill(32)
    return binary[:16].count('1') >= binary[16:].count('1')


for A in range(0, 256):
    net = ip_network(f'116.242.{A}.26/255.255.255.224', False)

    if all(proverka(ip) == 1 for ip in net):
        print(A)


