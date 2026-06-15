a = []

for x in range(2, 2026):
    num = 5 ** 2025 + 5 ** 200 - x

    c = 0
    while num > 0:
        if num % 5 == 4:
            c += 1
        num //= 5

    if c == 199:
        print(x)

    # a.append(c)
# print(max(a))