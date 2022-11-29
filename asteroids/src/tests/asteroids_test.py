import unittest
from game.asteroids import Asteroids
from utils import load_image
from sprites.spaceship import Spaceship
from index import main


class TestAsteroids(unittest.TestCase):
    def setUp(self):
        self.spaceship = Spaceship(80, 50, load_image("spaceship"))

    def test_spaceship_sprite_creates_correct_class(self):
        self.assertEqual(type(self.spaceship), Spaceship)


class TestSpaceship(unittest.TestCase):
    def setUp(self):
        self.spaceship = Spaceship(80, 50, load_image("spaceship"))

    def test_spaceship_stays_on_screen(self):
        self.spaceship.rect.y = 700
        self.spaceship.move_y()
        self.assertEqual(self.spaceship.rect.y, 0)


class TestIndex(unittest.TestCase):
    def setUp(self):
        self.game = Asteroids()

    def test_game_initialized_correctly(self):
        self.assertEqual((self.game.width, self.game.height), (800, 640))
