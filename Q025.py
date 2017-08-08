#!python2
#coding: utf-8

##格式化时间 
"""
描述:
给你一个时间t（t是一个字典，共有六个字符串key(year,month,day,hour,minute,second),值为每个值为数字组成的字符串，
如t={'year':'2013','month':'9','day':'30','hour':'16','minute':'45','second':'2'}
请将其按照以下格式输出， 格式:XXXX-XX-XX XX:XX:XX。如上例应该输出： 2013-09-30 16:45:02。
"""

t={'year':'2013','month':'9','day':'30','hour':'16','minute':'45','second':'2'}

tar_ll = [t['year'], t['month'],t['day'],t['hour'],t['minute'],t['second']]
tar = map(int,tar_ll)
print "%4d-%02d-%02d %02d:%02d:%02d"%(tar[0], tar[1], tar[2], tar[3], tar[4], tar[5])