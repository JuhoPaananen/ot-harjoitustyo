import unittest
from Asteroids import Asteroids
from sprites.spaceship import Spaceship

class TestAsteroids(unittest.TestCase):
    def setUp(self):
        self.spaceship = Spaceship(80,50)
        Asteroids.TESTING = True
    
    def test_spaceship_sprite_creates_correct_class(self):     
        self.assertEqual(type(self.spaceship), Spaceship)