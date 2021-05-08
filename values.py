import pygame
largura = 900
altura = 450
tamanho_barra = 200

gray = (51, 51, 51)
black = (0, 0, 0)
white = (255, 255, 255)
red = (250, 0, 0)
green = (0, 250, 0)
blue = (0, 0, 250)

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