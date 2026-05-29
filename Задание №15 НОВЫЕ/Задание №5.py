# 5y = x
# 2x + 3y = 100001

# 13y = 100001
# y = 7692
# x = 38460

def check(A):
    for dx in range(-2000, 2000):
        for dy in range(-2000, 2000):
            x = 38460 + dx
            y = 7692 + dy

            f = (x > A) or (5 * y > x) or (2 * x + 3 * y < 100001)
            if f == 0:
                return 0

    return 1

for A in range(38462, 10 ** 8, 1):
    if check(A) == 1:
        print(A)