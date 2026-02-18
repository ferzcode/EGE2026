# Два узла, находящиеся в одной сети, имеют IP-адреса 200.154.190.12 и 200.154.184.0.
# Укажите наибольшее возможное количество единиц в маске этой сети.
#
# Учтите, что два адреса в любой подсети зарезервированы: адрес всей подсети и широковещательный адрес.

from ipaddress import *

for mask in range(32, -1, -1):
    net1 = ip_network(f'200.154.190.12/{mask}', False)
    net2 = ip_network(f'200.154.184.0/{mask}', False)

    if net1 == net2 and net1.network_address != ip_address('200.154.190.12') and net2.network_address != ip_address('200.154.184.0') \
            and net1.broadcast_address != ip_address('200.154.190.12') and net2.broadcast_address != ip_address('200.154.184.0'):
        print(mask)