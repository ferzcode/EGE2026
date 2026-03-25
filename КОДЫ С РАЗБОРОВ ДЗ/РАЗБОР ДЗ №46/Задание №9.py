nomer = 0

for stroka in open('Задание №2.txt'):
    s = [int(x) for x in stroka.split()]
    nomer += 1

    if s[0] > s[1] > s[2] > s[3] > s[4] > s[5] > s[6]:
        if (min(s) + max(s)) / 2 > (sum(s) - min(s) - max(s)) / 5:
            print(nomer, sum(s))
            break