#!python2
#coding: utf-8

##逆解最大公约数与最小公倍数

"""
我们经常遇到的问题是给你两个数，要你求最大公约数和最小公倍数。
今天我们反其道而行之，给你两个数a和b，计算出它们分别是哪两个数的最大公约数和最小公倍数。
输出这两个数，小的在前，大的在后，以空格隔开。若有多组解，输出它们之和最小的那组。
注：所给数据都有解，不用考虑无解的情况。

算法：就是求b/a的两个互质且和最小的因数
"""

a = int(input())
b = int(input())

import math
def gcd(p,q):
    p,q = (p,q) if (p > q) else(p,q)
    while(p%q!=0):
        p,q = q,p%q
    return q

a,b = (a,b) if a<b else (b,a)
diff=b/a
uper = int(math.sqrt(diff)) +1
XYList=[(i,diff/i) for i in range(uper, 0,-1) if diff%i ==0] #求所有因数
XYList =[i for i in XYList if gcd(i[0],i[1])==1]#去除非互质项
XYList.sort(cmp = lambda it1,it2:(it1[0]+it1[1])<(it2[0]+it2[1]) ) #排序，使第一项和最小
x,y=XYList[0]
x,y = (x*a,y*a) if x<y else(y*a,x*a)
print x,y



