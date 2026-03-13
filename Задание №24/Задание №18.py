# Текстовый файл состоит из символов F, G, Q, R, S и W.
# Определите в прилагаемом файле максимальное количество идущих подряд символов,
# среди которых подстрока FSRQ встречается ровно 80 раз.


f = open('Задание №9.txt').readline()
mx = 1

for l in range(0, len(f)):
    for r in range(l + mx, len(f)):
        s = f[l : r + 1]

        if s.count('FSRQ') > 80: break
        if s.count('FSRQ') == 80: mx = max(mx, len(s))
print(mx)