def f(x):
    return (((x % 7 != 0) and (x % 13 == 0)) <= (x > A - 40))

for A in range(1, 1000):
    if all(f(x) == 1 for x in range(1, 1000)):
        print(A)