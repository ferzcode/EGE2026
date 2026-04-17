from ipaddress import *

# Задача №1

# net = ip_network('146.180.173.153/255.192.0.0', False)
# print(net[-2]) # Наибольший адрес
# print(net[1]) # Наименьший адрес

# Задача №2

# c = 0
# net = ip_network('172.16.160.0/255.255.240.0', False)
# for ip in net:
#     b = bin(int(ip))[2:].zfill(32)
#     if b.count('1') % 2 == 0:
#         c += 1
# print(c)

# Задача №3

# net = ip_network('202.71.92.91/255.255.192.0', False)
# for ip in net.hosts():
#     b = str(ip).split('.')
#
#     nechet = [x for x in b if int(x) % 2 != 0]
#     if len(nechet) == 2:
#         print(ip)

# Задача №4

# net = ip_network('192.168.12.207/255.192.0.0', False)
# for ip in net:
#     b = bin(int(ip))[2:].zfill(32)
#
#     if b.count('0') == b.count('1'):
#         print(ip)

# Задача №5

# net = ip_network('172.95.116.174/255.255.192.0', False)
#
# for ip in net:
#     b = bin(int(ip))[2:].zfill(32)
#
#     if b.count('1') % 5 == 0:
#         print(ip)
#         break

# Задача №6

# net = ip_network('98.71.254.171/255.248.0.0', False)
# for ip in net.hosts():
#     b = bin(int(ip))[2:].zfill(32)
#
#     if b.count('1') % 7 == 0:
#         print(ip)
#         break



# Задача №7

# def f(ip):
#     b = bin(int(ip))[2:].zfill(32)
#     return b.count('1') > 15
#
# for A in range(0, 256):
#     net = ip_network(f'192.214.{A}.184/255.255.255.224', False)
#
#     if all(f(ip) == 1 for ip in net):
#         print(A)
#         break


# for A in range(0, 256):
#     net = ip_network(f'192.214.{A}.184/255.255.255.224', False)
#
#     c = 0
#     for ip in net:
#         b = bin(int(ip))[2:].zfill(32)
#         if b.count('1') > 15:
#             c += 1
#
#     if len(list(net)) == c:
#         print(A)
#         break

# Задача №8

# 0000 0000 = 0
# 1000 0000 = 128
# 1100 0000 = 192
# 1110 0000 = 224
# 1111 0000 = 240
# 1111 1000 = 248
# 1111 1100 = 252
# 1111 1110 = 254
# 1111 1111 = 255

m = [0, 128, 192, 224, 240, 248, 252, 254, 255]
for A in m:
    net = ip_network(f'127.63.67.1/255.255.{A}.0', False)

    c = 0
    for ip in net:
        b = bin(int(ip))[2:].zfill(32)
        levie = b[:16]
        pravie = b[16:]

        if levie.count('1') >= pravie.count('1'):
            c += 1

    if len(list(net)) == c:
        print(A)
        break
















