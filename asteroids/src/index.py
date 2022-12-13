from services.asteroids import AsteroidsGame

def main():
    game = AsteroidsGame()
    while game.running:
        game.curr_menu.show_menu()
        game.gameloop()

if __name__ == "__main__":
    main()
