# Текстовый файл состоит не более чем из 106 символов L, D и R.
# Определите максимальную длину цепочки вида LDRLDRLDR...
# (составленной из фрагментов LDR, последний фрагмент может быть неполным).

f = open('Задание №3.txt').readline()

k = 0
mx = 0
for i in range(len(f)):
    if (f[i] == 'L' and k % 3 == 0) or (f[i] == 'D' and k % 3 == 1) or (f[i] == 'R' and k % 3 == 2):
        k += 1
        mx = max(mx, k)
    elif f[i] == 'L':
        k = 1
    else:
        k = 0

print(mx)

# 012 345 678
# LDR LDR LDR LDR LD

    # LDR LDR LDR LD
    # L    % 3 == 0
    # D    % 3 == 1
    # R    % 3 == 2