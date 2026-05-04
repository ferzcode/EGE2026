from ipaddress import *

# for mask in range(32, -1, -1):
#     net1 = ip_network(f'95.24.2.9/{mask}', False)
#     net2 = ip_network(f'95.24.3.10/{mask}', False)
#
#     if net1 != net2:
#         print(mask)

c1 = 0
net1 = ip_network('95.24.2.9/24', False)
for ip in net1.hosts():
    b = bin(int(ip))[2:].zfill(32)

    if b[-1] == '0':
        c1 += 1

c2 = 0
net2 = ip_network('95.24.3.10/24', False)
for ip in net2.hosts():
    b = bin(int(ip))[2:].zfill(32)

    if b[-1] == '0':
        c2 += 1

print(c1, c2)