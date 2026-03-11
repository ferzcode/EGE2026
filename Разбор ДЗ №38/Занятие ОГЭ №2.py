# 1 ШАБЛОН
# ЕСЛИ В ПРОГРАММУ ВВОДИТСЯ КОЛИЧЕСТВО ПОСЛЕДУЮЩИХ ЗНАЧЕНИЙ

# N = int(input())
# c = 0
# summa = 0
#
# for i in range(N):
#     massa = int(input())
#
#     if massa > 10:
#         c = c + 1
#         summa = summa + massa
#
# print(summa / c)
# print(c)



# N = int(input())
# c = 0
# obsch_chisl = 0
# for i in range(N):
#     normativ = int(input())
#
#     if 13 <= normativ <= 20:
#         c = c + 1
#         obsch_chisl = obsch_chisl + normativ
#
# print(obsch_chisl / c)
# print(c)


# kolvo_vv = int(input())
# podhodyach = 0
# for i in range(kolvo_vv):
#     chislo = int(input())
#
#     if chislo // 10 > chislo % 10 and 10 <= chislo <= 99:
#         podhodyach = podhodyach + 1
# print(podhodyach)

obch = int(input())
summa = 0
for i in range(obch):
    new = int(input())

    if new % 2 == 0 and new < 30:
        summa = summa + new
print(summa)

    # % 10 - ПОСЛЕДНЯЯ ЦИФРА ЧИСЛА
    # % 100 - ПОСЛЕДНИЕ ДВЕ ЦИФРЫ ЧИСЛА
    # % 1000 - ПОСЛЕДНИЕ ТРИ ЦИФРЫ ЧИСЛА













