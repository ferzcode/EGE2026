A = range(100, 200)
B = [i for i in range(2, 121) if 121 % i == 0]

def f(x):
    return ((x in C) <= ((x in A) and not(x in B)))

for y in range(1, 20_000):
    C = [i for i in range(2, y) if y % i == 0]
    if len(C) > 0:
        if all(f(x) == 1 for x in range(1, 5000)):
            print(y)
            break