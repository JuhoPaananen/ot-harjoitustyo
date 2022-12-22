import unittest
import pygame
from pygame import mixer
from pygame.math import Vector2
from services.asteroids import AsteroidsGame
from services.soundplayer import SoundPlayer
#from utils import load_image
from entities.objects import FlyingObject, Asteroid, LargeAsteroid, MediumAsteroid, SmallAsteroid, Bullet, Player
#from index import main


class TestAsteroidsGame(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.game = AsteroidsGame()

    def test_one_live_reduced_when_crashed_with_asteroid(self):
        self.game.spaceship = Player((self.game.width/2, self.game.height/2))
        self.game.asteroids.append(Asteroid((self.game.spaceship.position)))
        self.game._run_game_logic()

        self.assertEqual(self.game.spaceship.get_health(), 2)

    def test_asteroid_is_destroyed_when_crashed_with_player(self):
        self.game.lives = 2
        self.game.spaceship = Player((self.game.width/2, self.game.height/2))
        self.game.asteroids.append(Asteroid((self.game.spaceship.position)))
        self.game._run_game_logic()

        self.assertEqual(len(self.game.asteroids), 0)

    def test_mainloop_is_ran_correctly(self):
        self.game.start_new_game()
        self.game.spaceship.speed = Vector2(0,-10)
        self.game.spaceship.health = 1
        self.game.asteroids.append(SmallAsteroid((self.game.width/2, self.game.height/2 - 30)))
        self.game.spaceship.shoot()
        self.game.spaceship.rotate_left()
        self.game.gameloop(True)

        self.assertEqual(len(self.game.asteroids), 10)
        self.assertEqual(self.game.spaceship, None)
        self.assertFalse(self.game.playing)

    def test_large_asteroid_brokes_into_three_medium_asteroids(self):
        self.game.start_new_game()
        self.game.spaceship.position = (150, 150)
        test_asteroid = LargeAsteroid(
            (self.game.width/2, self.game.height/2))
        self.game.asteroids.append(test_asteroid)
        test_asteroid.health = 1
        self.game.spaceship.bullets.append(Bullet(test_asteroid.get_position(), 0))
        self.game._run_game_logic()

        self.assertEqual(len(self.game.asteroids), 13)

    def test_game_over_recognized(self):
        self.game.spaceship = Player((self.game.width/2, self.game.height/2))
        self.game.spaceship.health = 1
        self.game.asteroids.append(Asteroid((self.game.spaceship.get_position())))
        self.game._run_game_logic()

        self.assertEqual(self.game.is_gameover, True)

    def test_music_can_be_loaded_successfully(self):
        self.game.soundplayer.play_music()

        self.assertTrue(mixer.music.get_busy())

    def test_lives_set_correctly_when_game_initialized(self):
        self.game.start_new_game()

        self.assertEqual(self.game.spaceship.get_health(), 3)

    def test_player_initialized_when_game_initialized(self):
        self.game.start_new_game()
        
        self.assertIsNotNone(self.game.spaceship)

    def test_correct_amount_of_asteroids_created_when_game_initialized(self):
        self.game.start_new_game()

        self.assertEqual(len(self.game.asteroids), 10)

    def test_mode_is_set_to_playing_when_game_initialized(self):
        self.game.start_new_game()

        self.assertEqual(self.game.playing, True)

    def test_bullet_is_created_when_shot(self):
        self.game.start_new_game()
        self.game.spaceship.shoot()

        self.assertEqual(len(self.game.spaceship.get_bullets()), 1)

    def test_bullet_is_not_created_if_all_bullets_used(self):
        self.game.start_new_game()
        for _ in range(4):
            self.game.spaceship.shoot()

        self.assertEqual(len(self.game.spaceship.get_bullets()), 3)

    def test_all_flying_objects_are_collected(self):
        self.game.start_new_game()
        self.game.spaceship.bullets.append(
            Bullet((self.game.width/2, self.game.height/2), 0))

        self.assertEqual(len(self.game._get_flying_objects()), 12)

    def test_hit_when_asteroid_destroyed_increases_score(self):
        self.game.start_new_game()
        self.game.spaceship.position = (50, 50)
        self.game.asteroids.append(SmallAsteroid(
            (self.game.width/2, self.game.height/2)))
        self.game.spaceship.bullets.append(
            Bullet((self.game.width/2, self.game.height/2), 0))
        self.game._run_game_logic()

        self.assertEqual(self.game.score, 1)

    def test_player_is_destroyed_returns_true_when_destroyed(self):
        self.game.spaceship = Player((self.game.width/2, self.game.height/2))
        self.game.spaceship.health = 1

        self.assertEqual(self.game.spaceship.is_destroyed(), True)

    def test_player_is_none_after_destroyed(self):
        self.game.spaceship = Player((self.game.width/2, self.game.height/2))
        self.game.spaceship.health = 1
        self.game.asteroids.append(Asteroid((self.game.spaceship.get_position())))
        self.game._run_game_logic()

        self.assertEqual(self.game.spaceship, None)

    def test_player_is_not_in_drawn_after_destroyed(self):
        self.game.spaceship = Player((self.game.width/2, self.game.height/2))
        self.game.spaceship.health = 1
        self.game.asteroids.append(Asteroid((self.game.spaceship.get_position())))
        self.game._run_game_logic()

        self.assertNotIn(self.game.spaceship, self.game._get_flying_objects())

    def test_asteroids_are_not_created_when_gameover(self):
        self.game.start_new_game()
        self.game.is_gameover = True
        self.game._create_asteroids(True)

        self.assertEqual(len(self.game.asteroids), 10)

    