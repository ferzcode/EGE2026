def f(x):
    P = 15 <= x <= 40
    Q = 21 <= x <= 63
    A = a1 <= x <= a2

    return (P <= ((Q and (not A)) <= (not P)))

otvet = []
point = [14.9, 15, 15.1, 39.9, 40, 40.1, 20.9, 21, 21.1, 62.9, 63, 63.1]
for a1 in point:
    for a2 in point:
        if a2 >= a1 and all(f(x) == 1 for x in point):
            otvet.append(a2 - a1)
print(min(otvet))