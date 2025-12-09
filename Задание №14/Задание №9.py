from string import *

for x in printable[:29]:
    summa = int(f'923{x}874', 29) + int(f'524{x}6152', 29)

    if summa % 28 == 0:
        print(summa // 28)