import os
import random
import pygame
import pygame.freetype
from pygame.mixer import Sound
from pygame.math import Vector2

dirname = os.path.dirname(__file__)

def get_music_path(name):
    """Palauttaa taustamuusikin absoluutisen sijainnin assets/sounds kansiosta

    Args:
        name (str): Haettavan tiedoston nimi muodossa "nimi.tiedostopääte"

    Returns:
        path: Haettavan tiedoston absoluuttinen sijainti
    """
    path = f"{dirname}/assets/sounds/{name}.mp3"
    return path

def load_image(name):
    """Lataa haettavan kuvan assets/images suhteellisesta sijainnista

    Args:
        name (str): Haettavan kuvan nimi muodossa "tiedostonimi"

    Returns:
        Pygame.Surface: Haettava kuva Surface-muodossa
    """
    path = f"{dirname}/assets/images/{name}.png"
    image = pygame.image.load(path)
    return image

def load_font(name):
    """Lataa fontin käyttöön assets/font suhteellisesta sijainnista

    Args:
        name (str): Haettavan fontin nimi muodossa "nimi.tiedostopääte"

    Returns:
        freetype.Font: Haettu fontti
    """
    path = f"{dirname}/assets/font/{name}"
    font_size = 60
    myfont = pygame.freetype.Font(path, font_size)
    return myfont

def load_sound(name):
    """Lataa haettavan äänitehosteen suhteellisesta sijainnista assets/sounds

    Args:
        name (str): Haettavan äänitehosteen nimi muodossa "nimi.tiedostopääte"

    Returns:
        mixer.Sound: Äänitehoste mixer.Sound muodossa
    """
    path = f"{dirname}/assets/sounds/{name}"
    return Sound(path)

def keep_on_screen(position, width, height):
    """Muodostaa uuden vektorisijainnin mikäli annetut rajat ylitetään /
    pitää sijainnin pelialueella

    Args:
        position (tuple): Sijainti (asteroidin tai aluksen), jota verrataan rajoihin
        width (int): Pelialueen / rajatun alueen leveys
        height (int): Pelialuuen / rajatun alueen korkeus

    Returns:
        pygame.Vector2: Vektori, joka on pelialuuen sisällä
    """
    x_position, y_position = position
    return Vector2(x_position % width, y_position % height)

def randomize_position():
    """Luo satunnaisen sijainnin pelialueen rajoilla

    Returns:
        pygame.Vector2: Satunnainen vektorisijainti pelialuuen rajalla
    """
    return Vector2(random.randint(-10,10), random.randint(-10,10))

def randomize_movement(min_speed, max_speed):
    """Luo satunnaisen vektorin

    Args:
        min_speed (int): Luotavan vektorin minimipituus
        max_speed (int): Luotavan vektorin maksimipituus

    Returns:
        pygame.Vector2: Vektori, jolla on satunnainen (min,max) välillä
                        oleva pituus ja suunta välillä (0,360)
    """
    speed = random.randint(min_speed, max_speed)
    heading = random.randrange(0,360)
    return Vector2(speed, 0).rotate(heading)

def randomize_rotation():
    """Luo satunnaisen pyörimisliikkeen

    Returns:
        int: Satunnainen pyörimisvauhti
    """
    rotate_speed = random.randint(-3,3)
    return rotate_speed

def randomize_size():
    """Arpoo uuden asteroidin koon

    Returns:
        str: Satunnainen koko ilmoitettuna "S,M,L" merkkinä
    """
    return random.choice(["S", "M", "M", "M", "L"])
