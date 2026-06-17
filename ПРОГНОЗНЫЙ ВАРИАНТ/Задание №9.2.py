nomer = 0
for stroka in open('Задание №9 В2.txt'):
    s = [int(x) for x in stroka.split()]
    nomer += 1

    tri = [x for x in s if s.count(x) == 3] # len == 3
    odin = [x for x in s if s.count(x) == 1] # len == 3

    if len(tri) == 3 and len(odin) == 3:
        if tri[0] > (sum(odin) / len(odin)):
            print(nomer)