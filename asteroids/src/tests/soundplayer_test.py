import unittest
from pygame import mixer
from services.soundplayer import SoundPlayer


class TestSoundPlayer(unittest.TestCase):
    def setUp(self):
        self.player = SoundPlayer()

    def test_music_can_be_loaded_successfully(self):
        self.player.play_music()

        self.assertTrue(mixer.music.get_busy())
    
    def test_music_can_be_stopped(self):
        self.player.play_music()
        self.player.stop_music()

        self.assertFalse(mixer.music.get_busy())

    def test_music_can_be_paused(self):
        self.player.play_music()
        self.player.pause_music()

        self.assertFalse(mixer.music.get_busy())

    def test_music_can_be_unpaused(self):
        self.player.play_music()
        self.player.pause_music()
        self.player.pause_music()

        self.assertTrue(mixer.music.get_busy())

    def test_effect_can_be_muted(self):
        self.player.sounds_on = True
        self.player.turn_sounds_on_off()
        
        self.assertEqual(self.player.sounds_on, False)

    def test_effect_can_be_unmuted(self):
            self.player.sounds_on = False
            self.player.turn_sounds_on_off()
            
            self.assertEqual(self.player.sounds_on, True)
