import pygame

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

display = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Змейка")

x1 = 300
y1 = 300

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0

            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0

            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10

            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10

    x1 += x1_change
    y1 += y1_change
    display.fill(white)

    pygame.draw.rect(display, black, [x1, y1, 20, 20])
    pygame.display.update()
    clock.tick(20)

pygame.quit()
quit()
