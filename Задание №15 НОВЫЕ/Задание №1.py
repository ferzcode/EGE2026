# 3x = y
# 535 = x

# y = 3 * 535 = 1605
# (535, 1605)

def check(A):
    for dx in range(-535, 200):
        for dy in range(-1605, 200):
            x = 535 + dx
            y = 1605 + dy

            f = (x * y < A) or (3 * x < y) or (535 <= x)
            if f == 0:
                return 0

    return 1

for A in range(855469, 0, -1):
    if check(A) == 1:
        print(A)