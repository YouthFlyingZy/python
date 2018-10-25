# coding=utf-8

'''关于各种反转'''

#1.字符串反转
a='12345'
print(a[::-1]) #321
print(list(reversed(a))) #['5','4','3','2','1']

#2.列表反转
b=[1,2,3,4,5]
print(b[::-1]) #[5,4,3,2,1]
print(list(reversed(b))) #[5,4,3,2,1]

#3.元组反转
c=('R','u','n','o','o','b')
print(c[::-1]) #('b', 'o', 'o', 'n', 'u', 'R')
print(list(reversed(c))) #['b', 'o', 'o', 'n', 'u', 'R']

