# Определите максимальное кол-во символов в непрерывной последовательности
# котора является корректным арифм. выражением с целыми
# НЕОТРИЦАТЕЛЬНЫМИ числами (без знака)
# В этом выражении отсутсвуют незначащие нули

from re import *

s = open('24.txt').readline()
res = []
reg = r'(?=((0|[1-9][0-9]*)([+*](0|[1-9][0-9]*))+))'
for c in finditer(reg, s):
    res.append([len(c[1]), c[1]])

print(max(res))



s = open('24.txt').readline()
for c in '123456789': s = s.replace(c, '1') # МЕНЯЕМ ВСЕ ЦИФРЫ КРОМЕ 0 НА 1
# ДЛЯ УДОБСТВА БУДУЩИХ ПРОВЕРОК

while '++' in s or '+01' in s or '+00' in s:
    s = s.replace('++', '+ +')
    s = s.replace('+01', '+0 1')
    s = s.replace('+00', '+0 0')

s = s.split()
maxi = 0
for s1 in s:
    for l in range(len(s1)):
        if s1[l] != '+':
            for r in range(l + m, len(s1)):
                if s1[r] != '+':
                    c = s1[l : r + 1]
                    if c[:2] not in '00' or c[:2] not in '01':
                        m = max(len(c), maxi)
print(m)
