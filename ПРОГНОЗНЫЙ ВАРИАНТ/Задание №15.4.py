def f(x):
    return (((x & 17 !=0 ) <= ((x & A != 0) <= (x & 58 != 0))) <= ((x & 8 == 0) and (x & A != 0) and (x & 58 == 0)))

for A in range(1, 1000):
    if all(f(x) == 0 for x in  range(1, 1000)):
        print(A)