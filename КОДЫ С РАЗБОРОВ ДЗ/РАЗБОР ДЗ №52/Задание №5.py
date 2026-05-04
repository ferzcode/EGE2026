from ipaddress import *

c = 0
net = ip_network('172.95.116.174/255.255.192.0', False)
for ip in net:
    b = bin(int(ip))[2:].zfill(32)

    if b.count('1') % 5 == 0:
        print(ip)
        break
