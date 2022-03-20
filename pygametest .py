from pickle import TRUE
import pygame
import sys
import time 
pygame.init()
screen = pygame.display.set_mode((1100,600))
FONT = pygame.font.Font(None,72)

tick = 0
while True:
    text = FONT.render("", True, (0,0,0))
    Clock = pygame.time.Clock()
    Clock.tick(30)
    tick += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
    screen.fill((0,255,0))
    if tick > 30 and tick <60:
        text = FONT.render("Ready", True, (0,0,0))
    if tick > 60 and tick <90:
        text = FONT.render("Set", True, (0,0,0))
    if tick > 90 and tick <120:
        text = FONT.render("Go", True, (0,0,0))
    screen.blit(text,(0,0))
    pygame.display.update()


