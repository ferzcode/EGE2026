def f(x):
    B = 36 <= x <= 75
    C = 60 <= x <= 110
    A = a1 <= x <= a2

    return ((not A) <= (B == C))


points = [35.9, 36, 36.1, 74.9, 75, 75.1, 59.9, 60, 60.1, 109.9, 110, 110.1]
otvet = []

for a1 in points:
    for a2 in points:
        if a2 >= a1 and all(f(x) == 1 for x in points):
            otvet.append(a2 - a1)

print(round(min(otvet)))