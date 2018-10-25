# coding=utf-8

#链式比较
b=6
print(4 < b < 7) #相当于print(4 < b and b < 7),输出True

#链式函数
def mul(a, b):
	return a*b

def add(a, b):
	return a+b
	
flag = True
print((mul if flag else add)(5, 7)) #输出35
