import pygame
from utils import load_image
from pygame.math import Vector2 
import math
import os

dirname = os.path.dirname(__file__)


class Spaceship(pygame.sprite.Sprite):

    ROTATE_SPEED = 3

    def __init__(self, x, y):
        super().__init__()
        #self.image = load_image("spaceship")
        self.image = pygame.image.load(os.path.join(dirname, "..", "assets", "spaceship.png"))
                
        self.rect = self.image.get_rect()
        self.angle = math.radians(0)
        
    def moveRight(self, velocity):
        self.rect.x += velocity
    
    def moveLeft(self, velocity):
        self.rect.x -= velocity

    def moveUp(self, velocity):
        self.rect.y += velocity

    def moveDown(self, velocity):
        self.rect.y -= velocity

    def moveX(self, velocity):
        self.rect.x += velocity

    def moveY(self, velocity):
        self.rect.y += velocity

    def rotateLeft(self):
        self.image = pygame.transform.rotate(self.image, 3)
        #self.angle += self.ROTATE_SPEED

    def rotateRight(self):
        self.image = pygame.transform.rotate(self.image, -3)
        #self.angle -= self.ROTATE_SPEED