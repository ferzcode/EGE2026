from math import *

k = 246
for N in range(1, 100000000):
    i = ceil(log(N, 2))
    V1 = ceil((k * i) / 8)

    if V1 * 703569 <= 77 * 1024 * 1024:
        print(N)
