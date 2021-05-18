import pygame
from math import *
largura = 1020
altura = 450 + 150
tamanho_barra = 200
dna_view = False

gray = (51, 51, 51)
gray2 = (41, 41, 41)
gray3 = (31, 31, 31)
gray4 = (11, 11, 11)
black = (0, 0, 0)
white = (255, 255, 255)
red = (250, 0, 0)
green = (0, 250, 0)
blue = (0, 0, 250)
cyan = (0, 15, 150)

vehicle_img = pygame.image.load("Evolutionary_Steering_Behaviors/imgs_vehicles/vehicle_none.png")
vehicle_img0 = pygame.image.load("Evolutionary_Steering_Behaviors/imgs_vehicles/vehicle_none.png")
vehicle_img1 = pygame.image.load("Evolutionary_Steering_Behaviors/imgs_vehicles/vehicle_health1.png")
vehicle_img2 = pygame.image.load("Evolutionary_Steering_Behaviors/imgs_vehicles/vehicle_health2.png")
vehicle_img3 = pygame.image.load("Evolutionary_Steering_Behaviors/imgs_vehicles/vehicle_health3.png")
vehicle_img4 = pygame.image.load("Evolutionary_Steering_Behaviors/imgs_vehicles/vehicle_health4.png")
vehicle_img5 = pygame.image.load("Evolutionary_Steering_Behaviors/imgs_vehicles/vehicle_health5.png")
vehicle_img6 = pygame.image.load("Evolutionary_Steering_Behaviors/imgs_vehicles/vehicle_health6.png")
vehicle_img7 = pygame.image.load("Evolutionary_Steering_Behaviors/imgs_vehicles/vehicle_health6.png")


vehicles_base = [
    vehicle_img0,
    vehicle_img7,
    vehicle_img6,
    vehicle_img5,
    vehicle_img4,
    vehicle_img3,
    vehicle_img2,
    vehicle_img1,
    vehicle_img1
]

vehicles = list(vehicles_base)

def to_draw_dna(window, v1, dna_view):
    if dna_view:
        pygame.draw.line(window, green, v1.position, (v1.position + v1.velocity.normalize() * v1.dna[0] * 20), width=3)
        pygame.draw.line(window, red, v1.position, (v1.position + v1.velocity.normalize() * v1.dna[1] * 20), width=2)
        pygame.draw.line(window, black, v1.position, (v1.position + v1.velocity.normalize() * v1.dna[2] * 20), width=1)
        pygame.draw.circle(window, green, v1.position, int(v1.dna[3]), width=1)
        pygame.draw.circle(window, red, v1.position, int(v1.dna[4]), width=1)
        pygame.draw.circle(window, gray4, v1.position, int(v1.dna[5]), width=1)

# Constroi o tapete de sierpinski
def sierpinski_carpet():
    k = 2
    LL = 3 ** k
    L = int(LL)
    lista_de_vetores = []
    for i in range(L):
        for j in range(L):
            kk = 0
            while kk <= k-1:
                if floor((i - 1) / pow(3, kk)) % 3 == 1 and floor((j - 1) / pow(3, kk)) % 3 == 1:
                    x, y = float(i), float(j)
                    lista_de_vetores.append(pygame.Vector2(x, y))
                kk += 1
    aumento = 50
    soma_total_x = 0
    soma_total_y = 0
    qtde_total = 0
    for i in range(len(lista_de_vetores)):
        lista_de_vetores[i].x = lista_de_vetores[i].x * aumento #+ largura / 4
        lista_de_vetores[i].y = lista_de_vetores[i].y * aumento #+ altura / 4
        #pygame.draw.rect(window, black, (lista_de_vetores[i].x, lista_de_vetores[i].y, aumento, aumento), 0)
        soma_total_x += lista_de_vetores[i].x
        soma_total_y += lista_de_vetores[i].y
        qtde_total += 1

    # Calcula o centro da figura, soma todos os vetores posição e divide pela qtde total
    centro_x = soma_total_x / qtde_total
    centro_y = soma_total_y / qtde_total
    centro_sc = pygame.Vector2(centro_x, centro_y)
    centro = pygame.Vector2(largura / 2, altura / 2)

    # Calcula o vetor de translação
    vetor_de_translação = centro - centro_sc

    # Translada os muros
    for i in range(len(lista_de_vetores)):
        lista_de_vetores[i] += vetor_de_translação #+ largura / 4
        #pygame.draw.rect(window, gray2, (lista_de_vetores[i].x, lista_de_vetores[i].y, aumento / 3, aumento / 3), 0)
     
    return lista_de_vetores
