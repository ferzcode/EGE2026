from re import *

f = open('Задание №5.txt').readline()
reg = r'(?=([1-7][0-7]+[0246]))'

mx = []
for x in findall(reg, f):
    if int(x, 8) == 292320724440304:
        print(f.find(x))
        # mx.append()
# 
# print(min(mx))