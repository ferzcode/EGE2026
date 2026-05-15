a = [] # СЮДА БУДЕМ КЛАСТЬ КОЛИЧЕСТВО НУЛЕЙ ДЛЯ КАЖДОГО ЧИСЛА
for x in range(1, 2031):
    num = 6 ** 2030 + 6 ** 100 - x

    c0 = 0
    while num > 0:
        if num % 6 == 0:
            c0 += 1
        num //= 6

    a.append(c0)
print(min(a))