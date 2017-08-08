#!python2
#coding: utf-8

##判断三角形 
"""
描述:
给你三个整数a,b,c,  判断能否以它们为三个边长构成三角形。
若能，输出YES，否则输出NO。
算法：
任一边小于三边之和的一半
"""

from random import *
a,b,c=[randint(1, 50) for i in range(3)]
print a,b,c

L=[a,b,c]
dif = filter(lambda x:(sum(L)/2-x)<0, L)
#print dif
if dif ==[]:
	print "YES"
else:
	print "NO"