from re import findall

f = open('24_23381.txt').readline()

# mx = []
# alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#
# for bukva in alp:
#     reg = fr'(?=([02468][{bukva}]+[02468]))'
#
#     for stroka in findall(reg, f):
#         mx.append(len(stroka))
# print(max(mx))

mx = []
reg = r'(?=([02468][A-Z]+[02468]))'
for stroka in findall(reg, f):
    s = stroka[1:-1] # ВСЯ СТРОКА, НО БЕЗ ПЕРВОЙ ЦИФРЫ И ПОСЛЕДНЕЙ ЦИФРЫ
    if len(set(s)) == 1:
        mx.append(len(stroka))

print(max(mx))


