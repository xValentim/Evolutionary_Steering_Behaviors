import pygame
from math import *
largura = 900
altura = 450
tamanho_barra = 200

gray = (51, 51, 51)
gray2 = (41, 41, 41)
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

def to_draw_dna(window, v1):
    pygame.draw.line(window, green, v1.position, (v1.position + v1.velocity.normalize() * v1.dna[0] * 20), width=2)
    pygame.draw.line(window, red, v1.position, (v1.position + v1.velocity.normalize() * v1.dna[1] * 20), width=1)
    pygame.draw.circle(window, green, v1.position, int(v1.dna[2]), width=1)
    pygame.draw.circle(window, red, v1.position, int(v1.dna[3]), width=1)

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
    return lista_de_vetores

#print(sierpinski_carpet())

'''void sc(){          // sierpinski carpet
  for (float i = 1; i <= L; i++){
    for (float j = 1; j <= L; j++){
      for (float kk = 0; kk <= k-1; kk++){
        /*float aux1 = round((i) / pow(3, kk));
        float aux2 = round((j) / pow(3, kk));*/
        if(floor((i-1) / pow(3, kk)) % 3.0 == 1.0 && floor((j-1) / pow(3, kk)) % 3.0 == 1.0){ 
          mol[(int)i][(int)j] = 0;
        }
      }
    }
  }
  aux = 1;
}'''