import random
import pygame
import time

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

dis_width = 800
dis_heigth = 600
display = pygame.display.set_mode((dis_width, dis_heigth))
pygame.display.set_caption("Змейка")

snake_block = 10



clock = pygame.time.Clock()
snake_speed = 15
font_style = pygame.font.SysFont(None, 50)


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [50, dis_heigth / 2])


def game_loop():
    game_over = False
    game_close = False
    x1 = dis_width/2
    y1 = dis_heigth/2
    x1_change = 0
    y1_change = 0
    food_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, dis_heigth - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close == True:
            display.fill(white)
            message('Вы проиграли, нажмите Q для выхода или R для повторной игры', red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0

                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0

                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block

                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

        if x1 >= dis_width or x1 <= 0 or y1 >= dis_heigth or y1 <= 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        display.fill(white)

        pygame.draw.rect(display, red, [food_x, food_y, snake_block, snake_block])
        pygame.draw.rect(display, black, [x1, y1, snake_block, snake_block])
        pygame.display.update()
        clock.tick(snake_speed)

    pygame.display.update()
    time.sleep(2)
    pygame.quit()

    quit()

game_loop()
