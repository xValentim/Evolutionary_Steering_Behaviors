import pygame
import math
import random
from values import *

class Vehicle:
    def __init__(self, x=0 , y=0):
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, -0.001)
        self.acceleration = pygame.Vector2()
        self.r = 0.75 + random.random() / 4
        self.maxspeed = 5
        self.maxforce = 0.3
        self.health = 100

    def limit(self, limit_value, vector):
        if vector.magnitude_squared() > limit_value * limit_value:
            return (vector.normalize()) * limit_value
        else:
            return vector
        #return (vector.normalize()) * limit_value

    def eat(self, lista):
        # list of foods
        record = largura
        record_2 = record * record
        Radius_eat = 10
        closest = -1

        # List of food
        for i in range(len(lista)):
            d_2 = (lista[i] - self.position).magnitude_squared()
            if d_2 < record_2:
                record_2 = d_2
                closest = i


        # If there is food: seek closest
        if closest != -1: 
            self.seek(lista[closest])
             
        # Eat food and remove food of list
        if record_2 < Radius_eat * Radius_eat:
            lista.pop(closest)

        
        
    # Update location
    def update(self):
        
        # Update velocity
        self.velocity += self.acceleration

        # Limit is maxspeed
        self.velocity = self.limit(self.maxspeed, self.velocity)

        # Update location with new velocity
        self.position += self.velocity

        # Boundary condition
        self.position.x = self.position.x % largura
        self.position.y = self.position.y % altura


        # Set zero acceleration
        self.acceleration = self.acceleration * 0

    def applyForce(self, force):
        self.acceleration += force
    
    def seek(self, target):
        # Calculate desired
        desired = target - self.position
        desired = desired.normalize() * self.maxspeed

        # Calculate steer (Craig Raynolds classic vehicle)
        # steering = desired - velocity
        steer = desired - self.velocity

        # Limit steer
        steer = self.limit(self.maxforce, steer)

        # Apply force
        self.applyForce(steer)



'''v1 = Vehicle()
v = pygame.Vector2(1, 1)
angle = v.as_polar()
print(angle)
limit = 10
for i in range(10):
    v1.position += v
    v1.position = v1.limit(limit, v1.position)
    print(v1.position)'''

