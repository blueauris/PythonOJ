#!python2
#coding: utf-8

##相同数字 
"""
描述:
给你一个整数列表L,判断L中是否存在相同的数字，
若存在，输出YES，否则输出NO。
"""

from random import *
n=randint(1, 20)
L=[randint(0, 50) for i in range(n)]
print L

L.sort()
sign = False
for i in range(len(L)-1):
	if L[i]==L[i+1]:
		sign = True
		break

if sign:
	print "YES"
else:
	print "NO"