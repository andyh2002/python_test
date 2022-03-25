import sys

import pygame

pygame.init()
pygame.display.set_caption("贪吃蛇")  # 窗口标题
screen = pygame.display.set_mode([400, 500])
clock = pygame.time.Clock()
test_surface = pygame.Surface((100, 200))
test_surface.fill((0, 0, 255))  # 填充RGB颜色
test_rect = test_surface.get_rect(topright=(200, 250))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((175, 215, 70))
    test_rect.right += 1  # 向右移动
    screen.blit(test_surface, test_rect)
    pygame.display.update()
    clock.tick(60)  # 每秒60帧
