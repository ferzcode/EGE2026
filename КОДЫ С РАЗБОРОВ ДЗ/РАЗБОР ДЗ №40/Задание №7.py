from calendar import prcal

c = 0
for stroka in open('Задание №7.csv'):
    s = [int(x) for x in stroka.split()]

    povt = [x for x in s if s.count(x) > 1]
    nechetnie = [x for x in s if x % 2 != 0]

    if (len(povt) > 0) + (len(nechetnie) == 3) == 1:
        c += 1
print(c)