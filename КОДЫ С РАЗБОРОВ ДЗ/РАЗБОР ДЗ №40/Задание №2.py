c = 0

for stroka in open('Задание №2.txt'):
    s = [int(x) for x in stroka.split()]
    chetnie = [x for x in s if x % 2 == 0]
    nechetnie = [x for x in s if x % 2 != 0]

    if max(s) < (sum(s) - max(s)):
        if sum(chetnie) == sum(nechetnie):
            c += 1
print(c)

