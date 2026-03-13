# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите максимальное количество идущих подряд символов,
# среди которых каждая из букв C и D встречается не более двух раз.

f = open('Задание №10.txt').readline()
mx = 1

for l in range(0, len(f)):
    for r in range(l + mx, len(f)):
        s = f[l : r + 1]

        if s.count('C') > 2 or s.count('D') > 2: break
        if s.count('C') <= 2 and s.count('D') <= 2: mx = max(mx, len(s))

print(mx)