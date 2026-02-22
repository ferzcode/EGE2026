from ipaddress import *

net = ip_network('112.154.132.0/255.255.252.0', False)
c = 0

# .hosts() - ТОЛЬКО УЗЛЫ (УСТРОЙСТВА)

for ip in net.hosts():
    binary = bin(int(ip))[2:].zfill(32)

    if binary[:16].count('1') <= binary[16:].count('0') and binary[16:].count('0') % 2 != 0:
        c += 1


print(c)