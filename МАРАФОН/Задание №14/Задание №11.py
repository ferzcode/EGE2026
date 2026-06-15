num = 6 ** 1333 - 5 * 6 ** 1215 + 3 * 6 ** 144 - 86
summa = 0

while num > 0:
    summa += num % 6
    num //= 6
print(summa)