import pygame
import math
import random
from values import *

class Vehicle:
    def __init__(self, x=0 , y=0):
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(random.uniform(-2, 2), random.uniform(-2, 2))
        self.acceleration = pygame.Vector2()
        #self.r = random.uniform(0.25, 0.8)
        self.r = 0.8
        self.maxspeed = 3
        self.maxforce = 0.2
        self.health = 4
        # Peso food
        a = random.uniform(-2, 2)
        # Peso poison
        b = random.uniform(-2, 2)
        # Food Perception
        c = random.uniform(0, 70)
        # Poison Perception
        d = random.uniform(0, 70)
        self.dna = [a, b, c, d]
        #self.skin = round(a + b)
        #print(self.skin)

    #TODO: Projeto final
    def limit(self, limit_value, vector):
        if vector.magnitude_squared() > limit_value * limit_value:
            return (vector.normalize()) * limit_value
        else:
            return vector
        #return (vector.normalize()) * limit_value

    def behaviors(self, good, bad):
        steerG = self.eat(good, 0.5, self.dna[2])
        steerB = self.eat(bad, -0.1, self.dna[3])

        steerG *= self.dna[0] 
        steerB *= self.dna[1] 

        self.applyForce(steerG)
        self.applyForce(steerB)

    def eat(self, lista, nutrition, PerceptionRadius):
        # list of foods
        record = largura
        record_2 = record * record
        Radius_eat = 10
        closest = -1

        # List of food
        for i in range(len(lista)):
            d_2 = (lista[i] - self.position).magnitude_squared()
            if d_2 < record_2 and d_2 < PerceptionRadius * PerceptionRadius:
                record_2 = d_2
                closest = i
             
        # Eat food and remove food of list
        if record_2 < Radius_eat * Radius_eat:
            lista.pop(closest)
            self.health += nutrition
            if self.health >= 6:
                self.health = 6
        elif closest > -1:
            return self.seek(lista[closest])
        return pygame.Vector2()
        
    #TODO: Projeto final
    def dead(self):
        return self.health < 0

    #TODO: Projeto final
    # Update location
    def update(self):

        self.health -= 0.009

        # Boundary condition (depende da aceleração)
        self.boundary()

        # Update velocity
        self.velocity += self.acceleration

        # Limit is maxspeed
        self.velocity = self.limit(self.maxspeed, self.velocity)

        # Update location with new velocity
        self.position += self.velocity

        # Boundary condition (depende da posição)
        #self.periodic_boundary()
        
    
        # Set zero acceleration
        self.acceleration = self.acceleration * 0

    def boundary(self):
        d = 1
        desired = pygame.Vector2()
        if self.position.x < d:
            desired = pygame.Vector2(self.maxspeed, self.velocity.y)
        elif self.position.x > largura - d:
            desired = pygame.Vector2(-self.maxspeed, self.velocity.y)
        if self.position.y < d:
            desired = pygame.Vector2(self.velocity.x, self.maxspeed)
        elif self.position.y > altura - d:
            desired = pygame.Vector2(self.velocity.x, -self.maxspeed)

        if desired.magnitude_squared() > 0:
            desired = desired.normalize() * self.maxspeed
            steer = desired - self.velocity
            steer = self.limit(self.maxforce, steer)
            self.applyForce(steer)

    #TODO: Projeto final
    def periodic_boundary(self):
        self.position.x = self.position.x % largura
        self.position.y = self.position.y % altura

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

        return steer

        # Apply force
        #self.applyForce(steer)

'''v1 = Vehicle()
v = pygame.Vector2(1, 1)
angle = v.as_polar()
print(angle)
limit = 10
for i in range(10):
    v1.position += v
    v1.position = v1.limit(limit, v1.position)
    print(v1.position)'''