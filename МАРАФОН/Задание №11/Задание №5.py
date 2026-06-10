from math import *

N = 10 + 52 + 972
i = ceil(log(N, 2))

for k in range(1, 10000000):
    V1 = ceil((k * i) / 8)

    if V1 * 2048 > 172 * 1024:
        print(k)
        break

