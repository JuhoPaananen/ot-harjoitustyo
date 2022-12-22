import sys
import random
import pygame
import pygame.freetype
from services.soundplayer import SoundPlayer
from utils import (
    load_image,
    load_font,
    randomize_position,
    randomize_size
)
from entities.objects import (
    Player,
    LargeAsteroid,
    MediumAsteroid,
    SmallAsteroid
)
from ui.menus import (
    MainMenu,
    PauseMenu,
    InputScoreMenu
)

WHITE = (255, 255, 255)
SCREEN_WIDTH = 1028
SCREEN_HEIGHT = 768
SAFE_DISTANCE = 100

class AsteroidsGame:
    """Luokka, joka vastaa pelin logiikasta
    """

    def __init__(self):
        """Luokan konstruktori, joka alustaa pelin tarvitsemat muuttujat
        """
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.running = True
        self.playing = False
        self.is_gameover = False
        self.myfont = load_font("prstartk.ttf")
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Asteroids project")
        self.background_image = pygame.transform.scale(
            load_image("milkyway"), (self.width, self.height))
        self.spaceship = None
        self.asteroids = []
        self.score = None
        self.main_menu = MainMenu(self)
        self.pause_menu = PauseMenu(self)
        self.curr_menu = self.main_menu
        self.clock = pygame.time.Clock()
        self.soundplayer = SoundPlayer()

    def _initialize_game(self):
        """Alustaa tarvittavat muuttujat uuteen pelisessioon /
        ylikirjoittaa muuttujat edellisen pelisession jälkeen
        """
        self.soundplayer.play_music()
        self.playing = True
        self.score = 0
        self.spaceship = Player((self.width/2, self.height/2))
        self.asteroids = []
        for _ in range(10):
            self._create_asteroids(True)

    def _draw_stats(self):
        """Kirjoittaa pelitilanteen tiedot peliruudulle
        """
        if self.spaceship:
            health = self.spaceship.get_health()
        else:
            health = 0
        score_text = f"Score  {self.score}"
        lives_text = f"Health  {health}"
        lives_rect = self.myfont.get_rect(lives_text, size=32)
        lives_rect.topright = self.width - 4, 4
        self.myfont.render_to(self.window, (4, 4), score_text, WHITE, size=32)
        self.myfont.render_to(self.window, (lives_rect),
                              lives_text, WHITE, size=32)

    def _handle_key_input(self):
        """Käsittelee pelaajan syötteet
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and not self.is_gameover:
                    self.playing = False
                    self.curr_menu = self.pause_menu
                if event.key == pygame.K_m:
                    self.soundplayer.pause_music()
                if event.key == pygame.K_n:
                    self.soundplayer.turn_sounds_on_off()
                if self.spaceship and event.key == pygame.K_SPACE:
                    if self.spaceship.shoot():
                        self.soundplayer.play_blaster_effect()
                if self.is_gameover and event.key == pygame.K_RETURN:
                    self.playing = False
                    self.curr_menu = InputScoreMenu(self)
                    self.curr_menu.run_menu = True
                    self.is_gameover = False

        keys_pressed = pygame.key.get_pressed()

        if self.spaceship:
            if keys_pressed[pygame.K_RIGHT]:
                self.spaceship.rotate_right()
            if keys_pressed[pygame.K_LEFT]:
                self.spaceship.rotate_left()
            if keys_pressed[pygame.K_UP]:
                self.spaceship.accelerate()

    def _draw_game(self):
        """Piirtää peli-ikkunan tapahtumat
        """
        self.window.blit(self.background_image, (0, 0))
        for obj in self._get_flying_objects():
            obj.draw(self.window)
        self._draw_stats()
        if self.is_gameover:
            self.draw_text("Game over", 64, self.width / 2, self.height / 2)
            self.draw_text("Press ENTER to continue",
                           24, self.width / 2, self.height / 2 + 50)
        pygame.display.flip()

    def draw_text(self, text, text_size, text_x, text_y):
        """Piirtää tekstit pyydetyille paikoilleen ikkunassa

        Args:
            text (str): Piirrettävä teksti
            text_size (int): Fonttikoko
            text_x (int): Piirrettävän tekstin sijainti x-akselilla
            text_y (int): Piirrettävän tekstin sijainti y-akselilla
        """
        text_rect = self.myfont.get_rect(text, size=text_size)
        text_rect.center = (text_x, text_y)
        self.myfont.render_to(self.window, (text_rect),
                              text, WHITE, size=text_size)

    def start_new_game(self):
        """Alustaa uuden pelitapahtuman
        """
        self._initialize_game()

    def _crash(self, asteroid):
        """Käsittelee pelaajan törmäyksen asteroidin kanssa

        Args:
            asteroid (Asteroid): Aluksen kanssa törmännyt asteroidi, joka poistetaan pelistä
        """
        flash_speed = 10
        counter = 0
        if asteroid in self.asteroids:
            self.asteroids.remove(asteroid)
        self.soundplayer.play_crash_effect()
        while counter <= flash_speed:
            self.window.fill(WHITE)
            pygame.display.flip()
            counter += 1

    def _handle_bullet_hit(self, bullet, asteroid):
        """Käsittelee ammuksien osumat asteroidien kanssa

        Args:
            bullet (Bullet): Ammus, jolla tullut osuma, poistetaan pelistä
            asteroid (Asteroid): Asteroidi, johon on osuttu, poistetaan tai hajoitetaan pienemmäksi
        """

        if bullet in self.spaceship.get_bullets():
            self.spaceship.remove_bullet(bullet)
        if asteroid.is_destroyed():
            self.score += 1
            self.soundplayer.play_explosion_effect()
            if asteroid in self.asteroids:
                self.asteroids.remove(asteroid)
            if asteroid.get_size() == 2:
                for _ in range(3):
                    self.asteroids.append(
                        MediumAsteroid(asteroid.get_position()))
            elif asteroid.get_size() == 1:
                for _ in range(2):
                    self.asteroids.append(
                        SmallAsteroid(asteroid.get_position()))

    def _run_game_logic(self):
        """Huolehtii pelilogiikasta
        """
        for obj in self._get_flying_objects():
            obj.move(self.width, self.height)

        if not self.spaceship:
            return

        for asteroid in self.asteroids:
            if asteroid.collides_with(self.spaceship):
                if self.spaceship.is_destroyed():
                    self._crash(asteroid)
                    self.spaceship = None
                    self.is_gameover = True
                else:
                    self._crash(asteroid)
                break

        if self.spaceship:
            for bullet in self.spaceship.get_bullets()[:]:
                if not self.window.get_rect().collidepoint(bullet.get_position()):
                    self.spaceship.remove_bullet(bullet)
                for asteroid in self.asteroids:
                    if asteroid.collides_with(bullet):
                        self._handle_bullet_hit(bullet, asteroid)

    def _get_flying_objects(self):
        """Palauttaa pelissä olevat objektit

        Returns:
            list: Lista asteroideista, ammuksista ja pelaajan aluksesta
        """
        flying_objects = [*self.asteroids]
        if self.spaceship:
            flying_objects.append(self.spaceship)
            for bullet in self.spaceship.get_bullets():
                flying_objects.append(bullet)
        return flying_objects

    def _create_asteroids(self, init_phase=False):
        """Luo satunnaisen kokoisia asteroideja satunnaisiin
        sijainteihin satunnaisella todennäköisyydellä

        Args:
            init_phase (bool, optional): Metodia kutsuttaessa vapaaehtoinen
                                        True-argumentti ohittaa satunnaisen todennäköisyyden
        """
        if self.is_gameover:
            return
        if not init_phase:
            if random.randrange(0, 700) > 5:
                return
        while True:
            position = randomize_position()
            if position.distance_to(self.spaceship.get_position()) > SAFE_DISTANCE:
                break
        asteroid_size = randomize_size()
        if asteroid_size == "L":
            new_asteroid = LargeAsteroid(position)
        elif asteroid_size == "M":
            new_asteroid = MediumAsteroid(position)
        else:
            new_asteroid = SmallAsteroid(position)
        self.asteroids.append(new_asteroid)

    def gameloop(self, testing=False):
        """Pyörittää peliä eteenpäin
        """
        while self.playing:
            self._create_asteroids()
            self._handle_key_input()
            self._run_game_logic()
            self._draw_game()
            self.clock.tick(60)
            if testing:
                self.playing = False
