from string import *

for x in printable[:29]:
    number = int(f'463{x}7921', 29) + int(f'8241{x}153', 29)

    if number % 28 == 0:
        print(number // 28)