def f(x):
    P = 13 <= x <= 19
    Q = 17 <= x <= 23
    A = a1 <= x <= a2

    return ((not((not P) <= Q)) <= (A <= ((not Q) <= P)))

otvet = []
points = [12.9, 13, 13.1, 18.9, 19, 19.1, 16.9, 17, 17.1, 22.9, 23, 23.1]
for a1 in points:
    for a2 in points:
        if a2 >= a1 and all(f(x) == 1 for x in points):
            otvet.append(a2 - a1)
print(max(otvet))