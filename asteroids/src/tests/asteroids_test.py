import unittest
import pygame
from pygame import mixer
from pygame.math import Vector2
from services.asteroids import AsteroidsGame
from services.soundplayer import SoundPlayer
from utils import load_image
from entities.objects import FlyingObject, Asteroid, LargeAsteroid, MediumAsteroid, SmallAsteroid, Bullet, Player
from index import main


class TestAsteroidsGame(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.game = AsteroidsGame()

    def test_one_live_reduced_when_crashed_with_asteroid(self):
        self.game.lives = 3
        self.game.spaceship = Player((self.game.width/2, self.game.height/2))
        self.game.asteroids.append(Asteroid((self.game.spaceship.position)))
        self.game.run_game_logic()
        
        self.assertEqual(self.game.lives, 2)

    def test_asteroid_is_destroyed_when_crashed_with_player(self):
        self.game.lives = 2
        self.game.spaceship = Player((self.game.width/2, self.game.height/2))
        self.game.asteroids.append(Asteroid((self.game.spaceship.position)))
        self.game.run_game_logic()
        
        self.assertEqual(len(self.game.asteroids), 0)

    def test_game_over_recognized(self):
        self.game.lives = 1
        self.game.spaceship = Player((self.game.width/2, self.game.height/2))
        self.game.asteroids.append(Asteroid((self.game.spaceship.position)))
        self.game.run_game_logic()
        
        self.assertEqual(self.game.is_gameover, True)

    def test_music_can_be_loaded_successfully(self):
        self.game.soundplayer.play_music()
        
        self.assertTrue(mixer.music.get_busy())

    def test_lives_set_correctly_when_game_initialized(self):
        self.game.lives = 2
        self.game.initialize_game()
        
        self.assertEqual(self.game.lives, 3)

    def test_player_initialized_when_game_initialized(self):
        self.game.initialize_game()
        self.assertIsNotNone(self.game.spaceship)

    def test_correct_amount_of_asteroids_created_when_game_initialized(self):
        self.game.initialize_game()
        
        self.assertEqual(len(self.game.asteroids), 10)

    def test_mode_is_set_to_playing_when_game_initialized(self):
        self.game.initialize_game()
        
        self.assertEqual(self.game.playing, True)

    def test_bullet_is_created_when_shot(self):
        self.game.initialize_game()
        self.game.shoot()
        
        self.assertEqual(len(self.game.bullets), 1)

    def test_bullet_is_not_created_if_all_bullets_used(self):
        self.game.initialize_game()
        for _ in range(4):
            self.game.shoot()
        
        self.assertEqual(len(self.game.bullets), 3)

    def test_all_flying_objects_are_collected(self):
        self.game.initialize_game()
        self.game.bullets.append(Bullet((self.game.width/2,self.game.height/2), 0))
        
        self.assertEqual(len(self.game.get_flying_objects()), 12)

    def test_hit_when_asteroid_destroyed_increases_score(self):
        self.game.initialize_game()
        self.game.spaceship.position = (50,50)
        self.game.asteroids.append(SmallAsteroid((self.game.width/2, self.game.height/2)))
        self.game.bullets.append(Bullet((self.game.width/2,self.game.height/2), 0))
        self.game.run_game_logic()
        
        self.assertEqual(self.game.score, 1)


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.game = AsteroidsGame()
        self.game.spaceship = Player((self.game.width/2, self.game.height/2))

    def test_Player_stays_on_screen(self):
        self.game.spaceship.speed = Vector2(600,400)
        self.game.spaceship.move(self.game.width, self.game.height)
        self.assertEqual(self.game.spaceship.position, Vector2(86,16))
"""
class TestBullet(unittest.TestCase):
    def setUp(self):
        self.game = AsteroidsGame()
        self.bullet_speed = Vector2(0,-1)
        self.bullet = Bullet((self.game.width/2, self.game.height/2), self.bullet_speed)
        #self.game.bullets.append(self.bullet)

    def test_bullets_are_not_wrapped(self):
        self.bullet.position = (self.game.width/2, self.game.height+2)
        self.game.bullets.append(self.bullet)
        self.game.run_game_logic()
        self.assertEqual(len(self.game.bullets), 0)

    def test_bullets_are_removed_correctly(self):
        self.bullet.position = (self.game.width/2, self.game.height/2)
        self.game.bullets.append(self.bullet)
        self.game.asteroids.append(Asteroid(self.bullet.position))
        self.game.run_game_logic()
        self.assertEqual(len(self.game.asteroids), 0)
        self.assertEqual(len(self.game.bullets), 0)
"""
