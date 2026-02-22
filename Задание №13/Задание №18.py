# Сеть задана IP-адресом 192.168.31.80 и маской сети 255.255.255.240. Определите максимальную сумму единиц в двоичной записи IP-адреса в этой сети.
#
# В ответе укажите только число.

from ipaddress import *

net = ip_network('192.168.31.80/255.255.255.240', False)
maxi = 0

for ip in net:
    binary = bin(int(ip))[2:].zfill(32)

    maxi = max(maxi, binary.count('1'))
print(maxi)

# 2 СПОСОБ

print(bin(int(net.broadcast_address))[2:].zfill(32).count('1'))