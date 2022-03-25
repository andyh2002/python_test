# coding=utf-8

i = input("请输入一个数字：")
n = 8888
try:
    result = n / int(i)
    print(result)
    print("{0}除以{1}等于{2}".format(n, int(i), result))
except ZeroDivisionError as e:
    print("不能除以0，异常：{0}".format(e))
except ValueError as e:
    print("输入的是无效数字，异常：{0}".format(e))
