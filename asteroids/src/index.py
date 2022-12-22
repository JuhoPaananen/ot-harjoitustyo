import pygame
from services.asteroids import AsteroidsGame

def main():
    pygame.init()
    pygame.freetype.init()
    game = AsteroidsGame()
    while game.running:
        game.curr_menu.show_menu()
        game.gameloop()
      
    pygame.quit()
    print("Thank you for playing!")

if __name__ == "__main__":
    main()
