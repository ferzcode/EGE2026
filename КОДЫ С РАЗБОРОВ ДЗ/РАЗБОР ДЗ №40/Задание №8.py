from ipaddress import *

net = ip_network('95.24.30.144/255.255.248.0' , False)
print(net[1])