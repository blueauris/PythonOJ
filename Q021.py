#!python2
#coding: utf-8

##回文子串
"""
给你一个字符串a和一个正整数n,判断a中是否存在长度为n的回文子串。如果存在，则输出YES，否则输出NO。
回文串的定义：记串str逆序之后的字符串是str1，若str=str1,则称str是回文串，如"abcba".
"""

a = raw_input()
n  =int(input())
print a,n

flag=False
halfN = int(n/2)
len_a = len(a)
if n>=len_a:
    flag = False
for i in range(0,len_a-n+1):
    str1= a[i:i+halfN:1]
    if n%2 == 0:
        str2 =a[i+n-1:i+halfN-1:-1]
    else:
        str2 =a[i+n-1:i+halfN:-1]
    if str1==str2:
        flag = True
        break
if flag :
    print "YES"
else:
    print "NO"
