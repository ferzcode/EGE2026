from ipaddress import *

mask = [255, 254, 252, 248, 240, 224, 192, 128, 0]
for X in mask:
    net = ip_network(f'172.16.168.0/255.255.255.{X}', False)

    c = 0
    for ip in net:
        b = bin(int(ip))[2:].zfill(32)

        if b.count('0') % 7 == 0:
            c += 1

    if c == 35:
        print(X)