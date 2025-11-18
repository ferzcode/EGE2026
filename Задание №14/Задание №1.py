number = 3 * 3125 ** 8 + 2 * 625 ** 7 - 4 * 625 ** 6 + 3 * 125 ** 5 - 2 * 25 ** 4 - 2025
c = 0
while number > 0:
    if number % 25 == 0:
        c = c + 1
    number = number // 25
print(c)