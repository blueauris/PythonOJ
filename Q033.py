#!python2
#coding: utf-8

##大幂次运算 
"""
描述:
给你两个正整数a(0 < a < 10 0000)和n(0 <= n <=1000 0000 0000)，计算(a^n) % 20132013并输出结果
"""
"""
算法：快速幂并取模
快速幂：记指数b为二进制形式 各位分别为 Bn B(n-1) B(n-2) ……B2 B1 B0
则 a^b = [(a^1)^B0] [(a^2)^B1] [(a^4)^B2]……[(a^(2^(n-1)))^B(n-1)][(a^(2^n))^Bn]
取模：有数论公式，积的取余等于取余的积的取余
则  a^b = [(a^1 mod c)^B0] * [(a^2 mod c)^B1] * [(a^4  mod c)^B2]…… * [(a^(2^(n-1))  mod c)^B(n-1)] * [(a^(2^n) mod c)^Bn]  mod c

另 按数论公式
1.如果b是偶数，记 k = a^2 mod c，则 a^b mod c = (k)^(b/2) mod c
2.如果b是奇数，记 k = a^2 mod c，则 a^b mod c =( (k)^(b/2) mod c * a) mod c 
将上式迭代 亦可得快速幂取模算法
"""

a = 15
n = 30

def powMod(x, y, z):
	result = 1
	X2 = x  # x的2^n次幂
	while( y > 0):
		result  = (result * X2 % z) if ( y % 2 == 1) else result
		X2 = X2*X2 %z
		y = y / 2
	return result

print powMod(a, n, 20132013)