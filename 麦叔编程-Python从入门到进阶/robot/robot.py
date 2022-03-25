#! /usr/bin/env python
# coding = utf-8
# 引入另外一个文件/模块/module import
import opening
import order
# from datetime import datetime
import time
# 1. 出场
opening.show_robot()
time.sleep(1)

# 2. 了解主人,问问题
name = opening.ask()
#
# # 3. 问好
# opening.hello(name)

# 4. 显示时间
# dt = datetime.now()
# print(f'今天是:{dt.year}年{dt.month}月{dt.day}日 {dt.hour}:{dt.minute}')
# print(dt.strftime("今天是:%Y年%m月%d日 %H:%M:%S"))

while True:
    print("-----------------")
    print("小麦:您有什么吩咐?")
    cmd = input()
    if cmd == "time":
        order.show_time()
    elif cmd == "hello":
        opening.hello(name)
    elif cmd == "88":
        print("小麦:88,有需要再找我!")
        break
    elif cmd == "tianqi":
        city = input("你想查询那个城市的天气:")
        order.tianqi(city)
    else:
        print(order.ai_talk(cmd))
