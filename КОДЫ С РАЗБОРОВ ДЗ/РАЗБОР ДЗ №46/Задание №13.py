def f(x):
    return (x % A == 0) or ((120 <= x <= 180) <= ((x % 16 != 0) or (x + A <= 204)))

for A in range(1, 1000):
    if all(f(x) == 1 for x in range(1, 1000)):
        print(A)
        