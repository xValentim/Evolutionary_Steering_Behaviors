import pygame
import numpy
from vehicle import *

pygame.init()
largura = 640
altura = 320

gray = (51, 51, 51)
black = (0, 0, 0)
white = (255, 255, 255)
red = (250, 0, 0)
green = (0, 250, 0)
blue = (0, 0, 250)

u = pygame.Vector2()
v = pygame.Vector2(1, 1)


# Dots green : Food
# Dots red : Poison


relogio = pygame.time.Clock()
window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Evolutionary Steering Behaviors")
window.fill(gray)
v1 = Vehicle(largura / 2, altura / 2)

continua = True
while continua:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            continua = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                continua = False
        '''if event.type == pygame.MOUSEBUTTONUP:
            target = pygame.mouse.get_pos()
            print(target)'''
        target = pygame.mouse.get_pos()
        #print(pygame.mouse.get_pos())
    
    v1.seek(target)
    v1.update()
    window.fill(gray)
    pygame.draw.circle(window, white, v1.position, v1.r)
    relogio.tick(60)
    pygame.display.update()

pygame.quit()