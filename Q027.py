#!python2
#coding: utf-8

##加油站 
"""
描述：
一个环形的公路上有n个加油站，编号为0,1,2,...n-1,
每个加油站加油都有一个上限，保存在列表limit中，即limit[i]为第i个加油站加油的上限，
而从第i个加油站开车开到第(i+1)%n个加油站需要cost[i]升油,cost为一个列表。
现在有一辆开始时没有油的车，要从一个加油站出发绕这个公路跑一圈回到起点。
给你整数n，列表limit和列表cost,你来判断能否完成任务。
如果能够完成任务，输出起始的加油站编号，如果有多个,输出编号最小的。
如果不能完成任务，输出-1。
算法：
车无加油上限，故可应用分年现金流量模型。、
limit即为年收入，cost即为年支出，所求即为验证各年盈余累计是否为正值
环形道路，为计算方便，可将0～n-1节点的数据复制到n~2n-1节点
"""

from random import *
n=randint(1, 20)
limit=[randint(0, 50) for i in range(n)]
cost=[randint(0, 30) for i in range(n)]
print "n=",n
print "limit=",limit
print "cost=",cost


rest=[limit[i]-cost[i] for i in range(n)]

if sum(rest) <0:
	print -1
	quit()

rest = rest[:]+rest[:]

for i in range(n):
	sign = True
	total = 0
	for j in range(n):
		total += rest[i+j]
		if total < 0:
			sign = False
			break
	if sign == True:
		pos = i
		break

if sign == True:
	print pos
else:
	print -1