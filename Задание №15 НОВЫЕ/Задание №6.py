# 5x = y
# 486 = x

# y = 486 * 5 = 2430

# (486, 2430)

def check(A):
    for dx in range(-1000, 1000):
        for dy in range(-1000, 1000):
            x = 486 + dx
            y = 2430 + dy

            f = (x * y < A) or (5 * x < y) or (486 <= x)
            if f == 0:
                return 0

    return 1

for A in range(1176126, 0, -1):
    if check(A) == 1:
        print(A)