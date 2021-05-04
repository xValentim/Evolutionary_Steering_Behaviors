import pygame
import math

class Vehicle:
    def __init__(self, x=0 , y=0):
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, -0.001)
        self.acceleration = pygame.Vector2()
        self.r = 5
        self.maxspeed = 8
        self.maxforce = 0.2
        self.health = 100

    def limit(self, limit_value, vector):
        if vector.magnitude_squared() > limit_value * limit_value:
            return (vector.normalize()) * limit_value
        else:
            return vector
        #return (vector.normalize()) * limit_value

    # Update location
    def update(self):
        
        # Update velocity
        self.velocity += self.acceleration

        # Limit is maxspeed
        self.velocity = self.limit(self.maxspeed, self.velocity)

        # Update location with new velocity
        self.position += self.velocity


        # Set zero acceleration
        self.acceleration = self.acceleration * 0

    def applyForce(self, force):
        self.acceleration += force
    
    def seek(self, target):
        desired = target - self.position
        desired = desired.normalize() * self.maxspeed
        steer = desired - self.velocity
        #steer.scale_to_length(self.maxforce)
        steer = self.limit(self.maxforce, steer)
        self.applyForce(steer)

    def steering(self):
        pass
        

# steering = desired - velocity

'''v1 = Vehicle()
v = pygame.Vector2(1, 1)
limit = 10
for i in range(10):
    v1.position += v
    v1.position = v1.limit(limit, v1.position)
    print(v1.position)'''

