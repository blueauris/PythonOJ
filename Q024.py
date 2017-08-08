#!python2
#coding: utf-8

##一马当先
"""
描述:
下过象棋的人都知道，马只能走'日'字形（包括旋转90°的日），现在想象一下，给你一个n行m列网格棋盘，
棋盘的左下角有一匹马，请你计算至少需要几步可以将它移动到棋盘的右上角，若无法走到，则输出-1.
如n=1，m=2,则至少需要1步；若n=1，m=3,则输出-1。
算法1：
广度优先搜索(BFS)
算法2：
所有方向走法的线性组合
"""

m,n=map(int,raw_input().split())

m,n=(n,m) if m<n else(m,n)

horse = [(1,2), (2,1), (-1,2), (-2,1), (1,-2), (2,-1)]
queue = [(0,0)]
goal = {(0,0):0}

def isValid(po):
	return  (0<=po[0]<=m and 0<=po[1]<=n and (not po in goal) )
		
def BFS():
	while queue != [] :
		base=queue.pop(0)
		for item in horse:
			arrow =( (item[0]+base[0]), (item[1]+base[1]) ) 
			if isValid(arrow):
				goal[arrow] = goal[base]+1
				queue.append(arrow)
				if arrow == (m,n):
					break

BFS()
if (m,n) in goal:
	print goal[(m,n)]
else:
	print -1