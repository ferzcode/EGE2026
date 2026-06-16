nomer = 0
for stroka in open('9_23193.txt'):
    nomer += 1

    s = [int(x) for x in stroka.split()]
    tri = [x for x in s if s.count(x) == 3] # len(tri) == 3
    odin = [x for x in s if s.count(x) == 1] # len(odin) == 3

    if len(odin) == 3 and len(tri) == 3:
        if tri[0] > (sum(odin) / len(odin)):
            print(nomer)

