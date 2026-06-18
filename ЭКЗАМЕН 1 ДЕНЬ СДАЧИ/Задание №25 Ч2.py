# Пусть M - миним. и максим. простых
# делителей целого числа, не считая самого числа
# Если делителей нет - M равно 0
# Программа перебирает целые числа, большие
# 8 007 494 154, в порядке возрастания и ищет
# среди них такие, для которых М больше 80 000
# является простым числом и в своем написании
# последовательность цифр 567 ровно один раз


def f_M(num):  # M
    d = set()
    for i in range(2, round(num ** 0.5) + 1):
        if num % i == 0:
            d.add(i)
            d.add(num // i)
    return d


def f_prosite(num, d=2):
    for d in range(d, round(num ** 0.5) + 1):
        if num % d == 0:
            return [d] + f_prosite(num // d, d)
    return [num]


c = 0
for num in range(8_007_494_155, 8_200_000_000):
    d = set(f_prosite(num))

    M = min(d) + max(d) if len(d) >= 2 else 0

    if len(f_M(M)) == 0 and M > 80000 and str(M).count('567') == 1:
        print(num, M)
        c += 1

    if c == 5:
        break