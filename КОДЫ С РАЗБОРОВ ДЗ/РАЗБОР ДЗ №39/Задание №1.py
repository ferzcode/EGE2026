c = 0

for stroka in open('Задание №1.txt'):
    s = [int(x) for x in stroka.split()]

    chetnie = [x for x in s if x % 2 == 0]
    nechetnie = [x for x in s if x % 2 != 0]

    if len(chetnie) == len(nechetnie):
        if min(s) ** 2 <= (sum(s) - min(s)):
            c += 1
print(c)