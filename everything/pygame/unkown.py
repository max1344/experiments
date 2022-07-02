from ctypes import sizeof
from pickle import TRUE
import pygame
import sys
import time 
pygame.init()
screen = pygame.display.set_mode((1100,600))
FONT = pygame.font.Font(None,72)
waiting = True



tick = 0
statements = ["Ready", "Set", "Go"]
while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and waiting == False:
                text = FONT.render("Space player WON!", True, (0,0,0))
                waiting = True
            if event.key == pygame.K_RIGHT and waiting == False:
                text = FONT.render("Right player WON!", True, (0,0,0))
                waiting = True
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            print("haha fak ju ") 

    text = FONT.render("", True, (0,0,0))
    Clock = pygame.time.Clock()
    Clock.tick(60)
    tick += 1
    screen.fill((0,255,0))
    if (tick+30) < 180:
        text = FONT.render(statements[(tick+30)//60], True, (0,0,0))
    else:
        text = FONT.render(" ", True, (0,0,0))
    screen.blit(text,((1100//2) - (72 // 2) , (600//2) - (72 // 2)))
    pygame.display.update()
    print(tick)


