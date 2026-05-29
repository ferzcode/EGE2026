# x = 7 * y
# x = 343

# y = x / 7 = 343 / 7 = 49

# (343, 49)

def check(A):
    for dx in range(-1000,1000):
        for dy in range(-1000, 1000):
            x = 343 + dx
            y = 49 + dy

            # if x >= 0 and y >= 0:
            f = (x * y < A) or (x < 7 * y) or (343 < x)
            if f == 0:
                return 0

    return 1


for A in range(16808, 0, -1):
    if check(A) == 1:
        print(A)