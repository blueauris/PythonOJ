#!python2
#coding: utf-8

##最大公约数 
"""
描述:
给你两个正整数a和b， 输出它们的最大公约数。
"""

a,b = (a,b) if (a > b) else(b,a)
while(a%b!=0):
    a,b = b,a%b
print b