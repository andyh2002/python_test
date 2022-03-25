import random

n = random.randint(0, 10)

count = 0
while count < 5:
    user_guess = int(input("Input your guess number："))

    if user_guess > n:
        print("try smaller...")
    elif user_guess < n:
        print("try bigger...")
    else:
        print("bingo, you got it...")
        break  # 猜对了退出循环

    count += 1

print(n)
