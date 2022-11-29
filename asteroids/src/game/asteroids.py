import sys
import pygame
from sprites.spaceship import Spaceship
from utils import load_image


class Asteroids:
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 640
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Asteroids project")
        self.background_image = load_image("milkyway")
        self.spaceship = Spaceship(
            self.width, self.height, load_image("spaceship"))
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.spaceship)
        self.to_up = False
        self.to_down = False

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.to_up = True
                if event.key == pygame.K_DOWN:
                    self.to_down = True
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.to_up = False
                if event.key == pygame.K_DOWN:
                    self.to_down = False

    def move(self):
        self.spaceship.move_y()
        if self.to_up:
            self.spaceship.accelerate()
        if self.to_down:
            self.spaceship.brake()

    def draw(self):
        self.all_sprites.update()
        self.window.fill((0, 0, 0))
        self.window.blit(self.background_image, (0, 0))
        self.all_sprites.draw(self.window)
        pygame.display.flip()

    def gameloop(self):
        while True:
            self.event_handler()
            self.move()
            self.draw()
            # print(self.spaceship.speed)
            self.clock.tick(60)
