#!python2
#coding: utf-8

##求解100以内的所有素数 
"""
描述:
输出100以内的所有素数，素数之间以一个空格区分
"""

ll=[2]
for i in range(3,100):
    isPrime=True
    for j in range(2,i/2+1):
        if i%j == 0:
            isPrime=False
            break
    if isPrime==True:
        ll.append(i)
    
stll=[str(i) for i in ll ]
print " ".join(stll)