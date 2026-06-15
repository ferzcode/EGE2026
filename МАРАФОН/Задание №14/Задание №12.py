from string import *

for x in printable[:15]:
    num = int(f'131{x}1', 15) + int(f'13{x}3', 17)
    if num % 11 == 0:
        print(x, num // 11)
