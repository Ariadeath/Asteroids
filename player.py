import pygame
import constants
import circleshape
from shot import Shot

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(
            screen, # surface for drawing
            "white", # color of triangle
            self.triangle(), # list of points from triangle
            2 # line width of pixels
        )
    
    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        
        self.timer -= dt
        
    def shoot(self):
        if self.timer <= 0:
            velocity = pygame.Vector2(0, 1)
        
            # Rotate based on player rotation
            velocity = velocity.rotate(self.rotation)
        
            # Scale by shoot speed
            velocity = velocity * constants.PLAYER_SHOOT_SPEED

            Shot(self.position, velocity)

            # Added cooldown to shots
            self.timer = constants.PLAYER_SHOOT_COOLDOWN

            
        