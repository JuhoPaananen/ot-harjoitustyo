import sys
import random
import pygame
import pygame.freetype
from pygame import mixer
from utils import (
    load_image,
    load_font,
    load_sound,
    randomize_position,
    get_music_path,
    randomize_size
)
from sprites.objects import (
    Player,
    Bullet,
    LargeAsteroid,
    MediumAsteroid,
    SmallAsteroid
)
from game.menu import MainMenu, PauseMenu

WHITE = (255, 255, 255)
WIDTH = 1028
HEIGHT = 768
SAFE_DISTANCE = 100
BULLETS = 3
BULLET_SPEED = 8

class AsteroidsGame:
    """Luokka, joka vastaa pelin logiikasta
    """
    def __init__(self):
        """Luokan konstruktori, joka alustaa pelin tarvitsemat muuttujat
        """
        pygame.mixer.pre_init(44100, -16, 4, 1024)
        pygame.init()
        pygame.freetype.init()
        mixer.init()
        self.width = WIDTH
        self.height = HEIGHT
        self.running = True
        self.playing = False
        self.is_gameover = False
        self.myfont = load_font("8-BIT WONDER.TTF")
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Asteroids project")
        self.background_image = pygame.transform.scale(
            load_image("milkyway"), (self.width, self.height))
        self.spaceship = None #Player((self.width/2,self.height/2))
        self.asteroids = []
        self.bullets = []
        self.score = None
        self.lives = None
        self.blaster_sound = load_sound("LaserBlast.mp3")
        self.blaster_sound.set_volume(0.5)
        self.explosion_sound = load_sound("explosion.mp3")
        self.crash_sound = load_sound("Crash.mp3")
        self.main_menu = MainMenu(self)
        self.pause_menu = PauseMenu(self)
        self.curr_menu = self.main_menu
        self.clock = pygame.time.Clock()

    def initialize_music(self):
        """Tuo pelin taustamusiikin käyttöön ja käynnistää sen soittamisen ikuisella loopilla
        """
        # Music Copyright Kidd2Will, used only as a part of a school project
        mixer.music.load(get_music_path("Fire_Aura"))
        mixer.music.set_volume(0.7)
        mixer.music.play(-1)

    def initialize_game(self):
        """Alustaa tarvittavat muuttujat uuteen pelisessioon /
        ylikirjoittaa muuttujat edellisen pelisession jälkeen
        """
        self.playing = True
        self.score = 0
        self.lives = 3
        self.spaceship = Player((self.width/2,self.height/2))
        self.asteroids = []
        for _ in range (10):
            self.asteroid_factory(True)

    def stats(self):
        """Kirjoittaa pelitilanteen tiedot peliruudulle
        """
        score_text = f"Score  {self.score}"
        lives_text = f"Lives  {self.lives}"
        lives_rect = self.myfont.get_rect(lives_text, size=32)
        lives_rect.topright = self.width - 4, 4
        self.myfont.render_to(self.window, (4, 4), score_text, WHITE, size=32)
        self.myfont.render_to(self.window, (lives_rect), lives_text, WHITE, size=32)

    def event_handler(self):
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
                    if mixer.music.get_busy():
                        mixer.music.pause()
                    else:
                        mixer.music.unpause()
                if self.spaceship and event.key == pygame.K_SPACE:
                    self.shoot()
                if self.is_gameover and event.key == pygame.K_RETURN:
                    self.playing = False
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

    def draw_game(self):
        """Piirtää peli-ikkunan tapahtumat
        """
        self.window.blit(self.background_image, (0, 0))
        for obj in self.get_flying_objects():
            obj.draw(self.window)
        self.stats()
        if self.is_gameover:
            self.draw_text("Game over", 64, self.width / 2, self.height / 2)
            self.draw_text("Press ENTER to return to menu",
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
        text_rect = self.myfont.get_rect(text, size = text_size)
        text_rect.center = (text_x, text_y)
        self.myfont.render_to(self.window, (text_rect), text, WHITE, size = text_size)

    def shoot(self):
        """Ampuu, eli luo uuden ammuksen peliin
        """
        bullet_speed = self.spaceship.heading * BULLET_SPEED + self.spaceship.speed
        if len(self.bullets) < BULLETS:
            self.bullets.append(Bullet(self.spaceship.position,bullet_speed))
            pygame.mixer.Sound.play(self.blaster_sound)

    def crash(self, asteroid):
        """Käsittelee pelaajan törmäyksen asteroidin kanssa

        Args:
            asteroid (Asteroid): Aluksen kanssa törmännyt asteroidi, joka poistetaan pelistä
        """
        flash_speed = 10
        counter = 0
        if asteroid in self.asteroids:
            self.asteroids.remove(asteroid)
        pygame.mixer.Sound.play(self.crash_sound)
        while counter <= flash_speed:
            self.window.fill(WHITE)
            pygame.display.flip()
            counter += 1

    def hit(self, bullet, asteroid):
        """Käsittelee ammuksien osumat asteroidien kanssa

        Args:
            bullet (Bullet): Ammus, jolla tullut osuma, poistetaan pelistä
            asteroid (Asteroid): Asteroidi, johon on osuttu, poistetaan tai hajoitetaan pienemmäksi
        """
        if bullet in self.bullets:
            self.bullets.remove(bullet)
        if asteroid.is_destroyed():
            self.score += 1
            pygame.mixer.Sound.play(self.explosion_sound)
            if asteroid in self.asteroids:
                self.asteroids.remove(asteroid)
            if asteroid.get_size() == 2:
                for _ in range(3):
                    self.asteroids.append(MediumAsteroid(asteroid.get_position()))
            elif asteroid.get_size() == 1:
                for _ in range(2):
                    self.asteroids.append(SmallAsteroid(asteroid.get_position()))

    def run_game_logic(self):
        """Huolehtii pelilogiikasta
        """
        for obj in self.get_flying_objects():
            obj.move(self.width, self.height)

        if not self.spaceship:
            return

        for asteroid in self.asteroids:
            if asteroid.collides_with(self.spaceship):
                self.lives -= 1
                if self.lives > 0:
                    self.crash(asteroid)
                else:
                    self.crash(asteroid)
                    self.spaceship = None
                    self.is_gameover = True
                break

        for bullet in self.bullets[:]:
            if not self.window.get_rect().collidepoint(bullet.position):
                self.bullets.remove(bullet)
            for asteroid in self.asteroids:
                if asteroid.collides_with(bullet):
                    self.hit(bullet, asteroid)

    def get_flying_objects(self):
        """Palauttaa pelissä olevat objektit

        Returns:
            list: Lista asteroideista, ammuksista ja pelaajan aluksesta
        """
        flying_objects = [*self.asteroids, *self.bullets]
        if self.spaceship:
            flying_objects.append(self.spaceship)
        return flying_objects

    def asteroid_factory(self, init_phase=False):
        """Luo satunnaisen kokoisia asteroideja satunnaisiin
        sijainteihin satunnaisella todennäköisyydellä

        Args:
            init_phase (bool, optional): Metodia kutsuttaessa vapaaehtoinen
                                        True-argumentti ohittaa satunnaisen todennäköisyyden
        """
        if self.is_gameover:
            return
        if not init_phase:
            lottery = random.randrange(0,700)
            if lottery > 5:
                return
        while True:
            position = randomize_position()
            if position.distance_to(self.spaceship.position) > SAFE_DISTANCE:
                break
        asteroid_size = randomize_size()
        if asteroid_size == "L":
            new_asteroid = LargeAsteroid(position)
        elif asteroid_size == "M":
            new_asteroid = MediumAsteroid(position)
        else:
            new_asteroid = SmallAsteroid(position)
        self.asteroids.append(new_asteroid)

    def gameloop(self):
        """Pyörittää peliä eteenpäin
        """
        while self.playing:
            self.asteroid_factory()
            self.event_handler()
            self.run_game_logic()
            self.draw_game()
            self.clock.tick(60)
