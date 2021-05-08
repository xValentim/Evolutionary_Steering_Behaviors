import pygame
import math
import random
from values import *

class Vehicle:
    def __init__(self, x=0 , y=0, dna=[]):
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(random.uniform(-2, 2), random.uniform(-2, 2))
        self.acceleration = pygame.Vector2()
        #self.r = random.uniform(0.25, 0.8)
        self.r = 0.8
        self.maxspeed = 3
        self.maxforce = 0.2
        self.health = 4
        mr = 0.01
        if dna == []:
            # Peso food
            A = random.uniform(-2, 2)
            # Peso poison
            B = random.uniform(-2, 2)
            # Food Perception
            C = random.uniform(0, 70)
            # Poison Perception
            D = random.uniform(0, 70)
            #d = 0
            self.dna = [A, B, C, D]
            #self.skin = round(a + b)
            #print(self.skin)
        else:
            self.dna = []
            self.dna.append(dna[0])
            if random.random() < mr:
                self.dna[0] += random.uniform(-0.1, 0.1)

            self.dna.append(dna[1])
            if random.random() < mr:
                self.dna[1] += random.uniform(-0.1, 0.1)

            self.dna.append(dna[2])
            if random.random() < mr:
                self.dna[2] += random.uniform(-10, 10)

            self.dna.append(dna[3])
            if random.random() < mr:
                self.dna[3] += random.uniform(-10, 10)

    #TODO: Projeto final
    def limit(self, limit_value, vector):
        if vector.magnitude_squared() > limit_value * limit_value:
            return (vector.normalize()) * limit_value
        else:
            return vector
        #return (vector.normalize()) * limit_value

    def behaviors(self, good, bad):
        steerG = self.eat(good, 0.3, self.dna[2])
        steerB = self.eat(bad, -0.2, self.dna[3])

        steerG *= self.dna[0] / 1.5
        steerB *= self.dna[1] / 1.5

        self.applyForce(steerG)
        self.applyForce(steerB)

    def clone(self, z):
        if random.random() < z:
            return Vehicle(self.position.x, self.position.y, self.dna)
        else:
            return None

    def eat(self, lista, nutrition, PerceptionRadius):
        # list of foods
        record = largura
        record_2 = record * record
        Radius_eat = self.maxspeed
        closest = None

        # List of food
        i = 0
        #for i in range(len(lista)):
        while i < len(lista):
            d_2 = (lista[i] - self.position).magnitude_squared()
            if d_2 < Radius_eat * Radius_eat:
                lista.pop(i) ##
                self.health += nutrition
                if self.health >= 6:
                    self.health = 6
            elif d_2 < record_2 and d_2 < PerceptionRadius * PerceptionRadius:
                record_2 = d_2
                closest = lista[i]
            i += 1
        # Eat food and remove food of list
        '''if record_2 < Radius_eat * Radius_eat:
            lista.pop(closest) ##
            self.health += nutrition
            if self.health >= 6:
                self.health = 6'''

        if closest != None:
            return self.seek(closest)

        return pygame.Vector2()
        
    #TODO: Projeto final
    def dead(self):
        return self.health < 0

    #TODO: Projeto final
    # Update location
    def update(self):

        self.health -= 0.005

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
    
    def wall(self, lista_de_vetores):
        d = 10
        d_2 = d * d
        desired = pygame.Vector2()
        for wall in lista_de_vetores:
            vector_d = wall - self.position
            distance_to_wall_2 = (vector_d).magnitude_squared()
            if distance_to_wall_2 < d_2:
                desired = vector_d.normalize()

            if desired.magnitude_squared() > 0:
                desired = desired.normalize() * self.maxspeed
                steer = desired - self.velocity
                steer = self.limit(self.maxforce, steer)
                self.applyForce(-steer)

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