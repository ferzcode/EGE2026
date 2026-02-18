# ЗАДАЧА №1

# n1 = 2
# f1 = 48000
# i1 = 32
# t1 = 2.5 * 60
#
# U = 128_0000
#
# i2 = i1 // 2
# f2 = 32000
# n2 = n1
# t2 = t1
#
# V1 = f1 * i1 * n1 * t1
# V2 = f2 * i2 * n2 * t2
#
# t = ((V1 - V2) / U) / 60
# print(t)

# ЗАДАЧА №2

# x = 7680
# y = 4320
# i = 16
#
# Vcard = 9 * 1024 * 1024 * 1024 * 8
# Ncard = (Vcard // (x * y * i))
#
# print(4010 % Ncard)

# ЗАДАЧА №3

# from math import ceil
#
# x = 3840
# y = 2160
# i = 24
#
# V1 = (x * y * i) * 0.65 + 120 * 1024 * 8
# Vcard = 20 * 1024 * 1024 * 1024 * 8
# Ncard = Vcard // V1
#
# print(ceil(4320 / Ncard))

# ЗАДАЧА №4

# n = 2
# f = 48000
# i = 24
# V_sjatiy = 20                       # 100%
# V_origin = (V_sjatiy * 140) / 100   # 140%
#
# t = (V_origin * 1024 * 1024 * 8) / (f * i * n)
# print(t)

# ЗАДАЧА №5

# n = 2
# f = 96000
# t = 3 * 60 + 33
# V_sjatogo = 25                        # 60%
# V_origin =  (V_sjatogo * 100) / 60    # 100%
#
# print((V_origin * 1024 * 1024 * 8) / (f * n * t))
from math import *

for Nmin in range(1, 10_000_000):
    x = 2560
    y = 1440
    i = ceil(log(Nmin, 2))
    n = 52

    U = 8388608
    if (x * y * i * n) / U >= 520:
        print(Nmin)
        break












