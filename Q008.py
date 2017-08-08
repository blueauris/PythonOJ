#!python2
#coding: utf-8

##求中位数 
"""
描述:
给你一个list L, 如 L=[0,1,2,3,4], 输出L的中位数（若结果为小数，则保留一位小数）。
"""

L.sort()
length = len(L)
if length%2 == 0:
    print (L[length/2]+L[length/2-1])/2.0
else:
    print L[length/2]