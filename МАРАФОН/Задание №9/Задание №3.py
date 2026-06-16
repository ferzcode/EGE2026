nomer = 0
for stroka in open('9_23268.txt'):
    s = [int(x) for x in stroka.split()]
    nomer += 1

    dva = [x for x in s if s.count(x) == 2] # len(dva) == 4
    odin = [x for x in s if s.count(x) == 1] # len(odin) == 3\

    if len(dva) == 4 and len(odin) == 3:
        if (sum(dva) / len(dva)) < max(odin):
            print(nomer, sum(s))
            break