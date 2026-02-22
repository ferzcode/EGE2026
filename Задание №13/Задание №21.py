from ipaddress import *

# Для узла c IP-адресом 175.122.80.13 адрес подсети равен 175.122.80.0. Сколько существует различных возможных значений маски,
# если известно, что в этой сети не менее 28 узлов? Ответ запишите в виде десятичного числа.

c = 0
for mask in range(27, -1, -1):
    net = ip_network(f'175.122.80.13/{mask}', False)

    if net.network_address == ip_address('175.122.80.0') and ip_address('175.122.80.13') in net.hosts():
        c += 1
print(c)