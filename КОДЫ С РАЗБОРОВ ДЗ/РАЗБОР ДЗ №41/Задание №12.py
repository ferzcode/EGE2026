maxi = 0
for x in range(1, 7291):
    num = 27 ** 298 + 27 ** 269 - x

    c0 = 0
    while num > 0:
        if num % 27 == 0:
            c0 += 1
        num //= 27

    maxi = max(maxi, c0)

print(maxi)