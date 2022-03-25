robot_name = '小麦'


def show_robot():
    # 机器人ICON
    print("""      \\_/
     (* *)
    __)#(__
   ( )...( )(_)
   || |_| ||//
>==() | | ()/
    _(___)_
   [-]小麦[-]
    """)


def ask():
    # 定义变量
    name = input("我是小麦,你叫什么名字?\n")
    age = input("我8岁了,你呢?\n")  # 字符串

    # 类型转换
    # 字符串转数字
    age = int(age)
    # 判断
    # 如果age大于30:我喜欢成熟的人,很有魅力
    # 如果age小于30:你真年轻,如花似玉的年龄
    if age < 30:
        print(f"你才{age}啊!!!")
        print(f"你真年轻,如花似玉的年龄")
    elif age < 50:
        print(f"{age}岁像一座沉稳的大山!!!")
    else:
        print(f"我喜欢成熟的人,很有魅力")

    return name  # 返回获取到的名称


def hello(name):
    # 字符拼接,如是其他数据类型会报错
    # print('---------------------')
    # print("你好," + name + ',我是' + robot_name)
    # print("天地之间," + name + "最帅!")
    # print("我对" + name + "的敬仰之情,犹如黄河之水一发而不可收拾!")
    # print("帅归帅," + name + "千万别忘了戴口罩!")
    # # 使用format
    # print('---------------------')
    # print('你好,{},我是{}'.format(name, robot_name))  # 使用format带参数替换
    # print('天地之间,{}最帅!'.format(name))
    # print("我对{}的敬仰之情,犹如黄河之水一发而不可收拾!".format(name))
    # print("帅归帅,{}千万别忘了戴口罩!".format(name))
    # 字符串前面要加一个f
    print('---------------------')
    print(f'你好,{name},我是{robot_name}')
    print(f'天地之间,{name}最帅!')
    print(f"我对{name}的敬仰之情,犹如黄河之水一发而不可收拾!")
    print(f"帅归帅,{name}千万别忘了戴口罩!")
