num = 5 * 729 ** 2024 + 3 * 243 ** 1413 - 7 * 81 ** 169 - 2 * 9 ** 107 + 3017
summa = 0
while num > 0:
    if (num % 27) <= 25 and (num % 27) % 2 == 0:
        summa += (num % 27)
    num //= 27
print(summa)