import pygame
import numpy
import random
from vehicle import *
from values import *

pygame.init()
u = pygame.Vector2()
v = pygame.Vector2(1, 1)

# Dots green : Food
# Dots red : Poison


relogio = pygame.time.Clock()
window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Evolutionary Steering Behaviors")
window.fill(gray)
v1 = Vehicle(largura / 2, altura / 2)
food = []
for i in range(10):
    x = random.randint(1, largura)
    y = random.randint(1, altura)
    food.append(pygame.Vector2(x, y))

continua = True
while continua:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            continua = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                continua = False
        target = pygame.mouse.get_pos()
        
    v1.seek(target)
    v1.update()
    window.fill(gray)
    #pygame.draw.circle(window, white, v1.position, v1.r)

    health_i = 0
    k = float(v1.r)
    vehicles[health_i] = pygame.transform.scale(vehicles_base[health_i], (int(k * 30), int(k * 16)))

    teta = v1.velocity.as_polar()
    teta = teta[1]
    
    vehicles[health_i] = pygame.transform.rotate(vehicles[health_i], -teta)
    
    rect = vehicles[health_i].get_rect()
    rect.center = v1.position
    
    window.blit(vehicles[health_i], rect)
    for i in range(len(food)):
        pygame.draw.circle(window, green, food[i], 2)
    relogio.tick(60)
    pygame.display.update()

pygame.quit()