import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame 
import sys
import constants
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 # Delta time starts at 0 here
    
    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Set containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    # Create Instances
    player_instance = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    # Game loop
    running = True
    game_over = False
    
    while running:
        #Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
         
        if not game_over:

            #Update game state
            updatable.update(dt) # Where to hook in update method
        
            # Check for collisions
            for asteroid in asteroids:
                if player_instance.is_colliding(asteroid):
                    print("Game over!")
                    game_over = True
                    break
            
                for shot in shots:
                    if shot.is_colliding(asteroid):
                        shot.kill()
                        asteroid.split()
            
            # Render
            screen.fill("black")
            for drawable_obj in drawable:
                drawable_obj.draw(screen)
        else:
            # Game over screen
            screen.fill("black")

            # Draw game over text
            font = pygame.font.Font(None, 74)
            text = font.render("GAME OVER", True, "red")
            text_rect = text.get_rect(center=(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2))
            screen.blit(text, text_rect)

            # Draw restart instructions
            font_small = pygame.font.Font(None, 36)
            restart_text = font_small.render("Press R to restart", True, "white")
            restart_rect = restart_text.get_rect(center=(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2 + 60))
            screen.blit(restart_text, restart_rect)

            # Check for R key to restart
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                # Reset game state
                game_over = False
                
                # Reset player position, rotation, and shooting cooldown
                player_instance.position = pygame.Vector2(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
                player_instance.rotation = 0
                player_instance.timer = 0

                # Clear asteroids and shots
                for asteroid in asteroids.sprites():
                    asteroid.kill()
                
                for shot in shots.sprites():
                    shot.kill()

                # Creates a new asteroid field.
                AsteroidField() 

        # Updates the display
        pygame.display.flip()

        # Regulates FPS
        dt = clock.tick(60)/ 1000

        
    

if __name__ == "__main__":
    main()