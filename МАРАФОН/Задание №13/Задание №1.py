from ipaddress import *

# net = ip_network('146.180.173.153/255.192.0.0', False)
# print(net[-2])

# net = ip_network('172.16.160.0/255.255.240.0', False)
# c = 0
# for ip in net:
#     b = bin(int(ip))[2:].zfill(32)
#
#     if b.count('1') % 2 == 0:
#         c += 1
# print(c)

# ВАЖНЫЕ КОМАНДЫ ДЛЯ ИЗЪЯТИЯ ИЗ СЕТИ
# net = ip_network('IP/Маска', False)
# ШИРОК - net.broadcast_address()
# СЕТИ - net.network_address()
# УЗЛЫ - net.hosts()
# МАСКА - net.netmask()

# def p(ip):
#     b = bin(int(ip))[2:].zfill(32)
#     return b[:16].count('0') <= b[16:].count('0')
#
# for A in range(0, 256):
#     net = ip_network(f'217.109.{A}.94/255.255.254.0', False)
#
#     if all(p(ip) == 1 for ip in net):
#         print(A)

# def p(ip):
#     b = bin(int(ip))[2:].zfill(32)
#     return b[:16].count('1') >= b[16:].count('1')
#
# param = [255, 254, 252, 248, 240, 224, 192, 128, 0]
# for A in param:
#     net = ip_network(f'127.63.67.1/255.255.{A}.0', False)
#
#     if all(p(ip) == 1 for ip in net):
#         print(A)

from ipaddress import *

for mask in range(0, 33):
    net = ip_network(f'145.192.94.230/{mask}', False)

    if str(net[0]) == '145.192.80.0':
        print(net.netmask)

























