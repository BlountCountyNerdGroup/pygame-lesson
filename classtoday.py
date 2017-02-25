import pygame
import random

pygame.init()

# show how to define colors
SKY_BLUE = (135, 206, 235)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# show how to set up screen
SCREEN_SIZE = (800, 600) # width, height

gameDisplay = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Game')

gameDisplay.fill(BLACK)

# show how to draw rectangles
pygame.draw.rect(gameDisplay, WHITE, [400, 400, 50, 50]) # x, y, width, height

# once you draw something, you have to update it
pygame.display.update()

# show how to load images
carImg = pygame.image.load('spaceship.png')
carX = 300
carY = 300
gameDisplay.blit(carImg, (carX, carY))

# update again
pygame.display.update()

starX = random.randrange(0, 800)
starY = 0

# to simulate movement
while True:
    for event in pygame.event.get():
        print(event)

        if event.type == pygame.QUIT:
            exit()

    # always repaint the whole canvas before drawing
    gameDisplay.fill(BLACK)

    # obstacles
    starY += 1

    pygame.draw.rect(gameDisplay, WHITE, [starX, starY, 50, 50])

    # once star has flown by, draw a new one
    if starY >= 600:
        starY = 0
        starX = random.randrange(0, 800)

    # draw the car and perhaps make the car move
    carY -= .1
    gameDisplay.blit(carImg, (carX, carY))

    #update again
    pygame.display.update()