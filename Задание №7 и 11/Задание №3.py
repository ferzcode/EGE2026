from math import *

for N in range(1, 10000):
    i = ceil(log(N, 2))
    V1 = ceil((172 * i) / 8)

    if V1 * 356984 >= 54 * 1024 * 1024:
        print(N)
        break