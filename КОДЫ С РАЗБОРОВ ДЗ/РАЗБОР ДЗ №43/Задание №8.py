from ipaddress import *

def proverka(ip):
    binary = bin(int(ip))[2:].zfill(32)
    return binary[:16].count('1') <= binary[16:].count('1')

# 0000 0000 = 0
# 1000 0000 = 128
# 1100 0000 = 192
# 1110 0000 = 224
# 1111 0000 = 240
# 1111 1000 = 248
# 1111 1100 = 252
# 1111 1110 = 254
# 1111 1111 = 255

maskA = [0, 128, 192, 224, 240, 248, 252, 254, 255]

for A in maskA:
    net = ip_network(f'99.8.254.232/255.255.{A}.0', False)

    if all(proverka(ip) == 1 for ip in net):
        print(A)


