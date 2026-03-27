from math import *

x = 1024
y = 960
i = ceil(log(16384, 2))

V = x * y * i * 400
print(V / (8 * 1024 * 1024))