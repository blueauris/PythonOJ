#!python2
#coding: utf-8

##三角形形状
"""
给以一个三角形的三边长a,b和c(边长是浮点数),请你判断三角形的形状。
若是锐角三角形，输出R,
若是直角三角形，输出Z，
若是钝角三角形，输出D，
若三边长不能构成三角形，输出W.
"""

from random import *
a,b,c=[randint(1, 50) for i in range(3)]
print a,b,c


a,b,c =sorted([a,b,c])
if (a+b <=c) :
	print "W"
elif (a**2 + b**2 < c**2) :
	print "D"
elif (a**2 + b**2 == c**2) :
	print "Z"
else:
	print "R"