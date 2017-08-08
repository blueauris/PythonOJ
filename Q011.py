#!python2
#coding: utf-8

##结尾0的个数 
"""
描述:
给你一个正整数列表 L, 如 L=[2,8,3,50], 输出L内所有数字的乘积末尾0的个数,
如样例L的结果为2.(提示:不要直接相乘,数字很多,可能溢出)
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
    
print min(count2,count5)