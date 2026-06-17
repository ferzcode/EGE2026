def f(x):
    B = 22 <= x <= 40
    C = 32 <= x <= 50
    A = a1 <= x <= a2

    return ((not A) <= (B == C))


r = []
p = [21.9, 22, 22.1, 39.9, 40, 40.1, 31.9, 32, 32.1, 49.9, 50, 50.1]
for a1 in p:
    for a2 in p:
        if a2 >= a1 and all(f(x) == 1 for x in p):
            r.append(a2 -a1)
print(min(r))