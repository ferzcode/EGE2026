cl1 = []
cl2 = []
yellow1 = []
yellow2 = []
for stroka in open('Задание №3 А.txt'):
    zv = stroka.replace(',','.').split()

    x = float(zv[0])
    y = float(zv[1])
    h = str(zv[2])

    if y > 10:
        cl1.append([x, y])
        if h[0] == 'Z':
            yellow1.append([x, y])
    if y < 10:
        cl2.append([x, y])
        if h[0] == 'Z':
            yellow2.append([x, y])

print(len(yellow1), len(yellow2))
