from string import *

for x in printable[:16]:
    for y in printable[:16]:
        number = int(f'27A{x}23', 16) + int(f'8{y}E5D2', 16)

        if number % 5 == 0:
            print(x, y, int(x, 16) + int(y, 16))
