# coding=utf-8

class Horse:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        return "马的名字：{0}".format(self.name)

    def run(self):
        print("马跑...")


class Donkey:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        return "驴的名字：{0}".format(self.name)

    def run(self):
        print("驴跑...")

    def roll(self):
        print("驴打滚...")


class Mule(Horse, Donkey):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age


    def show_info(self):  # 重写父类方法show_info()
        return "骡：{0}，{1}岁".format(self.name, self.age)


m = Mule("骡宝莉", 1)
print(Mule.__mro__)  # 父类顺序
m.run()  # 继承父类Horse的方法
m.roll()  # 继承父类Donkey的方法
print(m.show_info())  # 子类Mule自己的方法
