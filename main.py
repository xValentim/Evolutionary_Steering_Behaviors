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
vehicles_list = []
for i in range(10):
    x = random.randint(1, largura)
    y = random.randint(1, altura)
    vehicles_list.append(Vehicle(x, y))
food = []
for i in range(50):
    x = random.randint(1, largura)
    y = random.randint(1, altura)
    food.append(pygame.Vector2(x, y))
poison = []
for i in range(50):
    x = random.randint(1, largura)
    y = random.randint(1, altura)
    poison.append(pygame.Vector2(x, y))

continua = True
while continua:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            continua = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                continua = False
            if event.key == pygame.K_f:
                for i in range(5):
                    x = random.randint(1, largura)
                    y = random.randint(1, altura)
                    food.append(pygame.Vector2(x, y))
            if event.key == pygame.K_p:
                for i in range(5):
                    x = random.randint(1, largura)
                    y = random.randint(1, altura)
                    poison.append(pygame.Vector2(x, y))
            if event.key == pygame.K_v:
                for i in range(5):
                    x = random.randint(1, largura)
                    y = random.randint(1, altura)
                    vehicles_list.append(Vehicle(x, y))

        #target = pygame.mouse.get_pos()
        
    window.fill(gray)

    #for i in range(len(vehicles_list)):
    i = 0
    while i < len(vehicles_list):
        v1 = vehicles_list[i]
        v1.behaviors(food, poison)
        v1.update()

        health_i = round(v1.health) + 1
        if health_i < 1:
            health_i = 1
        k = float(v1.r)
        vehicles[health_i] = pygame.transform.scale(vehicles_base[health_i], (int(k * 30), int(k * 16)))

        teta = v1.velocity.as_polar()
        teta = teta[1]
        
        vehicles[health_i] = pygame.transform.rotate(vehicles[health_i], -teta)
        
        rect = vehicles[health_i].get_rect()
        rect.center = v1.position
        
        window.blit(vehicles[health_i], rect)

        pygame.draw.line(window, green, v1.position, (v1.position + v1.velocity.normalize() * v1.dna[0] * 10), width=1)
        pygame.draw.line(window, red, v1.position, (v1.position + v1.velocity.normalize() * v1.dna[1] * 10), width=1)

        print(v1.health)

        if v1.dead():
            del(vehicles_list[i])
        i += 1


    for i in range(len(food)):
        pygame.draw.circle(window, green, food[i], 2)
    
    for i in range(len(poison)):
        pygame.draw.circle(window, red, poison[i], 2)
        
    relogio.tick(45)
    pygame.display.update()

pygame.quit()