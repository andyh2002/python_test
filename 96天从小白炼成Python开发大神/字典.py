# 字典学习
# 1.key-value结构
# 2.key必须为不可变数据类型、必须唯一
# 3.可存放任意多个value、可修改、可以不唯一
# 4.无序
# 5.查询速度快，且不受dict的大小影响
# 创建
# person = {'name':'张三', '__age':20}  # 2和key保存姓名和年龄
# print(person)
# 增加key
# person['address'] = '北京市海淀区西土城路10号'
# print('增加address:', person)
# # 修改value
# person['__age'] = 26
# print('修改age:', person)
# #删除key
# person.pop('address')
# print("删除address:",person)
# person.popitem() #随意删除
# print('删除一个key:',person)
# person.clear() #清空dict
# print('清空dict:',person)
# person = {'name':'张三', '__age':20, 'address':'北京市海淀区西土城路10号'}
# # 通过key 循环取value值
# for key in person:
#     print(key, ":", person[key])
# # 或者第二种
# for key in person.keys():
#     print(key, ":", person[key])
# # key,value在dict.item()中，同时取出来
# for key, value in person.items():
#     print(key, ":", value)
# 请把这个dict中key大于5的值value打印出来
a = {'k0': 0, 'k1': 1, 'k2': 2, 'k3': 3, 'k4': 4,
     'k5': 5, 'k6': 6, 'k7': 7, 'k8': 8, 'k9': 9}
print(a)
for key in a:
    if key > 'k5':
        print(a[key])
# value是偶数的统一改成-1
for key in a:
    if a[key] % 2 == 0:
        a[key] = -1
print(a)
