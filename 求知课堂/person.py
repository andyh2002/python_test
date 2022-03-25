# 定义类和对象
# 类的结构 类名 属性 方法
# class 类名：
#       属性
#       方法


class Person:  # 类名采用大驼峰方式命名
    # name = ""
    age = 0

    def __init__(self):
        self.name = "小明"

    def eat(self):
        # 吃饭
        print("大口大口的吃饭！")
        pass

    def run(self):
        print("飞快的跑！")


# 对象名 = 类名()  创建对象
xiaoming = Person()
xiaoming.eat()
xiaoming.run()
print("{}的年龄是:{}".format(xiaoming.name, xiaoming.age))

xiaozhang = Person()
xiaoming.age = 18
xiaozhang.name = "小张"
print(xiaozhang.age)
print(xiaozhang.name)
