nomer = 0

for stroka in open('Задание №1.txt'):
    s = [int(x) for x in stroka.split()]
    nomer += 1

    povt = [x for x in s if s.count(x) == 3] # len == 6
    odin = [x for x in s if s.count(x) == 1] # len == 1

    if len(povt) == 6 and len(odin) == 1:
        if odin[0] <= min(povt):
            print(nomer, max(povt))
            break
