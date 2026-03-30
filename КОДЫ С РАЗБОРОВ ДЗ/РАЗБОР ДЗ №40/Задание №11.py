def f(x):
    return (((x & 117 != 0) and (x & 91 == 0)) <= (x & A != 0))

for A in range(0, 1000):
    if all(f(x) == 1 for x in range(0, 1000)):
        print(A)
        break