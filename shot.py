import pygame
import constants
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, position, velocity):
        super().__init__(position.x, position.y, constants.SHOT_RADIUS)
        self.velocity = velocity
        
    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            (self.position.x, self.position.y),
            self.radius,
            0 
            )
    
    def update(self, dt):
        self.position += self.velocity * dt
