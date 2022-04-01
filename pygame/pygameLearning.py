
import pygame
import sys

win = pygame.display.set_mode((1100,600))
pygame.init()

pygame.display.set_caption("Test Run")

x = 50
y = 50
high = 60
width = 40
vel = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            sys.exit() #this and over code to close the window which pops up
    pygame.time.delay(100 )
    

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
    if keys[pygame.K_LSHIFT]:
        vel = vel + 20
    if keys[pygame.K_k]:
        vel = vel - 20
    
    if vel >= 40:
        vel = vel - 20
    if vel <= 0:
        vel = vel + 20

    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0), (x,y,width,high))
    pygame.display.update()



