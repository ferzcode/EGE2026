# ДОСРОК2026

from fnmatch import *
for x in range(0, 10 ** 10, 9874):
    if fnmatch(str(x), '89*6?7?9?'):
        print(x, x // 9874)

# ЕГКР2026

from math import *

def deliteli(num):
    d = []
    for i in range(2, round(num ** 0.5) + 1):
        if num % i == 0:
            d.append(i)
            d.append(num // i)
    return d

c = 0
for num in range(8_996_453, 10_000_000):
    d = deliteli(num) # ВСЕ ДЕЛИТЕЛИ
    prostie = [dl for dl in d if len(deliteli(dl)) == 0 and str(dl).count('3') == 2]

    if len(prostie) == 2 and prod(prostie) == num:
        print(num, max(prostie))
        c += 1

    if c == 5:
        break

# АПРОБАЦИЯ2026

from fnmatch import *

for x in range(0, 10 ** 8, 271):
    if fnmatch(str(x), '12??15*6'):
        print(x, x // 271)

# ЕГКР2026

def deliteli(num):
    d = set()
    for i in range(2, round(num ** 0.5) + 1):
        if num % i == 0:
            d.add(i)
            d.add(num // i)
    return d

c = 0
for num in range(1_350_051, 2_000_000):
    d = deliteli(num)

    d11 = [dl for dl in d if dl % 100 == 11 and dl != 11 and dl != num]
    if len(d11) > 0:
        print(num, min(d11))
        c += 1

    if c == 5:
        break


# ДЕМО2026

def deliteli(num):
    d = set()
    for i in range(2, round(num ** 0.5) + 1):
        if num % i == 0:
            d.add(i)
            d.add(num // i)
    return d

c = 0
for num in range(800_001, 1_000_000):
    d = deliteli(num)

    M = max(d) + min(d) if len(d) > 0 else 0
    if M % 10 == 4:
        print(num, M)
        c += 1

    if c == 5:
        break

# ПЕРЕСДАЧА ЕГЭ2026

from math import *

def deliteli(num):
    d = []
    for i in range(2, round(num ** 0.5) + 1):
        if num % i == 0:
            d.append(i)
            d.append(num // i)
    return d

c = 0
for num in range(6_086_056, 10_000_000):
    d = deliteli(num) # все делители   7
    prostie = [dl for dl in d if len(deliteli(dl)) == 0 and str(dl).count('6') == 1]

    if len(prostie) == 2 and prod(prostie) == num:
        print(num, max(prostie))
        c += 1

    if c == 5:
        break

# РЕЗЕРВ 2026

from math import *

def deliteli(num):
    d = []
    for i in range(2, round(num ** 0.5) + 1):
        if num % i == 0:
            d.append(i)
            d.append(num // i)
    return d

c = 0
for num in range(6_651_221, 7_000_000):
    d = deliteli(num)
    pr = [dl for dl in d if len(deliteli(dl)) == 0 and str(dl).count('2') == 1]

    if len(pr) == 2 and prod(pr) == num:
        print(num, max(pr))
        c += 1

    if c == 5:
        break

# ОСНОВНАЯ 2025

from math import *

def deliteli(num):
    d = set()
    for i in range(2, round(num ** 0.5) + 1):
        if num % i == 0:
            d.add(i)
            d.add(num // i)
    return d

c = 0
for num in range(5_400_001, 6_000_000):
    d = deliteli(num)
    pr = [dl for dl in d if len(deliteli(dl)) == 0]

    M = min(pr) + max(pr) if len(pr) > 0 else 0

    if M > 60000 and str(M) == str(M)[::-1]:
        print(num, M)
        c += 1

    if c == 5:
        break

# ОТКРЫТЫЙ 2025

def deliteli(num):
    d = set()
    for i in range(1, round(num ** 0.5) + 1):
        if num % i == 0:
            d.add(i)
            d.add(num // i)
    return d

c = 0
for num in range(500_001, 1_000_000):
    d = deliteli(num)

    R = sum(d)
    if str(R)[-1] == '6':
        print(num, R)
        c += 1
    if c == 5:
        break

# КРЫЛОВ 2026

from math import *

st3 = [3 ** x for x in range(1, 12)]
d103 = [x for x in range(0, 1_000_000, 103) if x % 2 != 0]

podh = []
for c1 in d103:
    for c2 in st3:
        num = c1 + c2

        if 100_000 <= num <= 999_999 and str(num).count('1') == 0:
            podh.append([num, c2])


for c, st in sorted(podh)[:5]:
    print(c, round(log(st, 3)))


















