#!python2
#coding: utf-8

##信息加密
"""
给你个小写英文字符串a和一个非负数b(0<=b<26), 将a中的每个小写字符替换成字母表中比它大b的字母。
这里将字母表的z和a相连，如果超过了z就回到了a。例如a="cagy",b=3, 则输出 fdjb
"""

a= raw_input()
b = int(raw_input())

def tranchar(chr_in):
    if 'a'<=chr_in<='z':
        chr_out = chr( (ord(chr_in)+b-97)%26+97)
    else:
        chr_out = chr_in
    return chr_out

aa=[tranchar(i) for i in a]
bb="".join(aa)
print bb
