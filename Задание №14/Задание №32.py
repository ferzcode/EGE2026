from string import *

for x in printable[:22]:
    num = int(f'12313{x}57', 22) + int(f'1{x}34561', 22)

    if num % 21 == 0:
        print(x, num // 21)