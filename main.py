import pygame
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 102)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 800
dis_heigth = 600
display = pygame.display.set_mode((dis_width, dis_heigth))
pygame.display.set_caption("Змейка")

snake_block = 10
clock = pygame.time.Clock()
snake_speed = 15
font_style = pygame.font.SysFont("bahnschrift", 20)
score_font = pygame.font.SysFont("comicsansms", 25)


def your_score(score):
    value = score_font.render(f"Ваш счет {score}", True, yellow)
    display.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [dis_width / 10, dis_heigth / 3])


def game_loop():
    game_over = False
    game_close = False
    x1 = dis_width / 2
    y1 = dis_heigth / 2
    x1_change = 0
    y1_change = 0
    snake_list = []
    length_of_snake = 1
    direction = "right"
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

                if event.type == pygame.QUIT:
                    game_close = False
                    game_over = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and direction != "right":
                    x1_change = -snake_block
                    y1_change = 0
                    direction = "left"

                elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and direction != "left":
                    x1_change = snake_block
                    y1_change = 0
                    direction = "right"

                elif (event.key == pygame.K_UP or event.key == pygame.K_w) and direction != "down":
                    x1_change = 0
                    y1_change = -snake_block
                    direction = "up"

                elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and direction != "up":
                    x1_change = 0
                    y1_change = snake_block
                    direction = "down"

        if x1 > dis_width:
            x1 = 0
        if x1 < 0:
            x1 = dis_width
        if y1 > dis_heigth:
            y1 = 0
        if y1 < 0:
            y1 = dis_heigth

        x1 += x1_change
        y1 += y1_change
        display.fill(blue)
        pygame.draw.rect(display, red, [food_x, food_y, snake_block, snake_block])
        snake_head = []

        snake_head.append(x1)
        snake_head.append(y1)

        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
        your_score(length_of_snake - 1)
        our_snake(snake_block, snake_list)
        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, dis_heigth - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


game_loop()
