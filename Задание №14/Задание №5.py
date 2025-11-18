n = 5 * 343 ** 2031 + 4 * 49 ** 2142 - 3 * 7 ** 111 + 7 ** 222
summa = 0
while n > 0:
    summa = summa + n % 7
    n = n // 7
print(summa)