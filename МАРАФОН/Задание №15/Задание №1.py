def f(n):
    d = set()
    for i in range(2, round(n ** 0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return d


def F(x):
    return ((x in C) <= ((x in A) and (x not in B)))


A = [i for i in range(100, 201)]
B = f(121)

for y in range(1, 20000):
    C = f(y)

    if all(F(x) for x in range(1, 10000)) and len(C) != 0:
        print(y)
