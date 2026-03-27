def f(x):
    P = 17 <= x <= 58
    Q = 29 <= x <= 80
    A = a1 <= x <= a2
    return (P <= ((Q and (not A)) <= (not P)))


points = [16.9, 17, 17.1, 57.9, 58, 58.1, 28.9, 29, 29.1, 79.9, 80, 80.1]
otvet = []

for a1 in points:
    for a2 in points:
        if a2 >= a1 and all(f(x) == 1 for x in points):
            otvet.append(a2 - a1)

print(round(min(otvet)))