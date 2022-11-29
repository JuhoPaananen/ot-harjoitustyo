import pygame


class Spaceship(pygame.sprite.Sprite):

    ROTATE_SPEED = 3
    MAX_SPEED = 10
    ACCELERATION = 0.5
    BRAKING = 0.1
    UP = (0, -1)

    def __init__(self, width, height, image: pygame.surface):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = width/2 - self.rect.centerx
        self.rect.y = height/2 - self.rect.centery
        self.speed = 0
        self.height = height

    def accelerate(self):
        self.speed += self.ACCELERATION
        self.speed = min(self.speed, self.MAX_SPEED)

    def brake(self):
        self.speed -= self.BRAKING
        self.speed = max(self.speed, 0)

    def move_y(self):
        self.rect.y -= self.speed
        self.rect.y = self.rect.y % self.height
