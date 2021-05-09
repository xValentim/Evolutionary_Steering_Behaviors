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
t_jump = 1000
t = 0
relogio = pygame.time.Clock()
window = pygame.display.set_mode((largura, altura + tamanho_barra))
pygame.display.set_caption("Evolutionary Steering Behaviors")
window.fill(gray)
# Constroi o tapete de sierpinski
walls = sierpinski_carpet()
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

def texto(msg, cor, tam, x, y):
    font = pygame.font.SysFont(None, tam)
    texto1 = font.render(msg, True, cor)
    window.blit(texto1, [x, y])

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
                for i in range(50):
                    x = random.randint(1, largura)
                    y = random.randint(1, altura)
                    food.append(pygame.Vector2(x, y))
            if event.key == pygame.K_p:
                for i in range(50):
                    x = random.randint(1, largura)
                    y = random.randint(1, altura)
                    poison.append(pygame.Vector2(x, y))
            if event.key == pygame.K_v:
                for i in range(5):
                    x = random.randint(1, largura)
                    y = random.randint(1, altura)
                    vehicles_list.append(Vehicle(x, y))
            if event.key == pygame.K_d:
                dna_view = not dna_view

        #target = pygame.mouse.get_pos()
        
    window.fill(gray)
    pygame.draw.line(window, black, (0, altura + 5), (largura, altura + 5), width=5)

    #TODO: Function Insert food
    z = random.random()
    if z < 0.1:
        x = random.randint(1, largura)
        y = random.randint(1, altura)
        food.append(pygame.Vector2(x, y))

    #TODO: Function Insert posion
    z = random.random()
    if z < 0.1:
        x = random.randint(1, largura)
        y = random.randint(1, altura)
        poison.append(pygame.Vector2(x, y))
    
    #TODO: Projeto final
    if t >= t_jump:
        for i in range(5):
            x = random.randint(1, largura)
            y = random.randint(1, altura)
            vehicles_list.append(Vehicle(x, y))
        t = 0
    #t += 1

    
    

    i = 0
    while i < len(vehicles_list):

        v1 = vehicles_list[i]
        v1.behaviors(food, poison, walls)
        v1.update()

        newVehicle = v1.clone(0.001) # Argument is probability to clone
        if newVehicle != None:
            vehicles_list.append(newVehicle)

        health_i = round(v1.health) + 1
        if health_i < 1:
            health_i = 1
        elif health_i > 7:
            health_i = 7
        k = float(v1.r)
        vehicles[health_i] = pygame.transform.scale(vehicles_base[health_i], (int(k * 30), int(k * 16)))

        teta = v1.velocity.as_polar()
        teta = teta[1]
        
        vehicles[health_i] = pygame.transform.rotate(vehicles[health_i], -teta)
        
        rect = vehicles[health_i].get_rect()
        rect.center = v1.position
        
        window.blit(vehicles[health_i], rect)
        to_draw_dna(window, v1, dna_view)
        
        #print(v1.health)

        if v1.dead():
            food.append(v1.position)
            del(vehicles_list[i])
        i += 1

    '''texto(f"V1: Health={velocidade:.7f} Dna={}", white, 20, 10, altura - 80)
    texto(f"V2: {velocidade:.7f}", white, 20, 10, altura - 60)
    texto(f"V3: {min(p1.distancias):.5f}", white, 20, 10, altura - 40)
    texto(f"V4: {max(p1.distancias):.5f}", white, 20, 10, altura - 20)'''

    #TODO: Draw walls
    for i in range(len(walls)):
        pygame.draw.circle(window, gray3, walls[i], 5)
    #TODO: Draw foods
    for i in range(len(food)):
        pygame.draw.circle(window, green, food[i], 1)
    #TODO: Draw poison
    for i in range(len(poison)):
        pygame.draw.circle(window, red, poison[i], 1)
        
    relogio.tick(60)
    pygame.display.update()

pygame.quit()