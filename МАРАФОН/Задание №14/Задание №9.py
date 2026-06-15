from string import *

for x in printable[:25]:
    num = int(f'A4{x}7F2', 25) + int(f'N{x}G5{x}H', 25) + int(f'74{x}M26', 25)

    if num % 24 == 0:
        print(num // 24)