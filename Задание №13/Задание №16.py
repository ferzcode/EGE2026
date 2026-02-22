#  Известно два узла с IP-адресами 123.20.103.136 и 123.20.103.151 принадлежат разным сетям с одинаковой маской.
#
# Определите значение 4 байта маски в этих сетях. Найденное значение представьте в десятичной системе счисления.

from ipaddress import *

for mask in range(32, -1, -1):
    net1 = ip_network(f'123.20.103.136/{mask}', False)
    net2 = ip_network(f'123.20.103.151/{mask}', False)

    if net1 != net2 and net1.network_address != ip_address('123.20.103.136') and net1.broadcast_address != ip_address('123.20.103.136') \
        and net2.network_address != ip_address('123.20.103.151') and net2.broadcast_address != ip_address('123.20.103.151'):
        print(mask)