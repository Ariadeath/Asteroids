import pygame
from circleshape import CircleShape
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(
            surface, #Surface for showing up
            pygame.Color("white"), # Color
            (self.position.x, self.position.y), #Position
            self.radius, # Radius
            2 # Width parameter
            )
    
    def update(self, dt):
        self.position += self.velocity * dt
