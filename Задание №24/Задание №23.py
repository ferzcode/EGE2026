# Текстовый файл состоит из символов, обозначающих прописные латинские буквы A, B, C.
# Определите максимальное количество символов в непрерывной последовательности вида
# A...AB...BC....C, содержащую равное количество букв A, B и C


from re import *

f = open('Задание №3.txt').readline()
reg = r'(?=(A+B+C+))'

mx = []
for stroka in findall(reg, f):
    if stroka.count('A') == stroka.count('B') == stroka.count('C'):
        mx.append(len(stroka))
print(max(mx))