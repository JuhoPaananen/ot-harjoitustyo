import pygame
from pygame.math import Vector2
from pygame.transform import rotozoom
from utils import load_image, keep_on_screen, randomize_movement, randomize_size, randomize_rotation

UP = Vector2(0, -1)
ASTEROID_SPEED_MIN = 1
ASTEROID_SPEED_MAX = 2

class FlyingObject():
    def __init__(self, position, image: pygame.surface, speed):
        super().__init__()
        self.position = Vector2(position)
        self.image = image
        self.speed = Vector2(speed)
        self.rect = image.get_rect()
        self.radius = self.image.get_width() / 2
        self.center = self.rect.center

    def move(self, width, height):
        self.position = keep_on_screen(self.position + self.speed, width, height)

    def draw(self, window):
        draw_position = self.position - Vector2(self.rect.center)
        window.blit(self.image, draw_position)

class Asteroid(FlyingObject):
    def __init__(self, position):
        super().__init__(
            position,
            randomize_size(load_image("asteroid")),
            randomize_movement(ASTEROID_SPEED_MIN, ASTEROID_SPEED_MAX))
        self.rotation = randomize_rotation()
        self.heading = Vector2(UP)

    def check_collision(self, other_object):
        distance = self.position.distance_to(other_object.position)
        return distance < self.radius + other_object.radius

    def draw(self, window):
        self.heading.rotate_ip(self.rotation)
        angle = self.heading.angle_to(UP)
        rotated = rotozoom(self.image, angle, 1.0)
        rotated_size = Vector2(rotated.get_size())
        draw_position = self.position - rotated_size * 0.5
        window.blit(rotated, draw_position)

class Bullet(FlyingObject):
    def __init__(self, position, speed):
        super().__init__(position, pygame.transform.scale(load_image("bullet"), (25,25)), speed)

    def move(self, width, height):
        self.position = self.position + self.speed


class Player(FlyingObject):

    ROTATE_SPEED = 4
    MAX_SPEED = 10
    ACCELERATION = 0.3
    BRAKING = 0.1

    def __init__(self, position):
        self.heading = Vector2(UP)
        super().__init__(position, load_image("spaceship"), Vector2(0))

    def rotate_left(self):
        angle = -self.ROTATE_SPEED
        self.heading.rotate_ip(angle)

    def rotate_right(self):
        angle = self.ROTATE_SPEED
        self.heading.rotate_ip(angle)

    def accelerate(self):
        self.speed += self.heading * self.ACCELERATION
        if self.speed.x > self.MAX_SPEED:
            self.speed.x = self.MAX_SPEED
        if self.speed.x < -self.MAX_SPEED:
            self.speed.x = -self.MAX_SPEED
        if self.speed.y > self.MAX_SPEED:
            self.speed.y = self.MAX_SPEED
        if self.speed.y < -self.MAX_SPEED:
            self.speed.y = -self.MAX_SPEED

    def draw(self, window):
        angle = self.heading.angle_to(UP)
        rotated = rotozoom(self.image, angle, 1.0)
        rotated_size = Vector2(rotated.get_size())
        draw_position = self.position - rotated_size * 0.5
        window.blit(rotated, draw_position)
