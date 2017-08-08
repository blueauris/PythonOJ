#!python2
#coding: utf-8

##结尾非零数的奇偶性 
"""
描述:
给你一个正整数列表 L, 如 L=[2,8,3,50], 判断列表内所有数字乘积的最后一个非零数字的奇偶性,
奇数输出1,偶数输出0. 如样例输出应为0
"""

L2=L[::]
count2 = 0
while L2!=[] :
    L2 =[item/2 for item in L2 if (item%2 ==0)]
    count2 +=L2.__len__()

L5=L[::]
count5 = 0
while L5!=[] :
    L5 =[item/5 for item in L5 if (item%5 ==0)]
    count5 +=L5.__len__()
    
result = 1 if count2<=count5 else 0
print result