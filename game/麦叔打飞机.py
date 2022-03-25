import pygame
import sys
import random
import math

# 1.初始化界面
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("麦叔打飞机")
icon = pygame.image.load("image/ufo.png")
pygame.display.set_icon(icon)
bgImg = pygame.image.load("image/space.jpg")
f_clock = pygame.time.Clock()
fps = 60
f_clock.tick(fps)
# 飞机
playerImg = pygame.image.load("image/space-shuttle-2_small.png")
playerX = 360
playerY = 520
playerStep = 0

# 敌人类
number_of_enemies = 6  # 敌人数量


class Enemy:
    def __init__(self):
        self.img = pygame.image.load("image/ufo_small.png")
        self.x = random.randint(200, 600)
        self.y = random.randint(50, 250)
        self.step = random.randint(1, 1)  # 移动敌人的速度，如何与fps关联？

    def reset(self):  # 重新初始化位置
        self.x = random.randint(200, 600)
        self.y = random.randint(50, 250)
        print('重新初始化！')


# 列表保存敌人
enemies = []
for i in range(number_of_enemies):
    enemies.append(Enemy())


def distance(bx, by, ex, ey):
    """
    :param bx:一个点的x坐标
    :param by:一个点的y坐标
    :param ex:另一个点的x坐标
    :param ey:另一个点的y坐标
    :return: 两个点之间的距离
    """
    a = bx - ex
    b = by - ey
    return math.sqrt(a * a + b * b)


class Bullet:
    """
    子弹类
    """

    def __init__(self):
        self.img = pygame.image.load('image/bullet.png')
        self.x = playerX + 22
        self.y = playerY - 20
        self.step = 1  # 子弹移动的速度

    # 击中判断
    def hit(self):
        for e in enemies:
            if distance(self.x, self.y, e.x, e.y) < 30:
                print(e, "被击中了！")
                bullets.remove(self)
                e.reset()


bullets = []  # 保存现有的子弹


# 显示子弹
def show_bullet():
    for b in bullets:
        screen.blit(b.img, (b.x, b.y))
        b.hit()  # 看看是否击中了敌人
        b.y -= b.step  # 移动子弹
        # 判断子弹是否出了界面
        if b.y < 0:
            bullets.remove(b)


# 显示敌人
def show_enemy():
    for e in enemies:
        screen.blit(e.img, (e.x, e.y))
        e.x += e.step
        if e.x > 736 or e.x < 0:
            e.step *= -1
            e.y += 10


# 移动玩家
def move_player():
    global playerX  # 全局变量
    playerX += playerStep
    # 防止飞机出界
    if playerX > 736:
        playerX = 736
    if playerX < 0:
        playerX = 0


# 2.游戏主循环


while True:
    screen.blit(bgImg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 游戏界面关闭
            pygame.quit()
            sys.exit()
        # 通过键盘事件来控制飞机的移动
        if event.type == pygame.KEYDOWN:  # 按下移动
            if event.key == pygame.K_RIGHT:
                playerStep = 1
            elif event.key == pygame.K_LEFT:
                playerStep = -1
            elif event.key == pygame.K_SPACE:
                print('发射子弹....')
                # 创建一颗子弹
                bullets.append(Bullet())
        if event.type == pygame.KEYUP:  # 抬起不动
            playerStep = 0

    screen.blit(playerImg, (playerX, playerY))
    move_player()
    show_enemy()
    show_bullet()  # 显示子弹
    pygame.display.update()
