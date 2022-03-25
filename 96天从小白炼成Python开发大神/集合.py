# 集合使用{}，但和字典不同，里面不是键值对的形式，每个集合元素使用,分隔。
# 可以存字符串，数字，元组这些不可变元素
a = {'Hello World', 1, 2, 3, (4, 5, 6)}  # 字符串，数字，元组
print(type(a))
print(len(a))
for i in a:
    print(i)
    print(type(i))

a.add((1, 2, 3))
a.add((4, 5, 6))
# 删除存在的元素(1,2,3)
a.discard((1, 2, 3))
# remove不存在的元素
# a.remove(4)

set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set_b = {5, 6, 7, 8, 9, 10, 11, 12, 13}
print('合集-->', set_a | set_b)  # a,b加起来去掉重复部分
print('交集-->', set_a & set_b)  # a,b重复部分
print('差集-->', set_a - set_b)  # a有b没有
print('差集-->', set_b - set_a)  # b有a没有
print('对称差集-->', set_a ^ set_b)  # a,b的合集去掉交集
