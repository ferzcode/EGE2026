# from ipaddress import *
#
# net = ip_network(f'134.80.0.0/255.240.0.0', False)
#
# max_sum = []
# for ip in net.hosts():
#     b = bin(int(ip))[2:].zfill(32)
#
#     if b.count('0') == b.count('1'):
#         ip_stroka = str(ip)
#
#         s = sum(int(octet) for octet in ip_stroka.split('.'))
#         max_sum.append(s)
# print(max(max_sum))

from ipaddress import *

net = ip_network(f'134.80.0.0/255.240.0.0', False)

max_sum = []
for ip in net.hosts():
    b = bin(int(ip))[2:].zfill(32)

    if b.count('0') == b.count('1'):
        ip_stroka = str(ip).replace('.', '+')
        s = eval(ip_stroka)

        max_sum.append(s)
print(max(max_sum))