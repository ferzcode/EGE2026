from ipaddress import *

for mask in range(32, -1, -1):
    net1 = ip_network(f'200.154.190.12/{mask}', False)
    net2 = ip_network(f'200.154.184.0/{mask}', False)

    if net1 == net2 and net1.network_address != ip_address('200.154.190.12') and \
            net1.network_address != ip_address('200.154.184.0') and \
            net1.broadcast_address != ip_address('200.154.190.12') and \
            net1.broadcast_address != ip_address('200.154.184.0'):
        print(mask)