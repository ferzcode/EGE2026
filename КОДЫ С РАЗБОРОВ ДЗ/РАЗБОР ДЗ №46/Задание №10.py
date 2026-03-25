nomer = 0

for stroka in open('Задание №3.txt'):
    s = [int(x) for x in stroka.split()]
    nomer += 1

    tri = [x for x in s if s.count(x) == 3] # len == 3
    dva = [x for x in s if s.count(x) == 2] # len == 2
    odin = [x for x in s if s.count(x) == 1] # len == 3

    if len(tri) == 3 and len(dva) == 2 and len(odin) == 3:
        if (sum(tri) + sum(dva)) > sum(odin):
            print(nomer, sum(s))