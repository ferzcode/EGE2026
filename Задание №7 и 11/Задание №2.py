from math import *

for k in range(1, 10000):
    N = 10 + 17
    i = ceil(log(N, 2))
    V1 = ceil((k * i) / 8)

    if V1 * 7564230 > 31 * 1024 * 1024:
        print(k)