# 550

import random

answer = random.randint(1, 10)
guess_limit = 3  # 最大猜测次数
guess_count = 0

while True:
    guess = int(input("我想好了1个1-10之间的数字,你猜是几?"))

    if guess == answer:
        print("你猜对了!OK")
        print("游戏结束!886")
        break  # 跳出循环
    elif guess > answer:
        print("太大了", end=' ')
    else:
        print("太小了", end=' ')

    guess_count += 1
    if guess_count == guess_limit:
        print('你已经用完了猜测次数:' + str(guess_limit))
        print('你失败了! ×')
        break
    else:
        print("请继续猜:")
