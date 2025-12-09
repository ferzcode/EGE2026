from string import *

for x in printable[:14]:
    summa = int(f'4B3{x}1C7', 14) + int(f'5{x}G83F7', 17)

    if summa % 15 == 0:
        print(summa // 15)