#!python2
#coding: utf-8

##人民币金额打印 
"""
描述:
注明：数据已于2013-11-19日加强，原来通过的代码可能不能再次通过。
注意：由于中文乱码问题，输出时请先decode("utf8")，例如你要输出ans = "零圆", print ans.decode("utf8").
银行在打印票据的时候，常常需要将阿拉伯数字表示的人民币金额转换为大写表示，现在请你来完成这样一个程序。
在中文大写方式中，0到10以及100、1000、10000被依次表示为：
    零壹贰叁肆伍陆柒捌玖拾佰仟万
以下的例子示范了阿拉伯数字到人民币大写的转换规则：

1	壹圆
11	壹拾壹圆
111	壹佰壹拾壹圆
101	壹佰零壹圆
-1000	负壹仟圆
1234567	壹佰贰拾叁万肆仟伍佰陆拾柒圆

现在给你一个整数a(|a|<100000000), 打印出人民币大写表示
"""

a = int(input())

def trans(num):
##将四位数转换为中文
	digs= {1:u'壹',2:u'贰',3:u'叁',4:u'肆',5:u'伍',6:u'陆',7:u'柒',8:u'捌',9:u'玖'}
	n1 = num%10
	n2 = num%100//10
	n3 = num%1000//100
	n4 = num//1000

	cnstr4 = (digs[n4] + u'仟') if n4!=0 else ""
	cnstr3 = (digs[n3] + u'佰') if n3!=0 else (u'零' if ( n4!=0 and (n2!=0 or n1!=0))else "")
	cnstr2 = (digs[n2] + u'拾') if n2!=0 else (u'零' if ((n4!=0 or n3!=0) and n1!=0) else "")
	cnstr1 = digs[n1] if n1!=0 else ""

	if cnstr3 ==u"零"  and cnstr2 ==u"零":
		cnstr2 =''

	cnstr = cnstr4 + cnstr3  + cnstr2 + cnstr1

	return cnstr

if a<0:
	a= -1*a
	str_all = u'负'
else:
	str_all =''

a_up = a//10000
a_down = a%10000

str_up = trans(a_up)
str_down = trans(a_down)


if a_up == 0 and a_down == 0:
	str_all += u'零'+u'圆'
elif a_up == 0 and a_down != 0:
	str_all += str_down + u'圆'
elif a_up != 0 and a_down != 0 and a_down <1000 :
	str_all += str_up + u'万' + u'零' +str_down + u'圆'
else:
	str_all += str_up + u'万' +str_down + u'圆'

print(str_all)