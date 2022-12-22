import sys
import pygame
from repositories.high_scores_repository import HighScoresRepository
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

    def _blit_screen(self):
        self.game.window.blit(self.game.background_image, (0, 0))
        pygame.display.update()
        self._reset_keys()

    def _check_menu_events(self):
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

    def _reset_keys(self):
        self.up_key, self. down_key, self.enter_key, self.esc_key = False, False, False, False


class MainMenu(Menu):
    def __init__(self, game):
        super().__init__(game)
        self.state = "New game"
        self.newgamex, self.newgamey = self.midx, self.midy + 50
        self.highscorex, self.highscorey = self.midx, self.midy + 100
        self.controlsx, self.controlsy = self.midx, self.midy + 150
        self.exitx, self.exity = self.midx, self.midy + 200
        self.pointer_rect.center = (self.newgamex + self.offset, self.newgamey)

    def _blit_screen(self):
        self.game.window.blit(self.game.background_image, (0, 0))
        self.game.draw_text("Menu", 45, self.midx, self.midy - 50)
        self.game.draw_text("New game", 32, self.newgamex, self.newgamey)
        self.game.draw_text("High scores", 32,
                            self.highscorex, self.highscorey)
        self.game.draw_text("Controls", 32, self.controlsx, self.controlsy)
        self.game.draw_text("Exit", 32, self.exitx, self.exity)
        self.game.window.blit(
            self.pointer, (self.pointer_rect.x, self.pointer_rect.y))
        pygame.display.update()
        self._reset_keys()

    def show_menu(self):
        """Näyttää Main menu ikkunan
        """
        self.game.soundplayer.stop_music()
        self.run_menu = True
        while self.run_menu:
            self._check_menu_events()
            self._check_input()
            self._blit_screen()

    def _move_pointer(self):
        if self.down_key:
            self.game.soundplayer.play_move_effect()
            if self.state == "New game":
                self.pointer_rect.center = (
                    self.highscorex + self.offset, self.highscorey)
                self.state = "High scores"
            elif self.state == "High scores":
                self.pointer_rect.center = (
                    self.controlsx + self.offset, self.controlsy)
                self.state = "Controls"
            elif self.state == "Controls":
                self.pointer_rect.center = (
                    self.exitx + self.offset, self.exity)
                self.state = "Exit"
            elif self.state == "Exit":
                self.pointer_rect.center = (
                    self.newgamex + self.offset, self.newgamey)
                self.state = "New game"
        elif self.up_key:
            self.game.soundplayer.play_move_effect()
            if self.state == "New game":
                self.pointer_rect.center = (
                    self.exitx + self.offset, self.exity)
                self.state = "Exit"
            elif self.state == "High scores":
                self.pointer_rect.center = (
                    self.newgamex + self.offset, self.newgamey)
                self.state = "New game"
            elif self.state == "Controls":
                self.pointer_rect.center = (
                    self.highscorex + self.offset, self.highscorey)
                self.state = "High scores"
            elif self.state == "Exit":
                self.pointer_rect.center = (
                    self.controlsx + self.offset, self.controlsy)
                self.state = "Controls"

    def _check_input(self):
        self._move_pointer()
        if self.enter_key:
            self.game.soundplayer.play_click_effect()
            if self.state == "New game":
                self.game.start_new_game()
                #self.game.soundplayer.play_music()
            elif self.state == "High scores":
                self.game.curr_menu = HighScoresMenu(self.game)
            elif self.state == "Controls":
                self.game.curr_menu = ControlsMenu(self.game)
            elif self.state == "Exit":
                self.game.running = False
            self.run_menu = False


class HighScoresMenu(Menu):
    def __init__(self, game, filename="high_scores.csv"):
        super().__init__(game)
        self.high_scores_repository = HighScoresRepository(filename)
        self.high_scores = []
        self.high_scores = self.high_scores_repository.get_high_scores()

    def _blit_screen(self):
        self.game.window.blit(self.game.background_image, (0, 0))
        self.game.draw_text("High scores", 45, self.midx, self.midy - 100)
        for i in range(min(10, len(self.high_scores))):
            if self.high_scores[i][0] is not None:
                name = self.high_scores[i][0]
                score = self.high_scores[i][1]
                self.game.draw_text(
                    f"{i+1: >2} {name: <20} {score: >5}", 25, self.midx, self.midy + i*30)
        pygame.display.update()
        self._reset_keys()

    def show_menu(self):
        """Näyttää High Scores ikkunan
        """
        self.run_menu = True
        while self.run_menu:
            self._check_menu_events()
            self._check_input()
            self._blit_screen()

    def _check_input(self):
        if self.esc_key:
            self.game.curr_menu = self.game.main_menu
            self.run_menu = False


class ControlsMenu(Menu):
    def __init__(self, game):
        super().__init__(game)

    def _blit_screen(self):
        self.game.window.blit(self.game.background_image, (0, 0))
        self.game.draw_text("Controls", 45, self.midx, self.midy - 100)
        self.game.draw_text("UP".ljust(
            5) + " Accelerate".ljust(22), 25, self.midx, self.midy + 30)
        self.game.draw_text("LEFT".ljust(
            5) + " Rotate to left".ljust(22), 25, self.midx, self.midy + 60)
        self.game.draw_text("RIGHT".ljust(
            5) + " Rotate right".ljust(22), 25, self.midx, self.midy + 90)
        self.game.draw_text("SPACE".ljust(
            5) + " Shoot".ljust(22), 25, self.midx, self.midy + 120)
        self.game.draw_text("M".ljust(
            5) + " Pause/unpause music".ljust(22), 25, self.midx, self.midy + 150)
        self.game.draw_text("N".ljust(
            5) + " Pause/unpause effects".ljust(22), 25, self.midx, self.midy + 180)
        self.game.draw_text("ESC".ljust(
            5) + " Move back in menus".ljust(22), 25, self.midx, self.midy + 210)
        self.game.draw_text("ENTER".ljust(
            5) + " Proceed in menus".ljust(22), 25, self.midx, self.midy + 240)
        pygame.display.update()
        self._reset_keys()

    def show_menu(self):
        """Näyttää Controls ikkunan
        """
        self.run_menu = True
        while self.run_menu:
            self._check_menu_events()
            self._check_input()
            self._blit_screen()

    def _check_input(self):
        if self.esc_key:
            self.game.soundplayer.play_click_effect()
            self.game.curr_menu = self.game.main_menu
            self.run_menu = False


class InputScoreMenu(Menu):
    def __init__(self, game, filename="high_scores.csv"):
        super().__init__(game)
        self.default_name = "Unnamed Captain Star"
        self.player_name = "Insert your name"
        self.name_accepted = True
        self.high_scores_repository = HighScoresRepository(filename)

    def _blit_screen(self):
        self.game.window.blit(self.game.background_image, (0, 0))
        self.game.draw_text("Your score", 40, self.midx, self.midy - 200)
        self.game.draw_text(f"{self.game.score} points",
                            40, self.midx, self.midy - 150)
        self.game.draw_text(self.player_name, 32, self.midx, self.midy)
        self.game.draw_text(
            "The max length of your name is 20 characters", 18, self.midx, self.game.height - 50)
        pygame.display.update()
        self._reset_keys()

    def show_menu(self):
        """Näyttää pelaajan nimen syöttämisestä vastaavan ikkunnan
        """
        self.run_menu = True
        while self.run_menu:
            self._check_menu_events()
            self._check_input()
            self._blit_screen()

    def _check_input(self):
        self.name_accepted = (0 < len(self.player_name) <=
                              20) and self.player_name != "Insert your name"
        if self.esc_key:
            self.player_name = self.default_name
            # self.game.soundplayer.stop_music()
            self.high_scores_repository.add_new_high_score(
                self.player_name, self.game.score)
            self.game.curr_menu = self.game.main_menu
            self.run_menu = False
        if self.enter_key:
            self.game.soundplayer.play_click_effect()
            if self.name_accepted:
                # self.game.soundplayer.stop_music()
                self.high_scores_repository.add_new_high_score(
                    self.player_name, self.game.score)
                self.game.curr_menu = self.game.main_menu
                self.run_menu = False

    def _check_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.esc_key = True
                if event.key == pygame.K_RETURN:
                    self.enter_key = True
                if event.key == pygame.K_BACKSPACE:
                    self.player_name = self.player_name[:-1]
                elif event.key != pygame.K_RETURN:
                    if self.player_name == "Insert your name":
                        self.player_name = event.unicode
                    elif len(self.player_name) < 20:
                        self.player_name += event.unicode


class PauseMenu(Menu):
    def __init__(self, game):
        super().__init__(game)
        self.state = "Resume game"
        self.offset = -250
        self.resumex, self.resumey = self.midx, self.midy + 50
        self.menux, self.menuy = self.midx, self.midy + 100
        self.pointer_rect.center = (self.resumex + self.offset, self.resumey)

    def _blit_screen(self):
        self.game.window.blit(self.game.background_image, (0, 0))
        self.game.draw_text("Game paused", 45, self.midx, self.midy - 50)
        self.game.draw_text("Resume game", 32, self.resumex, self.resumey)
        self.game.draw_text("Back to menu", 32, self.menux, self.menuy)
        self.game.window.blit(
            self.pointer, (self.pointer_rect.x, self.pointer_rect.y))
        pygame.display.update()
        self._reset_keys()

    def show_menu(self):
        """Näyttää pysäytys-ikkunan
        """
        self.run_menu = True
        while self.run_menu:
            self._check_menu_events()
            self._check_input()
            self._blit_screen()

    def _move_pointer(self):
        if self.down_key:
            self.game.soundplayer.play_move_effect()
            if self.state == "Resume game":
                self.pointer_rect.center = (
                    self.menux + self.offset, self.menuy)
                self.state = "Back to menu"
            elif self.state == "Back to menu":
                self.pointer_rect.center = (
                    self.resumex + self.offset, self.resumey)
                self.state = "Resume game"
        elif self.up_key:
            self.game.soundplayer.play_move_effect()
            if self.state == "Resume game":
                self.pointer_rect.center = (
                    self.menux + self.offset, self.menuy)
                self.state = "Back to menu"
            elif self.state == "Back to menu":
                self.pointer_rect.center = (
                    self.resumex + self.offset, self.resumey)
                self.state = "Resume game"

    def _check_input(self):
        self._move_pointer()
        if self.enter_key:
            self.game.soundplayer.play_click_effect()
            if self.state == "Resume game":
                self.game.playing = True
                self.game.curr_menu = self.game.main_menu
            elif self.state == "Back to menu":
                self.game.curr_menu = self.game.main_menu
            self.run_menu = False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                self.game.soundplayer.pause_music()
