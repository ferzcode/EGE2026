# Для узла с IP-адресом 251.211.38.240 адрес сети равен 251.211.38.0.
# Для скольких различных значений маски это возможно? В ответе запишите только число.

from ipaddress import *

c = 0
for mask in range(16, 33):
    net = ip_network(f'251.211.38.240/{mask}', False)

#   if net.network_address == ip_address('251.211.38.0'):

    if '251.211.38.0' in str(net):
        c += 1
print(c)