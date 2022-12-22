import unittest
import pygame
from pygame import mixer
from pygame.math import Vector2
from services.asteroids import AsteroidsGame
from services.soundplayer import SoundPlayer
from utils import load_image
from entities.objects import FlyingObject, Asteroid, LargeAsteroid, MediumAsteroid, SmallAsteroid, Bullet, Player
from index import main

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.game = AsteroidsGame()
        self.game.spaceship = Player((self.game.width/2, self.game.height/2))

    def test_Player_stays_on_screen(self):
        self.game.spaceship.speed = Vector2(600, 400)
        self.game.spaceship.move(self.game.width, self.game.height)
        
        self.assertEqual(self.game.spaceship.position, Vector2(86, 16))

    def test_spaceship_doesnt_exceed_max_speed(self):
        self.game.spaceship.speed = Vector2(-12,15)
        self.game.spaceship.accelerate()

        self.assertTrue(self.game.spaceship.get_speed().x >= -10)
        self.assertTrue(self.game.spaceship.get_speed().y <= 10)
        

class TestBullet(unittest.TestCase):
    def setUp(self):
        self.game = AsteroidsGame()
        self.game.start_new_game()
        self.bullet_speed = Vector2(0,-1)

    def test_bullets_are_not_wrapped(self):
        bullet = Bullet((self.game.width/2, self.game.height/2), self.bullet_speed)
        self.game.spaceship.bullets.append(bullet)
        bullet.position = (self.game.width/2, self.game.height+2)
        self.game._run_game_logic()
        self.assertEqual(len(self.game.spaceship.bullets), 0)

    def test_bullets_are_removed_correctly(self):
        self.game.spaceship.bullets = []
        self.game.spaceship.position = (50, 50)
        bullet = Bullet((self.game.width/2, self.game.height/2), self.bullet_speed)
        bullet.position = (self.game.width/2, self.game.height/2)
        self.game.spaceship.bullets.append(bullet)
        self.game.asteroids.append(SmallAsteroid(bullet.get_position()))
        self.game._run_game_logic()
        self.assertEqual(len(self.game.spaceship.bullets), 0)