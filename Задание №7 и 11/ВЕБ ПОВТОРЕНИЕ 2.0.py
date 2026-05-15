from math import *

# ЗАДАЧА №1

# x = 6580
# y = 3240
# i = ceil(log(2048, 2))
# u = 3_964_685 * 8
#
# for n in range(1, 10000):
#     if (x * y * i * n) / u <= 510:
#         print(n)

# ЗАДАЧА №2

# for k in range(1, 10000):
#     N = 62 + 10
#     i = ceil(log(N, 2))
#
#     V1 = ceil((k * i) / 8) # БАЙТЫ
#     if V1 * 5_895_222 > 23 * 1024 * 1024:
#         print(k)
#         break

# ЗАДАЧА №3

# for N in range(1, 100000):
#     i = ceil(log(N, 2))
#     k = 65
#
#     V1 = ceil((k * i) / 8)
#     if V1 * 131072 < 9 * 1024 * 1024:
#         print(N)

# ЗАДАЧА №4

k = 289
N = 10 + 1015
i = ceil(log(N, 2))

V1 = ceil((k * i) / 8)
print((V1 * 524288) / (1024 * 1024))







