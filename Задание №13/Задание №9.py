# Сеть, в которой содержится узел с IP-адресом 116.242.A.26, задана маской сети 255.255.255.224,
#
# где A - некоторое допустимое для записи IP-адреса число.
# Определите максимальное значение A, для которого для всех IP-адресов этой сети
# в двоичной записи IP-адреса суммарное количество единиц в левых двух байтах не меньше суммарного количества единиц в правых двух байтах.

# В ответе укажите только число.

from ipaddress import *

# 1 СПОСОБ

for A in range(0, 256):
    net = ip_network(f'116.242.{A}.26/255.255.255.224', False)

    c = 0
    for ip in net:
        binary = bin(int(ip))[2:].zfill(32)

        if binary[:16].count('1') >= binary[16:].count('1'):
            c += 1

    if c == len(set(net)):
        print(A)

# 2 СПОСОБ

def proverka(ip):
    binary = bin(int(ip))[2:].zfill(32)
    return binary[:16].count('1') >= binary[16:].count('1')

for A in range(0, 256):
    net = ip_network(f'116.242.{A}.26/255.255.255.224', False)

    if all(proverka(ip) == 1 for ip in net):
        print(A)