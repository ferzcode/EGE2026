from re import *

f = open('Задание №5.txt').readline()
reg = r'(?=([1-9AB][0-9AB]+[13579B]))'

mx = []
for x in findall(reg, f):
    if int(x, 12) == 3558961523338354573045986547427776444266153397058824906178188563457873887001623058615078644414008156181729915515425115:
        print(f.find(x))
    # mx.append(int(x, 12))
# print(max(mx))
