from ipaddress import *

for mask in range(32, 0, -1):
    net = ip_network(f'84.23.84.23/{mask}', False)

    if str(net.network_address) == '84.23.84.0' and ip_address('84.23.84.23') in net.hosts():
        print(mask)

        # 27 = 8 8 8 3 = 255 + 224 = 479 