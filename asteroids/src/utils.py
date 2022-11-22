import pygame
import os

dirname = os.path.dirname(__file__)

def load_image(name):
    image = pygame.image.load(os.path.join(dirname, "..", "assets", "{name}.png"))
    return image