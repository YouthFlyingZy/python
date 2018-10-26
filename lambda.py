# coding=utf-8

'''python中的lambda函数用法:
匿名函数lambda：是指一类无需定义标识符（函数名）的函数或子程序。lambda函数
				可以接收任意多个参数（包括可选参数）并且返回单个表达式的值
要点：1.lambda函数不能包含命令 2.包含的表达式不能超过一个
'''
#1.传入多个参数的lambda函数
def sum(x,y):
	return x+y
#用lambda函数来实现
p = lambda x,y:x+y
print(sum(4,6))
print(p(4,6))

#2.传入一个参数的lambda函数
a = lambda x:x*x
print(a(3))
#注意：这里的直接a(3)可以执行，但是没有输出的，前面的print不可少

#3.多个参数的lambda形式
b = lambda x,y,z:(x+8)*y-z
print(b(5,6,8))

'''
补充说明：
一定非要使用lambda函数；任何能够使用它们的地方，都可以定义一个单独的普通函数来进行替换。
						我将它们用在需要封装特殊的，非重用代码是，避免令我的代码充斥着
						大量单行函数。
'''

d = lambda x:x*x
print(d)	#输出为：<function <lambda> at 0x0000000002093E18>	
print(d(3))	#输出为：9



