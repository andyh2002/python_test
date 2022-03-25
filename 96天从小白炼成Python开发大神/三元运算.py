# 三元表达式
# 适用场景：变量赋值时存在条件判断，简化代码时使用

# a = 10
# b = 5
# if a > b:
#     max = a
# else:
#     max = b
# print('max:', max)

# # 可简化为：
# max = a if a > b else b
# print('max:', max)

# # 结果 = 值1 if 条件 else 值2
# # 如果条件成立，就取左边的值1，否则取右边的值2


# def Max(a, b):
#     return a if a > b else b


# print(Max(5, 15))

# (值2, 值1)[条件]
# print(("msg:条件为假", "msg:条件为真")[2>1])

def Max(a, b):
    return (b, a)[a > b]


print(max(5, 15))

#{条件值1:结果1, 条件值2:结果2}[判断]
# print({True: "msg2:条件为真", False: "msg2:条件为假"}[2 < 1])

#{条件值1:结果1, 条件值2:结果2}[判断]
# def Max(a, b):
#     return {True: a, False: b}[a > b]


# print(Max(5, 15))
