#!python2
#coding: utf-8

##序列判断 
"""
描述:
给你一个整数组成的列表L，按照下列条件输出：
若L是升序排列的,则输出"UP";
若L是降序排列的,则输出"DOWN";
若L无序，则输出"WRONG"。
"""

import random
L=[random.randint(0, 100) for i in range(10)]
#L.sort()
#L.sort(None,None,True)
#print L

signUp= True
signDown = True

for i in range( len(L)-1):
	if L[i] > L[i+1]:
		signUp = False
	if L[i] < L[i+1]:
		signDown = False

if signUp:
	print "UP"
elif signDown:
	print "DOWN"
else:
	print "WRONG"
