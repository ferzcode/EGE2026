nomer = 0
for stroka in open('Задание №3.txt'):
    s = sorted([int(x) for x in stroka.split()])
    nomer += 1

    povt = [x for x in s if s.count(x) == 2] # len == 4
    odin = [x for x in s if s.count(x) == 1] # len == 3
    nechetnie = [x for x in s if x % 2 != 0]


    if len(povt) == 4 and len(odin) == 3:
        if sum(povt) <= sum(nechetnie):
            print(nomer, sum(s))
            break