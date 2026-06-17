from fnmatch import *

def f(num):
    d = set()
    for i in range(1, round(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return d

for x in range(1, 10 ** 6):
    if fnmatch(str(x), '12*567'):
        d = f(x)

        S = sum(d)
        if S % 12 == 0:
            print(x, S)
