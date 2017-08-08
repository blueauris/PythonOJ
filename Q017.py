#!python2
#coding: utf-8

##公约数的个数 
"""
描述:
给你两个正整数a,b,  输出它们公约数的个数。
"""

a = int(input())
b = int(input())

if a<b:
    a,b =b,a

while(a%b)!=0:
    a,b = b,a%b
gcd = b

sum = 0
for i in range(1,gcd+1):
    if a%i==0 and b%i==0 :
        sum+=1
print(sum)