from cgitb import text
import pygame, sys
pygame.init()
pygame.display.set_caption("Arush")
import random

screen = pygame.display.set_mode((1920,1080))
FONT = pygame.font.Font(None,72)
myfont = pygame.font.SysFont("monospace",100)
color =(0,255,255)
rectc = (255,0,0)

while True:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                #color = ((random.randint(0,255),random.randint(0,255), random.randint(0,255)))
                text1 = myfont.render("Hello World",500,rectc)
                screen.blit(text1,(700,400))
    
    
    #screen.fill(color)
    #text1 = myfont.render("Hello World",500,rectc)
    #screen.blit(text1,(700,400))
    #pygame.draw.rect(screen, rectc, pygame.Rect(100,100,100,100))
    pygame.display.update()
    
