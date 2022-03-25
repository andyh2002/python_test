#! /usr/bin/env python
count = 1
red_list = []
while count < 7:
    n = int(input("请选择第{number}个红球的编号：1 <= n <= 33:".format(number=count)))
    if n < 1 or n > 33:
        print("您选择的编号超出范围")
    elif n in red_list:
        print("编号为{number}的红球已存在".format(number=n))
    else:
        red_list.append(n)
        count += 1
red_list.sort()
print(red_list)
