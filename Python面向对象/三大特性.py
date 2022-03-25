# ！/usr/bin/env python
# _*_ coding: utf-8 _*_
import jedi.debug


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


class Car(object):
    """汽车类"""


car = Car()


class Dog:
    def __init__(self, name, age, sex='雌性'):
        self.name = name
        self.__age = age
        self.sex = sex

    def run(self):
        print("{}在跑...".format(self.name))

    def speak(self, sound):
        print("{}在叫，“{}”！".format(self.name, sound))

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


d1 = Dog('球球', 2)
d2 = Dog('哈哈', 1, '雌性')
d3 = Dog(name='拖布', sex='雌性', age=3)

print('{0}:{1}岁{2}。'.format(d1.name, d1.age, d1.sex))
print('{0}:{1}岁{2}。'.format(d2.name, d2.age, d2.sex))
print('{0}:{1}岁{2}。'.format(d3.name, d3.age, d3.sex))
d1.run()
d2.run()
d2.speak("旺 旺 旺")
