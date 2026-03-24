from re import *

f = open('Задание №1.txt').readline()
reg = r'(?=([1-9AB][0-9AB]+))'

mx = []
for x in findall(reg, f):
    mx.append(len(x))
print(max(mx))