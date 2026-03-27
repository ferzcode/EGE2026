from ipaddress import *

net = ip_network('123.222.111.192/255.255.255.248', False)
c = 0

for ip in net:
    binary = bin(int(ip))[2:].zfill(32)

    if binary[24:].count('0') % 3 != 0:
        c += 1
print(c)