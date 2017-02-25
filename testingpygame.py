import pygame
import random

pygame.init()

SCREEN_SIZE = (800, 600)
SKY_BLUE = (135, 206, 235)
BLACK = (0, 0, 0)

carImg = pygame.image.load('racecar.png')
car_height = carImg.get_rect().size[0]
car_width = carImg.get_rect().size[1]
pygame.transform.scale(carImg, (car_width + 1000, car_height + 100))

gameDisplay = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Game')

pygame.display.update()

gameExit = False

x = 400
y = 400

keysDown = []


def draw_obstacle(x, y, width, height):
    pygame.draw.rect(gameDisplay, BLACK, [x, y, width, height])


def draw_car(x, y):
    gameDisplay.blit(carImg, (x, y))


obstacle_y = random.randrange(0, 800)
obstacle_x = 0
obstacle_speed = 4

print(carImg.get_rect().size)

while not gameExit:
    for event in pygame.event.get():
        print(event)

        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                keysDown.append(pygame.K_LEFT)
            if event.key == pygame.K_RIGHT:
                keysDown.append(pygame.K_RIGHT)
            if event.key == pygame.K_DOWN:
                keysDown.append(pygame.K_DOWN)
            if event.key == pygame.K_UP:
                keysDown.append(pygame.K_UP)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keysDown.remove(pygame.K_LEFT)
            if event.key == pygame.K_RIGHT:
                keysDown.remove(pygame.K_RIGHT)
            if event.key == pygame.K_DOWN:
                keysDown.remove(pygame.K_DOWN)
            if event.key == pygame.K_UP:
                keysDown.remove(pygame.K_UP)

    if pygame.K_RIGHT in keysDown:
        x += 1
    if pygame.K_LEFT in keysDown:
        x -= 1
    if pygame.K_UP in keysDown:
        y -= 1
    if pygame.K_DOWN in keysDown:
        y += 1

    print(keysDown)

    gameDisplay.fill(SKY_BLUE)
    if x > 800:
        x = 0
    elif x <= 0:
        x = 800

    if y > 600:
        y = 0
    elif y <= 0:
        y = 600

    obstacle_x += obstacle_speed - 2

    if obstacle_x > 800:
        obstacle_x = 0
        obstacle_y = random.randrange(0, 800)

    if obstacle_y <= y + car_height and obstacle_y >= y and obstacle_x <= x + car_width and obstacle_x >= x:
        pygame.transform.scale(carImg, (100, car_height + 100))
        print('collision')
        # carImg = pygame.image.load('BNGLogo.png')

    draw_car(x, y)
    draw_obstacle(obstacle_x, obstacle_y, 10, 10)

    pygame.display.update()
