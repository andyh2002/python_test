#! /usr/bin/env python
def register(name, age, country='中国'):  # 不带country参数时默认为"中国"
    msg = '''
-------注册信息-------
    name:{name}
    __age:{age}
    country:{country}
----------------------'''.format(name=name, age=age, country=country)
    return msg


print(register('张三', 18))  # 不带country参数时默认为"中国"
print(register('浩二', 20, '日本'))
