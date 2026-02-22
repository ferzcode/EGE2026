# Если маска подсети 255.255.252.0 и IP-адрес компьютера в сети 156.132.15.138, то чему будет равен номер компьютера в сети?

from ipaddress import *

net = ip_network('156.132.15.138/255.255.252.0', False)
nomer = -1

for ip in net:
    nomer += 1

    if ip == ip_address('156.132.15.138'):
        print(nomer)