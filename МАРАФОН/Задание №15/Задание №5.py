def check(A):
    for x in range(1, 78125):
        y = 78125 - 4 * x

        if y >= 1:
            f = (78125 != y + 4 * x) or (A > x ) and (A > y)
            if f == 0:
                return 0
    return 1

for A in range(78122, 0, -1):
    if check(A) == 1:
        print(A)