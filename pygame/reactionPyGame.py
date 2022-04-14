import pygame, sys, time 
pygame.init() 
pygame.display.set_caption("Reaction Time")
import random


screen = pygame.display.set_mode((1280,720)) 
clock = pygame.time.Clock()

curent_time = 0
button_press_time = 0


color =(0,0,0) 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            sys.exit() 
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: 
                color = ((random.randint(0,255),random.randint(0,255), random.randint(0,255))) #what happens when a key is pressed
        if event.type == pygame.KEYDOWN:
            button_press_time = pygame.time.get_ticks()
        
        curent_time = pygame.time.get_ticks()

    screen.fill(color)
    pygame.display.update()
