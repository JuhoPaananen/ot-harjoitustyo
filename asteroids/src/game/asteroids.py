import sys
import random
import pygame
import pygame.freetype
from pygame import mixer
from utils import load_image, load_font, load_sound, randomize_position, get_music_path
from sprites.objects import Player, Asteroid, Bullet

WHITE = (255, 255, 255)
WIDTH = 1028
HEIGHT = 768
SAFE_DISTANCE = 100
BULLETS = 3
BULLET_SPEED = 7

class AsteroidsGame:
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 1024)
        pygame.init()
        pygame.freetype.init()
        mixer.init()
        self._initialize_game()
        self.myfont = load_font("Connection")
        self._initialize_sounds()
        self.score = 0
        self.lives = 3
        self.is_gameover = False

    def _initialize_sounds(self):
        self.blaster_sound = load_sound("LaserBlast")
        self.explosion_sound = load_sound("explosion")
        self.crash_sound = load_sound("Crash")
        # Music Copyright Kidd2Will, used only as a part of a school project
        mixer.music.load(get_music_path("Fire_Aura"))
        mixer.music.set_volume(0.7)
        mixer.music.play(-1)

    def _initialize_game(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Asteroids project")
        self.background_image = pygame.transform.scale(
            load_image("milkyway"), (self.width, self.height))
        self.is_gameover = False
        self.spaceship = Player((self.width/2,self.height/2))
        self.asteroids = []
        for i in range (10):
            self._asteroid_factory(True)
        self.bullets = []
        self.clock = pygame.time.Clock()


    def stats(self):
        self.myfont.render_to(self.window, (4, 4), f"Score: {self.score}", WHITE, size=32)
        self.myfont.render_to(
            self.window, (self.width - 120, 4), f"Lives: {self.lives}", WHITE, size=32)

    def game_over(self):
        text = "GAME OVER!"
        text_rect = self.myfont.get_rect(text, size = 64)
        text_rect.center = self.window.get_rect().center
        text2 = "<Press ESC to exit>"
        text2_rect = self.myfont.get_rect(text2, size = 32)
        text2_rect.center = self.window.get_rect().center
        text2_rect.centery += 50
        self.myfont.render_to(self.window, (text_rect), text, WHITE, size = 64)
        self.myfont.render_to(self.window, (text2_rect), text2, WHITE, size = 32)

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if self.spaceship and event.key == pygame.K_SPACE:
                    self.shoot()

        keys_pressed = pygame.key.get_pressed()

        if self.spaceship:
            if keys_pressed[pygame.K_RIGHT]:
                self.spaceship.rotate_right()
            if keys_pressed[pygame.K_LEFT]:
                self.spaceship.rotate_left()
            if keys_pressed[pygame.K_UP]:
                self.spaceship.accelerate()

    def draw(self):
        self.window.fill((0, 0, 0))
        self.window.blit(self.background_image, (0, 0))
        for obj in self._get_flying_objects():
            obj.draw(self.window)
        self.stats()
        if self.is_gameover:
            self.game_over()
        pygame.display.flip()

    def shoot(self):
        bullet_speed = self.spaceship.heading * BULLET_SPEED + self.spaceship.speed
        if len(self.bullets) < BULLETS:
            self.bullets.append(Bullet(self.spaceship.position,bullet_speed))
            pygame.mixer.Sound.play(self.blaster_sound)

    def crash(self, asteroid):
        if asteroid in self.asteroids:
            self.asteroids.remove(asteroid)
        self.clock.tick(30)
        self.window.fill(WHITE)
        self.clock.tick(60)
        pygame.display.flip()
        pygame.mixer.Sound.play(self.crash_sound)

    def hit(self, bullet, asteroid):
        if bullet in self.bullets:
            self.bullets.remove(bullet)
        if asteroid in self.asteroids:
            self.asteroids.remove(asteroid)
        self.score += 1
        pygame.mixer.Sound.play(self.explosion_sound)

    def proceed(self):
        for obj in self._get_flying_objects():
            obj.move(self.width, self.height)

        if not self.spaceship:
            return

        for asteroid in self.asteroids:
            if asteroid.check_collision(self.spaceship):
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
                if asteroid.check_collision(bullet):
                    self.hit(bullet, asteroid)

    def _get_flying_objects(self):
        flying_objects = [*self.asteroids, *self.bullets]
        if self.spaceship:
            flying_objects.append(self.spaceship)
        return flying_objects

    def _asteroid_factory(self, init_phase=False):
        if self.is_gameover:
            return
        if not init_phase:
            lottery = random.randrange(0,700)
            if lottery > 10:
                return
        while True:
            position = randomize_position()
            if position.distance_to(self.spaceship.position) > SAFE_DISTANCE:
                break
        self.asteroids.append(Asteroid(position))

    def gameloop(self):
        while True:
            self._asteroid_factory()
            self.event_handler()
            self.proceed()
            self.draw()
            self.clock.tick(60)
