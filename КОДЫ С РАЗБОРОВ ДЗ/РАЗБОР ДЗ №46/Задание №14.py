def f(x):
    B = 34 <= x <= 72
    C = 32 <= x <= 61
    A = a1 <= x <= a2

    return (B <= A) and ((not C) or A)


otvet = []
point = [33.9, 34, 34.1, 71.9, 72, 72.1, 31.9, 32, 32.1, 60.9, 61, 61.1]

for a1 in point:
    for a2 in point:
        if a2 >= a1 and all(f(x) == 1 for x in point):
            otvet.append(a2 - a1)

print(min(otvet))