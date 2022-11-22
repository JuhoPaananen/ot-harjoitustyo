import pygame
from pygame.locals import *
from sprites.spaceship import Spaceship
#from utils import load_image
import os

dirname = os.path.dirname(__file__)

class Asteroids:
    
    pygame.init()

    TESTING = True
    WIDTH = 800
    HEIGHT = 640
    CLOCK = pygame.time.Clock()
    MOVESPEED = 10
  
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Asteroids project")

    #background_image = load_image("milkyway")
    background_image = pygame.image.load(os.path.join(dirname, "assets", "milkyway.png"))
    spaceship = Spaceship(80,50)

    x = WIDTH/2 - spaceship.rect.centerx
    y = HEIGHT/2 - spaceship.rect.centery

    spaceship.rect.x = x
    spaceship.rect.y = y
    all_sprites = pygame.sprite.Group()
    all_sprites.add(spaceship)

    to_right = False
    to_left = False
    to_up = False
    to_down = False

    while True and not TESTING:
        for event in pygame.event.get():
            """
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    to_left = True
                if event.key == pygame.K_RIGHT:
                    to_right = True
                if event.key == pygame.K_UP:
                    to_up = True
                if event.key == pygame.K_DOWN:
                    to_down = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    to_left = False
                if event.key == pygame.K_RIGHT:
                    to_right = False
                if event.key == pygame.K_UP:
                    to_up = False
                if event.key == pygame.K_DOWN:
                    to_down = False
            """
                    
            if event.type == pygame.QUIT:
                exit()
        
        """
        if to_left:
            X_VELOCITY -= ACCELERATION
        if to_right:
            X_VELOCITY += ACCELERATION
        if to_up:
            Y_VELOCITY -= ACCELERATION
        if to_down:
            Y_VELOCITY += ACCELERATION
        
            
        
        x += X_VELOCITY
        y += Y_VELOCITY
      
        if x > WIDTH:
            x = 0
        if x < 0:
            x = WIDTH
        if y > HEIGHT:
            y = 0
        if y < 0:
            y = HEIGHT
        """

        spaceship.moveRight(10)
        if spaceship.rect.x > WIDTH:
            spaceship.rect.x = 0

        all_sprites.update()
        window.fill((0, 0, 0))
        window.blit(background_image, (0, 0))
        all_sprites.draw(window)
        
        pygame.display.flip()
            
        CLOCK.tick(60)