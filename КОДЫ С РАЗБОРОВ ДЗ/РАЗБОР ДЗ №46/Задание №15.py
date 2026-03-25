def f(x):
    return (x & 79 != 0) and ((x & 31 == 0) <= (x & A != 0))

for A in range(1, 1000):
    if all(f(x) == 1 for x in range(90, 101)):
        print(A)
        break