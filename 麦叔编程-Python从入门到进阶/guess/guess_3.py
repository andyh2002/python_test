# 550

import random
import sys
import time  # 时间模块

print(sys.argv)

guess_limit = int(sys.argv[1])  # 获取参数，最多猜测次数
scores = []  # 保存战绩

cycle = 0  # 第几轮
while True:
    cycle += 1
    answer = random.randint(1, 10)
    is_right = False
    begin_time = time.time()  # 开始时间

    for i in range(guess_limit):
        guess = int(input("我想好了1个1-10之间的数字,你猜是几?"))
        if guess == answer:
            is_right = True
            break  # 跳出循环
        elif guess > answer:
            print("太大了", end=' ')
        else:
            print("太小了", end=' ')
            
        if i < guess_limit-1:
            print("请继续猜：")

    if is_right:
        print("你猜对了!OK")
    else:
        print('你已经用完了猜测次数，你失败了')
    end_time = time.time()
    used_time = end_time - begin_time
    used_time = round(used_time, 2)
    print(f'共用时{int(used_time)}秒')

    # 保存战绩
    scores.append((cycle, is_right, used_time))
    print('==========战绩==========')
    for _cycle, _is_right, _used_time in scores:
        label = 'OK' if (_is_right) else '×'
        print(f'第{_cycle}轮，{label}，{_used_time}')
    print('========================')

    con = input("要继续玩，输入y，否者直接回车：")
    if con != 'y':
        print('886...')
        break
