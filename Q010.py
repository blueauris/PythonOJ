#!python2
#coding: utf-8

##最小公倍数 
"""
描述:
给你两个正整数a和b， 输出它们的最小公倍数
"""

a1,b1 = (a,b) if (a > b) else(b,a)
c= a1%b1
while(a1%b1!=0):
    a1,b1 = b1,a1%b1
print a*b/b1