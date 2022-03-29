import pygame, sys
pygame.init()
pygame.display.set_caption("Arush")
import random

screen = pygame.display.set_mode((1100,600))

color =(0,0,0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                color = ((random.randint(0,255),random.randint(0,255), random.randint(0,255)))
    screen.fill(color)
    pygame.display.update()




#
