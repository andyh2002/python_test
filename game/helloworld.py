import sys

import pygame

pygame.init()

screen = pygame.display.set_mode([500, 600])
pygame.display.set_caption("Hello, World!")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
