#! /usr/bin/env python


# def calc(x, y):
#     """定义一个函数，返回x的y次幂
#     """
#     return x**y


# print('显示函数调用:', calc(2, 5))

# # 匿名函数形式

# # 匿名函数赋值给一个变量（非推荐模式）


# def c(x, y): return x**y  # 冒号前面是参数，后面是表达式


# print('匿名函数变量调用:', c(2, 5))

# # 可以直接调用匿名韩式
# print('匿名函数直接调用:', (lambda x, y: x**y)(2, 5))

# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
# 遍历序列，对序列中每个元素进行函数操作，最终获取新的序列
# li = [1, 3, 5, 7, 9]
# print(list(map(lambda x: x*x, li)))  # 将map操作后产生的Iterator转成list

# reduce函数
# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，
# 其效果就是：reduce(func,[1,2,3]) 等同于 func(func(1,2),3)，对于序列内所有元素进行累计操作
# from functools import reduce
# li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(reduce(lambda x, y: x * y, li))   # 1*2*3*4*5*6*7*8*9

# # filter 函数
# # filter过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表
# for i in filter(lambda x: x > 10, [1, 2, 10, 100, 20, 35]):
#     print(i, end=' ')

# sorted函数
# sorted 可以对所有可迭代的对象进行排序操作，返回一个新的对象
students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
# 按年龄排序，通过lambda取列表中每个元素(元组)的第3个资元素
students_sorted_by_age = sorted(students, key=lambda s: s[2])
print(students_sorted_by_age)
# 按姓名降序排列
students_sorted_by_name = sorted(students, key=lambda s: s[0], reverse=True)
print(students_sorted_by_name)
