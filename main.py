import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame 
import constants
import player

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 # Delta time starts at 0 here
    
    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    # Set containers
    player.Player.containers = (updatable, drawable)
    
    # Create a single player instance
    player_instance = player.Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    #Game loop
    running = True
    while running:
        #Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #Update game state
        updatable.update(dt) # Where to hook in update method
        
        #Render
        screen.fill("black")
        for drawable_obj in drawable:
            drawable_obj.draw(screen)
        
        #Updates the display
        pygame.display.flip()

        # Regulates FPS
        dt = clock.tick(60)/ 1000

        
    

if __name__ == "__main__":
    main()