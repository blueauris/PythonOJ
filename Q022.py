#!python2
#coding: utf-8

##时间就是金钱
"""
给你两个时间st和et(00:00:00<=st <= et<=23:59:59), 请你给出这两个时间间隔的秒数。
如：st="00:00:00", et="00:00:10", 则输出10.
"""

st = raw_input()
et = raw_input()

stl= st.split(':')
etl= et.split(':')

time =3600*(int(etl[0])-int(stl[0])) +60*(int(etl[1])-int(stl[1]))+(int(etl[2])-int(stl[2]))
print time