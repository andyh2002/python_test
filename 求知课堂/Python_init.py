class People:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def eat(self, food):
        print(self.name+'喜欢吃'+food)


zp = People('张鹏', '男生', 18)
print(zp.name, zp.age)
zp.eat("香蕉")

lh = People('李辉', '男生', 28)
print(lh.name, lh.age)
lh.eat("苹果")

xh = People('小花', '女生', 20)
print(xh.name, xh.age)
xh.eat("菠萝蜜")