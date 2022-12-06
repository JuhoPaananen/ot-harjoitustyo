import unittest
from pygame.math import Vector2
from game.asteroids import AsteroidsGame
from utils import load_image
from sprites.objects import FlyingObject, Asteroid, Bullet, Player
from index import main


class TestAsteroidsGame(unittest.TestCase):
    def setUp(self):
        self.game = AsteroidsGame()
        self.game.asteroids = []
        self.game.asteroids.append(Asteroid((self.game.spaceship.position)))

    def test_spaceship_crash_with_asteroids(self):
        self.game.proceed()
        self.assertEqual(self.game.lives, 2)
        self.assertEqual(len(self.game.asteroids), 0)

    def test_game_over_recognized(self):
        self.game.lives = 1
        self.game.proceed()
        self.assertEqual(self.game.is_gameover, True)

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.game = AsteroidsGame()

    def test_Player_stays_on_screen(self):
        self.game.spaceship.speed = Vector2(600,400)
        self.game.spaceship.move(self.game.width, self.game.height)
        self.assertEqual(self.game.spaceship.position, Vector2(86,16))

class TestBullet(unittest.TestCase):

    def test_bullets_are_not_wrapped(self):
        pass

    def test_bullets_are_removed_correctly(self):
        pass


class TestIndex(unittest.TestCase):
    def setUp(self):
        self.game = AsteroidsGame()

    def test_game_initialized_correctly(self):
        self.assertEqual((self.game.width, self.game.height), (1028, 768))
