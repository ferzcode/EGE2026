c = 0
for stroka in open('Задание №6.txt'):
    s = [int(x) for x in stroka.split()]

    if (len(s) == len(set(s))) + ((max(s) + min(s)) * 2 <= (sum(s) - min(s) - max(s))* 3) == 1:
        c += 1

print(c)