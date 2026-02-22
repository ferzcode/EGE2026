# В двух подсетях используются одинаковые маски. Известно, что два узла, находящиеся в первой подсети,
# имеют IP-адреса – 167.77.194.47 и 167.77.194.37, и один узел из второй сети имеет IP-адрес 167.77.200.25.
# Сколько существует масок, при которых соблюдается условие задачи?

from ipaddress import *

c = 0
for mask in range(32, -1, -1):
    net1 = ip_network(f'167.77.194.47/{mask}', False)
    net2 = ip_network(f'167.77.200.25/{mask}', False)

    if net1 != net2 and ip_address('167.77.194.47') in net1.hosts() and ip_address('167.77.194.37') in net1.hosts() and ip_address('167.77.200.25') in net2.hosts():
        c += 1
print(c)
