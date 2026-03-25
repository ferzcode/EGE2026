def f(x):
    return ((x % A != 0) <= ((x % 28 == 0) <= (x % 49 != 0)))

for A in range(1, 1000):
    if all(f(x) == 1 for x in range(1, 1000)):
        print(A)