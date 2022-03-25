age = int(input("请输入你的年龄："))
if age < 12:
    print("You are %d year old! You are a kid!" % age)
    print("You are {} year old! You are a kid!".format(age))
    print("You are {age} year old! You are a kid!".format(age= age))
elif age < 18:
    print("你还未成年吧")
else:
    print("开车!")