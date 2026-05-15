a = []
for x in range(1, 3001):
    num = 4 ** 210 + 4 ** 110 - x

    c0 = 0
    while num > 0:
        if num % 4 == 0:
            c0 += 1
        num //= 4

    if c0 == 105:
        print(x)
        break

#     a.append(c0)
# print(max(a))