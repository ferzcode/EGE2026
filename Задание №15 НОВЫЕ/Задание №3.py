# 3x + 4y = 84882
# x = y

# 7y = 84882
# (12126,  12126)

def check(A):
    for dx in range(-2000, 2000):
        for dy in range(-2000, 2000):
            x = 12126 + dx
            y = 12126 + dy

            f = (3 * x + 4 * y != 84882) or (x < y) or (A < x)
            if f == 0:
                return 0
    return 1

for A in range(12121, 10 ** 8, 1):
    if check(A) == 1:
        print(A)