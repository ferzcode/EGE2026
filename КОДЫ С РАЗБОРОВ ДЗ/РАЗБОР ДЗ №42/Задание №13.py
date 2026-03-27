f = 56000
i = 15
n = 2
t = 1647

for zagolovok in range(1_000_000_00):
    v1 = f * i * n * t + 28 * zagolovok * 1024 * 8
    v2 = 332 * 367_217_732

    if v2 < v1:
        print(zagolovok)
        break