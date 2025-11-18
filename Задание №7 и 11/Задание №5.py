from math import *

k = 223
N = 10 + 26 + 32724

i = ceil(log(N,2))
V1 = ceil((k * i) / 8)

print((17 * 1024 * 1024 * 1024) // V1)

# for nomer in range(1, 100000000000):
#     k = 223
#     N = 10 + 26 + 32724
#
#     i = ceil(log(N,2))
#     V1 = ceil((k * i) / 8)
#
#     if V1 * nomer <= 17 * 1024 * 1024 * 1024:
#         print(nomer)