nomer = 0

for stroka in open('Задание №5.txt'):
    s = [int(x) for x in stroka.split()]
    nomer += 1

    povt = [x for x in s if s.count(x) == 3] # len == 3
    odin = [x for x in s if s.count(x) == 1] # len == 4

    if len(povt) == 3 and len(odin) == 4:
        if sum(povt) / len(povt) > sum(s) / len(s):
            print(nomer)