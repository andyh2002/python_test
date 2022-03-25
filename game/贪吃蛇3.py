import sys, pygame, random
from pygame.math import Vector2


class FRUIT:
    def __init__(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)
        # create an x and y position
        # draw a square

    def draw_fruit(self):
        # create a rectangle
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, (126, 166, 114), fruit_rect)


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1, 0)

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, (183, 191, 122), block_rect)

    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]


pygame.init()
cell_size = 40
cell_number = 20
pygame.display.set_caption("贪吃蛇")  # 窗口标题
screen = pygame.display.set_mode([cell_number * cell_size, cell_number * cell_size])
clock = pygame.time.Clock()

fruit = FRUIT()
snake = SNAKE()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)   # 创建计时器，150毫秒触发一次

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            snake.move_snake()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction = Vector2(0,-1)

    screen.fill((175, 215, 70))
    fruit.draw_fruit()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(60)  # 每秒60帧
