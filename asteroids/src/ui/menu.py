import sys
import pygame
from utils import load_image

class Menu():
    def __init__(self, game):
        self.game = game
        self.run_menu = True
        self.midx = self.game.width/2
        self.midy = self.game.height/2
        self.pointer = load_image("spaceship")
        self.pointer = pygame.transform.rotate(self.pointer, -90)
        self.pointer_rect = self.pointer.get_rect()
        self.offset = -220
        self.up_key, self.down_key, self.enter_key, self.esc_key = False, False, False, False

    def blit_screen(self):
        self.game.window.blit(self.game.background_image, (0,0))
        pygame.display.update()
        self.reset_keys()

    def check_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.down_key = True
                if event.key == pygame.K_UP:
                    self.up_key = True
                if event.key == pygame.K_ESCAPE:
                    self.esc_key = True
                if event.key == pygame.K_RETURN:
                    self.enter_key = True

    def reset_keys(self):
        self.up_key, self. down_key, self.enter_key, self.esc_key = False, False, False, False

class MainMenu(Menu):
    def __init__(self, game):
        super().__init__(game)
        self.state = "New game"
        self.newgamex, self.newgamey = self.midx, self.midy + 50
        self.highscorex, self.highscorey = self.midx, self.midy + 100
        self.exitx, self.exity = self.midx, self.midy + 150
        self.pointer_rect.center = (self.newgamex + self.offset, self.newgamey)

    def blit_screen(self):
        self.game.window.blit(self.game.background_image, (0,0))
        self.game.draw_text("Menu", 45, self.midx, self.midy - 50)
        self.game.draw_text("New game", 32, self.newgamex, self.newgamey)
        self.game.draw_text("High scores", 32, self.highscorex, self.highscorey)
        self.game.draw_text("Exit", 32, self.exitx, self.exity)
        self.game.window.blit(self.pointer, (self.pointer_rect.x, self.pointer_rect.y))
        pygame.display.update()
        self.reset_keys()

    def show_menu(self):
        self.game.soundplayer.stop_music()
        self.run_menu = True
        while self.run_menu:
            self.check_menu_events()
            self.check_input()
            self.blit_screen()

    def move_pointer(self):
        if self.down_key:
            self.game.soundplayer.play_move_effect()
            if self.state == "New game":
                self.pointer_rect.center = (self.highscorex + self.offset, self.highscorey)
                self.state = "High scores"
            elif self.state == "High scores":
                self.pointer_rect.center = (self.exitx + self.offset, self.exity)
                self.state = "Exit"
            elif self.state == "Exit":
                self.pointer_rect.center = (self.newgamex + self.offset, self.newgamey)
                self.state = "New game"
        elif self.up_key:
            self.game.soundplayer.play_move_effect()
            if self.state == "New game":
                self.pointer_rect.center = (self.exitx + self.offset, self.exity)
                self.state = "Exit"
            elif self.state == "High scores":
                self.pointer_rect.center = (self.newgamex + self.offset, self.newgamey)
                self.state = "New game"
            elif self.state == "Exit":
                self.pointer_rect.center = (self.highscorex + self.offset, self.highscorey)
                self.state = "High scores"

    def check_input(self):
        self.move_pointer()
        if self.enter_key:
            self.game.soundplayer.play_click_effect()
            if self.state == "New game":
                self.game.initialize_game()
                self.game.soundplayer.play_music()
            elif self.state == "High scores":
                self.game.curr_menu = HighScores(self.game)
            elif self.state == "Exit":
                sys.exit()
            self.run_menu = False

class HighScores(Menu):

    def blit_screen(self):
        self.game.window.blit(self.game.background_image, (0,0))
        self.game.draw_text("High scores", 45, self.midx, self.midy - 100)
        self.game.draw_text("1  top player", 24, self.midx, self.midy)
        pygame.display.update()
        self.reset_keys()

    def show_menu(self):
        self.run_menu = True
        while self.run_menu:
            self.check_menu_events()
            self.check_input()
            self.blit_screen()

    def check_input(self):
        if self.esc_key:
            self.game.curr_menu = self.game.main_menu
            self.run_menu = False

class PauseMenu(Menu):
    def __init__(self, game):
        super().__init__(game)
        self.state = "Resume game"
        self.offset = -250
        self.resumex, self.resumey = self.midx, self.midy + 50
        self.menux, self.menuy = self.midx, self.midy + 100
        self.pointer_rect.center = (self.resumex + self.offset, self.resumey)

    def blit_screen(self):
        self.game.window.blit(self.game.background_image, (0,0))
        self.game.draw_text("Game paused", 45, self.midx, self.midy - 50)
        self.game.draw_text("Resume game", 32, self.resumex, self.resumey)
        self.game.draw_text("Back to menu", 32, self.menux, self.menuy)
        self.game.window.blit(self.pointer, (self.pointer_rect.x, self.pointer_rect.y))
        pygame.display.update()
        self.reset_keys()

    def show_menu(self):
        self.run_menu = True
        while self.run_menu:
            self.check_menu_events()
            self.check_input()
            self.blit_screen()

    def move_pointer(self):
        if self.down_key:
            self.game.soundplayer.play_move_effect()            
            if self.state == "Resume game":
                self.pointer_rect.center = (self.menux + self.offset, self.menuy)
                self.state = "Back to menu"
            elif self.state == "Back to menu":
                self.pointer_rect.center = (self.resumex + self.offset, self.resumey)
                self.state = "Resume game"
        elif self.up_key:
            self.game.soundplayer.play_move_effect()
            if self.state == "Resume game":
                self.pointer_rect.center = (self.menux + self.offset, self.menuy)
                self.state = "Back to menu"
            elif self.state == "Back to menu":
                self.pointer_rect.center = (self.resumex + self.offset, self.resumey)
                self.state = "Resume game"

    def check_input(self):
        self.move_pointer()
        if self.enter_key:
            self.game.soundplayer.play_click_effect()
            if self.state == "Resume game":
                self.game.playing = True
                self.game.curr_menu = self.game.main_menu
            elif self.state == "Back to menu":
                self.game.soundplayer.stop_music()
                self.game.curr_menu = self.game.main_menu
            self.run_menu = False
