# 读取用户指令
# input接收的输入都以字符串处理

name = input("输入你的名字:")
age = input("输入你的年龄:")
height = input("输入你的身高:")
question = input("你是不是全身都黑?")

print(name)
print(age)
print(height)
print(question)

# 格式化输出

msg = '''
---------Personal Info--------
Name    : %s
Age     : %s
Height  : %s
Answer  : %s
---------End------------------
''' %(name, age, height, question)

print(msg)

# 对用户输入进行判断
if question == "Y" or question == "y":
	print("我不信，让我看看。。。")

name = ['Alex', 'Golden', 'Oldman']
name.append('Robinson')
name.insert(3,'Kate')
print(name)