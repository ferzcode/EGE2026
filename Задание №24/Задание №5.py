# Текстовый файл состоит из символов A, C, D, F и O.
# Определите максимальное количество идущих подряд пар символов вида: согласная + гласная.

f = open('Задание №5.txt').readline()

f = f.replace('O', 'A').replace('D', 'C').replace('F', 'C')
k = 0
mx = 0

for i in range(0, len(f) - 1, 2):
    if f[i] == 'C' and f[i + 1] == 'A':
        k += 1
        mx = max(mx, k)
    else:
        k = 0
print(mx)