def f(x):
    P = 25 <= x <= 64
    Q = 40 <= x <= 115
    A = a1 <= x <= a2

    return (P <= ((Q and (not A)) <= (not P)))

r = [] # РЕЗУЛЬТАТЫ
p = [24.9, 25, 25.1, 63.9, 64, 64.1, 39.9, 40, 40.1, 114.9, 115, 115.1]

for a1 in p:
    for a2 in p:
        if a2 >= a1 and all(f(x) == 1 for x in p):
            r.append(a2 - a1)
print(min(r))