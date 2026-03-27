from ipaddress import *

for mask in range(32, 0, -1):
    net1 = ip_network(f'158.116.11.146/{mask}', False)

    if str(net1.network_address) == '158.116.0.0':
        print(mask)
