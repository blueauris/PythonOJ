#!python2
#coding: utf-8

##365 Or 366？
"""
一年有多少天，这是个大问题，很值得思考。现在给你一个年份year(year为四位数字的字符串，如"2008","0012"),
你输出这一年的天数。如year="2013", 则输出365。
"""

year = int(raw_input())

days = 365
if (year%4 ==0 and year%100 !=0) or year%400 ==0:
    days = 366

print days