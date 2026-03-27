from ipaddress import *

net = ip_network('214.187.224.0/255.255.224.0', False)
c = 0

for ip in net:
    binary = bin(int(ip))[2:].zfill(32)

    if binary.count('1') % 6 != 0 and binary[-4:] == '1000':
        c += 1
print(c)