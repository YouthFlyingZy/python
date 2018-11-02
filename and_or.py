# coding=utf-8

"""
@author: zhongy
@date: 2018/11/2
@desc:
"""

'''and...or...的用法，类似于Lua，但又不完全相同'''

# 即a and b，当a为真时(非0，False，None)，返回b，当a为0，False，None时，返回a，与Lua中完全相同
print('a and b')
print(1 and 2)  # 输出：2
print(0 and 2)  # 输出：0
print(False and 2)  # 输出：False
print(None and 2)  # 输出：None

# 即a or b，当a为真时(非0，False，None)，返回a，当a为0，False，None时，，与Lua中完全相同
print('a or b')
print(1 or 2)  # 输出：1
print(0 or 2)  # 输出：2
print(False or 2)  # 输出：2
print(None or 2)  # 输出：2

# 即在a不为0，False，None情况下：bool and a or b，当bool为真时，返回a，当bool为0，False，None时，返回b，与Lua中完全相同
print('bool and a or b')
print(True and 1 or 2)  # 输出：1
print(0 and 1 or 2)  # 输出：2
print(False and 1 or 2)  # 输出：2
print(None and 1 or 2)  # 输出：2
# 重点注意：在a为0，False，None情况下：bool and a or b，不管bool为何值，都返回b，与Lua中就不一样了，得不到上述情况的结果
print('bool and 0/False/None or b')
print(True and 0 or 2)  # 输出：2
print(True and False or 2)  # 输出：2
print(True and None or 2)  # 输出：2
# 为了避免上述情况出现，可以写成：(bool and [a] or [b])[0]，此时[a]是一个非空列表，绝不会为假，然后返回列表的第一个元素
print('(bool and [a] or [b])[0]')
print(True and [0] or [2])[0]
print(True and [False] or [2])[0]
print(True and [None] or [2])[0]
print(0 and [0] or [2])[0]
print(False and [False] or [2])[0]
print(None and [None] or [2])[0]



