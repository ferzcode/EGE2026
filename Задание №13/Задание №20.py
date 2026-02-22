# Два узла, находящиеся в одной сети, имеют IP-адреса 121.171.5.70 и 121.171.5.107.
#
# Укажите наименьшее возможное количество адресов в этой сети.

from ipaddress import *

for mask in range(32, -1, -1):
    net1 = ip_network(f'121.171.5.70/{mask}', False)
    net2 = ip_network(f'121.171.5.107/{mask}', False)

    if net1 == net2 and ip_address('121.171.5.70') in net1.hosts() and ip_address('121.171.5.107') in net2.hosts():
        print(mask)

# ВЫБИРАЕМ НАИБОЛЬШУЮ МАСКУ => МЕНЬШЕ 0 И МЕНЬШЕ АДРЕСОВ
# 2 ** 6 == 64
