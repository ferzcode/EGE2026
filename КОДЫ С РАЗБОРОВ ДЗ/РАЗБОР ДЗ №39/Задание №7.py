nomer = 0
for stroka in open('Задание №7.txt'):
    s = [int(x) for x in stroka.split()]
    nomer += 1
    povt = [x for x in s if s.count(x) == 2] # len == 2
    odin = [x for x in s if s.count(x) == 1] # len == 4

    if len(povt) == 2 and len(odin) == 4:
        if povt[0] >= (sum(odin) / len(odin)):
            print(nomer)
            break