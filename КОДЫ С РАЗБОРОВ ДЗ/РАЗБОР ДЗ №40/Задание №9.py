from ipaddress import *

net = ip_network('172.16.80.0/255.255.248.0' , False)
c = 0

for ip in net:
    binary = bin(int(ip))[2:].zfill(32)

    if binary.count('1') % 2 != 0:
        c += 1
print(c)