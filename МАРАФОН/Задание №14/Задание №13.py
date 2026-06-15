from string import *

for x in printable[:15]:
    for y in printable[:17]:
        num = int(f'123{x}5', 15) + int(f'67{y}9', 17)

        if num % 131 == 0:
            print(y, num // 131)