from ipaddress import *

c = 0
net = ip_network('172.16.96.0/255.255.224.0', False)
for ip in net:
    b = bin(int(ip))[2:].zfill(32)

    if b.count('1') % 2 == 0:
        c += 1

print(c)