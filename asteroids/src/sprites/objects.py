import pygame
from pygame.math import Vector2
from pygame.transform import rotozoom
from utils import load_image, keep_on_screen, randomize_movement, randomize_rotation

UP = Vector2(0, -1)
ASTEROID_SPEED_MIN = 1
ASTEROID_SPEED_MAX = 2
PLAYER_HP = 3
LASTEROID_HP = 3
MASTEROID_HP = 2
SASTEROID_HP = 1

class FlyingObject():
    """Luokka, joka vastaa kaikkien lentävien objektien yhteisistä metodeista
    """
    def __init__(self, position, image: pygame.surface, speed):
        """Luokan konstruktori, joka alustaa yhteiset muuttujat

        Args:
            position (tuple): Lentävän objektin (x,y) sijainti tuplena
            image (pygame.surface): Lentävän objektin kuva surfacena
            speed (int): Lentävän objektin nopeus kokonaislukuna
        """
        super().__init__()
        self.position = Vector2(position)
        self.image = image
        self.speed = Vector2(speed)
        self.rect = image.get_rect()
        self.radius = self.image.get_width() / 2
        self.center = self.rect.center
        self.health = 0

    def move(self, width, height):
        """Vastaa lentävien objektien liikuttamisesta

        Args:
            width (int): Sallitun liikkumisalueen leveys
            height (int): Sallitun liikkumisalueen korkeus
        """
        self.position = keep_on_screen(self.position + self.speed, width, height)

    def draw(self, window):
        """Vastaa lentävien objektien piirtämisestä

        Args:
            window (surface): Pelialue, jolle objekti halutaan piirtää
        """
        draw_position = self.position - Vector2(self.rect.center)
        window.blit(self.image, draw_position)

    def get_health(self):
        """Palauttaa objektin energiapisteet

        Returns:
            int: Energiapisteet kokonaislukuna
        """
        return self.health

class Asteroid(FlyingObject):
    """Luokka, joka vastaa asteroidien toiminnallisuuksista

    Args:
        FlyingObject (_type_): Perii parent-luokkansa FlyingObject
    """
    def __init__(self, position):
        """Luokan konstrukstori

        Args:
            position (tuple): Sijainti (x,y) tuplena
        """
        super().__init__(
            position,
            load_image("asteroid"),
            randomize_movement(ASTEROID_SPEED_MIN, ASTEROID_SPEED_MAX))
        self.rotation = randomize_rotation()
        self.heading = Vector2(UP)
        self.size = None
        self.img_size = self.image.get_size()
        self.img_size_x = self.img_size[0]
        self.img_size_y = self.img_size[1]

    def collides_with(self, other_object):
        """Vastaa törmäyksien tarkastamisesta

        Args:
            other_object (surface): Objekti, jonka kanssa törmäys tarkistetaan

        Returns:
            Bool: Palauttaa totuusarvon onko törmäys
        """
        distance = self.position.distance_to(other_object.position)
        return distance < self.radius + other_object.radius

    def draw(self, window):
        """Vastaa asteroidien surfacen pyörittämisestä ja piirtämisestä

        Args:
            window (surface): Ikkuna, johon halutaan piirtää
        """
        self.heading.rotate_ip(self.rotation)
        angle = self.heading.angle_to(UP)
        rotated = rotozoom(self.image, angle, 1.0)
        rotated_size = Vector2(rotated.get_size())
        draw_position = self.position - rotated_size * 0.5
        window.blit(rotated, draw_position)

    def is_destroyed(self):
        """Tarkistaa tuhotaanko asteroidi

        Returns:
            Bool: Totuusarvo, onko asteroidi tuhoutunut
        """
        self.health -= 1
        return self.get_health() == 0

    def get_position(self):
        return self.position

    def get_size(self):
        return self.size

class LargeAsteroid(Asteroid):
    def __init__(self, position):
        super().__init__(position)
        self.health = 3
        self.size = 2
        self.image = pygame.transform.scale(
            self.image,
            (self.img_size_x * self.size, self.img_size_y * self.size))
        self.radius = self.image.get_width() / 2

class MediumAsteroid(Asteroid):
    def __init__(self, position):
        super().__init__(position)
        self.health = 2
        self.size = 1
        self.image = pygame.transform.scale(
            self.image,
            (self.img_size_x * self.size, self.img_size_y * self.size))
        self.radius = self.image.get_width() / 2

class SmallAsteroid(Asteroid):
    def __init__(self, position):
        super().__init__(position)
        self.health = 1
        self.size = 0.5
        self.image = pygame.transform.scale(
            self.image,
            (self.img_size_x * self.size, self.img_size_y * self.size))
        self.radius = self.image.get_width() / 2

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
