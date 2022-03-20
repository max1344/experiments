from pickle import TRUE
import pygame
import sys
import time 
pygame.init()
screen = pygame.display.set_mode((1100,600))
FONT = pygame.font.Font(None,72)



tick = 0
statements = ["Ready", "Set", "Go"]
while True:
    text = FONT.render("", True, (0,0,0))
    Clock = pygame.time.Clock()
    Clock.tick(1)
    tick += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #pygame.quit()
            #sys.exit()
            print("haha fak ju ") 
    screen.fill((0,255,0))
    text = FONT.render(statements[tick - 1], True, (0,0,0))
    screen.blit(text,(0,0))
    pygame.display.update()
    print(tick)


