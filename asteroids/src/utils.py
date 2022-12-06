import os
import random
import pygame
import pygame.freetype
from pygame.mixer import Sound
from pygame.math import Vector2

dirname = os.path.dirname(__file__)

def get_music_path(name):
    path = f"{dirname}/assets/sounds/{name}.mp3"
    return path

def load_image(name):
    path = f"{dirname}/assets/images/{name}.png"
    image = pygame.image.load(path)
    return image

def load_font(name):
    path = f"{dirname}/assets/font/{name}.otf"
    font_size = 60
    myfont = pygame.freetype.Font(path, font_size)
    return myfont

def load_sound(name):
    path = f"{dirname}/assets/sounds/{name}.mp3"
    return Sound(path)

def keep_on_screen(position, width, height):
    x_position, y_position = position
    return Vector2(x_position % width, y_position % height)

def randomize_position():
    return Vector2(random.randint(-10,10), random.randint(-10,10))

def randomize_movement(min_speed, max_speed):
    speed = random.randint(min_speed, max_speed)
    heading = random.randrange(0,360)
    return Vector2(speed, 0).rotate(heading)

def randomize_rotation():
    rotate_speed = random.randint(-2,2)
    return rotate_speed

def randomize_size(image):
    size_selector = random.choice([1,2,2,3])
    size = image.get_size()
    size_x = size[0]
    size_y = size[1]
    if size_selector == 1:
        scale = 0.5
    elif size_selector == 3:
        scale = 2
    else: scale = 1
    return pygame.transform.scale(image, (size_x * scale, size_y * scale))
