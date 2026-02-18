# Узел с IP-адресом 143.131.211.37 принадлежит сети, в которой 15 IP-адресов,
# двоичная запись которых содержит ровно 10 единиц.
#
# Сколько единиц содержится в двоичной записи маски этой сети?

from ipaddress import *

for mask in range(32, -1, -1):
    net = ip_network(f'143.131.211.37/{mask}', False)
    c = 0

    for ip in net:
        binary = bin(int(ip))[2:].zfill(32)
        if binary.count('1') == 10:
            c += 1

    if c == 15:
        print(mask)