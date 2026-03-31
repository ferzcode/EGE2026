nomer = 0

for stroka in open('Задание №2.txt'):
    s = [int(x) for x in stroka.split()]
    nomer += 1

    povt3 = [x for x in s if s.count(x) == 3] # len == 3
    povt2 = [x for x in s if s.count(x) == 2] # len == 2
    povt1 = [x for x in s if s.count(x) == 1] # len == 1

    if len(povt3) == 3 and len(povt2) == 2 and len(povt1) == 1:
        if povt1[0] <= min(povt2 + povt3):
            print(nomer, min(povt2 + povt3))


