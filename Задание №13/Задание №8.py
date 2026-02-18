# Сеть, в которой содержится узел с IP-адресом 192.214.A.184, задана маской сети 255.255.255.224,
# где A - некоторое допустимое для записи IP-адреса число.
#
# Определите минимальное значение A, для которого для всех IP-адресов этой сети
# в двоичной записи IP-адреса суммарное количество единиц будет больше 15.
#
# В ответе укажите только число.

from ipaddress import *

# 1 CПОСОБ

for A in range(0, 256):
    net = ip_network(f'192.214.{A}.184/255.255.255.224', False)

    c = 0
    for ip in net:
        binary = bin(int(ip))[2:].zfill(32)
        if binary.count('1') > 15:
            c += 1

    if c == len(set(net)):
        print(A)
        break

# 2 CПОСОБ

def proverka(ip):
    binary = bin(int(ip))[2:].zfill(32)
    return binary.count('1') > 15


for A in range(0, 256):
    net = ip_network(f'192.214.{A}.184/255.255.255.224', False)

    if all(proverka(ip) == 1 for ip in net):
        print(A)
        break