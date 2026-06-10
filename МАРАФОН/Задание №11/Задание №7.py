from math import *

k = 223
N = 10 + 26 + 32724

i = ceil(log(N, 2))
V1 = ceil((k * i) / 8)

for kolvo in range(1, 1000000000000):
    if kolvo * V1 <= 17 * 1024 * 1024 * 1024:
        print(kolvo)