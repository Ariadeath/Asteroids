import pygame 
from constants import *
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #Game loop
    while True:
        #Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #Fills the screen with black
        screen.fill("black")
        
        #Updates the display
        pygame.display.flip()
    

if __name__ == "__main__":
    main()