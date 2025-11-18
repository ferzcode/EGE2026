num = 4 ** 644 + 4 ** 322 + 16 ** 35 - 64 ** 3
c = 0
while num > 0:
    if num % 4 == 3:
        c = c + 1
    num = num // 4
print(c)