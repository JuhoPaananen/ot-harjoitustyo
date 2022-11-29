import os
import pygame

dirname = os.path.dirname(__file__)


def load_image(name):
    path = f"{dirname}/assets/{name}.png"
    image = pygame.image.load(path)
    return image
