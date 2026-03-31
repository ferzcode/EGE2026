nomer = 0

for stroka in open('Задание №4.txt'):
    s = [int(x) for x in stroka.split()]
    nomer += 1
    chetnie = [x for x in s if x % 2 == 0]
    nechetnie = [x for x in s if x % 2 != 0]

    if s[0] < s[1] < s[2] < s[3] < s[4] < s[5]:
        if len(chetnie) == len(nechetnie):
            print(nomer, sum(s))

