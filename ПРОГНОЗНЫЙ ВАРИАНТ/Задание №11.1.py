from math import *

N = 10 + 62
i = ceil(log(N, 2))
for k in range(1, 10000000):
    V1 = ceil((k * i) / 8)

    if V1 * 5_895_222 > 23 * 1024 * 1024:
        print(k)
        break