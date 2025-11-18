from math import *

for N in range(1, 10000):
    i = ceil(log(N, 2))
    V1 = ceil((246 * i) / 8)

    if V1 * 703_569 <= 77 * 1024 * 1024:
        print(N)