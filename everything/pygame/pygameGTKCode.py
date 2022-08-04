import pygame, sys #behövs för att använda pygame
pygame.init() 
pygame.display.set_caption("Arush")
import random

screen = pygame.display.set_mode((1100,600)) #screen size to display

color =(0,0,0) #default color of screen when starting program

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            sys.exit() #this and over code to close the window which pops up
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: #code to active a key 
                color = ((random.randint(0,255),random.randint(0,255), random.randint(0,255))) #what happens when a key is pressed
    screen.fill(color)
    pygame.display.update()

