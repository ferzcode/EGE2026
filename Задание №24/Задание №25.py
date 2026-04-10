from re import *


f = open('Задание №1.txt').readline()
mx = 0

# BCA ...BCA...BCA...BCA...BCA...BCA...BCA...BCA
reg = r'BCA(?:[1-9]BCA)*'
for combo in findall(reg, f):
    # print(combo)
    mx = max(len(combo), mx)
print(mx)

