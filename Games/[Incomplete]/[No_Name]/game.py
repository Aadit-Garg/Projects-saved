import sys
import pygame
from variables import *

pygame.init()

screen = pygame.display.set_mode((DIM))
pygame.display.set_caption(NAME)
Run = True
m_x,m_y=X+50,Y+50
run = False

while Run:
    screen.fill(GREEN)
    keys = pygame.key.get_pressed()

    if run:
        m_x,m_y = pygame.mouse.get_pos()
        m_y = (m_x/m_y)

    for events in pygame.event.get():
        if events.type == pygame.MOUSEBUTTONUP:
            run=False
        elif events.type == pygame.MOUSEBUTTONDOWN:
            run = True
            

        if events.type == pygame.QUIT:
            Run = False
            sys.exit()
        
    SQUARE(pygame, screen)
    SQUARE(pygame, screen,y2=80, color=(BLACK))
    LINE(pygame,screen,X,Y,m_x,m_y,GREY)
    CIRCLE(pygame, screen,(X,Y),10,RED)
    pygame.display.update()    