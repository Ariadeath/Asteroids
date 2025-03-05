import pygame 
import constants
def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 # Delta time starts at 0 here

    #Game loop
    running = True
    while running:
        #Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #Fills the screen with black
        screen.fill("black")
        
        #Updates the display
        pygame.display.flip()

        # Regulates FPS
        dt = clock.tick(60)/ 1000
    

if __name__ == "__main__":
    main()