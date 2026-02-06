# Напишите программу, которая перебирает целые числа, большие 12 365 266, в порядке возрастания и ищет среди них те,
# которые можно представить в виде произведения ровно пяти различных простых множителей,
# а сумма этих множителей образует простое число.
#
# В ответе в первом столбце таблицы запишите первые 5 найденных чисел в порядке возрастания,
# во втором столбце — сумму их простых множителей.

from math import prod

def f(x):
    d = set()

    for delit in range(2, round(x ** 0.5) + 1):
        if x % delit == 0:
            d.add(delit)
            d.add(x // delit)
    return d

# def prosto(x):
#     return x > 1 and all(x % delit != 0 for delit in range(2, round(x ** 0.5) + 1))
# True - простое | False - не простое

c = 0
for x in range(12_365_267, 15_000_000):
    d = f(x) # ВСЕ ДЕЛИТЕЛИ
    prostie = [pd for pd in d if len(f(pd)) == 0]

    if len(prostie) == 5 and prod(prostie) == x and len(f(sum(prostie))) == 0 and c < 5:
        print(x, sum(prostie))
        c += 1