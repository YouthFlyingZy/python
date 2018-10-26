# coding=utf-8

'''sort()方法使用基础'''
'''
一.基本形式
sorted(iterable[,cmp[,key[,reverse]]]),相当于sorted(iterable, cmp=None, key=None, reverse=False)
iterable.sort(cmp[,key,reverse]]),相当于iterable.sort(self, cmp=None, key=None, reverse=False)
参数解释：
(1)iterable为指定要排序的list或者iterable
(2)cmp为函数,指定排序时进行比较的函数，可以指定一个函数或者lambda函数，如：
	students为类对象的list，每个成员有三个域。用sorted进行比较时可以自己定cmp函数，例如这里要通过
	比较第三个数据成员来排序，代码如下：
	students = [('john','A',15),('jane','B',12)]
	sorted(students,key=lambda student:student[2])
(3)key为函数，指定取待排序元素的哪一项进行排序，函数用上面例子说明，代码如下：
	sorted(students,key=lambda student:student[2])，也可写成sorted(students,key=lambda x:x[2])
	key指定的lambda函数功能是取元素student的第三个域(即student[2])，因此sorted排序时，会以students所
	有元素的第三个域来进行排序，无cmp时默认升序
	
二.普通用法
1.原址排序
列表有自己的sort方法，其对列表进行原址排序，既然是原址排序，那显然元组不可能拥有这种方法，因为元组不可修改
x = [4,6,2,1,7,9]
x.sort() #默认升序
print(x) #[1,2,4,6,7,9]
2.副本排序
(1)[:]分片方法
x = [4,6,2,1,7,9]
y = x[:]
y.sort()
print(y) #[1,2,4,6,7,9]
print(x) #[4,6,2,1,7,9]
注意:y = x[:]通过分片操作将列表x的元素全部拷贝给y，如果简单的把x赋值给y：y = x，y和x还是指向同一个列表，并
	未产生新的副本。
(2)sorted方法
sorted返回一个有序的副本，并且类型总是列表，如下：
x = [4,6,2,1,7,9]
y = sorted(x)
print(y) #[1,2,4,6,7,9]
print(x) #[4,6,2,1,7,9]
print(sorted('PYTHONPython')) #['H', 'N', 'O', 'P', 'P', 'T', 'Y', 'h', 'n', 'o', 't', 'y']

三.高级用法
1.自定义cmp比较函数
def comp(x, y):
	if x < y:
		return 1
	elif x > y:
		return -1
	else:
		return 0
nums = [3,2,8,0,1]
nums.sort(comp)
print(nums) #降序排序：[8,3,2,1,0]
nums.sort(cmp) #调用内建函数cmp,升序排序
print(nums) #升序排序：[0,1,2,3,8]
2.自定义key和reverse
(1)reverse实现降序排序，需要提供一个布尔值，默认为False（升序排序）
(2)key在使用时必须提供一个排序过程总调用的函数
alist = [('2','3','10'),('1','2','3'),('5','6','7'),('2','5','10'),('2','4','10')]
#多级排序，先按照第3个元素排序，然后按照第2个元素排序
print(sorted(alist, cmp=None, key=lambda x:(int(x[2]),int(x[1])), reverse=False)
输出为：[('1','2','3'),('5','6','7'),('2','3','10'),('2','4','10'),('2','5','10')]

四.operator.itemgetter函数
(1)operator模块提供的itemgetter函数用于获取对象的哪些维的数据，参数为一些序号（即需要获取的数据在对象中的序号），
例子如下：
import operator
a = [1,2,3]
b = operator.itemgetter(1) #定义函数b，获取对象的第一个域的值
print(b(a)) #输出为：2
b = operator.itemgetter(1,0) #定义函数b，获取对象的第一个域和第0个域的值
print(b(a)) #输出为:(2,1)
要注意：operator.itemgetter函数获取的不是值，而是定义了一个函数，通过该函数作用到对象才能获取到值
(2)itemgetter在sort的用法
from operator import itemgetter
alist = [('2','3','10'),('1','2','3'),('5','6','7'),('2','5','10'),('2','4','10')]
#多级排序，先按照第3个元素排序，然后按照第2个元素排序
print(sorted(alist, cmp=None, key=itemgetter(2,1), reverse=False))
print(sorted(alist, cmp=None, key=lambda x:itemgetter(2,1)(x), reverse=False))
print(sorted(alist, cmp=None, key=lambda x:map(int, itemgetter(2,1)(x)), reverse=False))
要注意：字符串的比较看首字母，比如'10'<'3','4'>'310'，
print(map(int, ('1','2'))) #输出为：[1,2]，对每个参数使用int函数
	












'''

