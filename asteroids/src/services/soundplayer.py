from pygame import mixer
from utils import load_sound, get_music_path

class SoundPlayer:
    def __init__(self):
        mixer.pre_init(44100, -16, 4, 1024)
        mixer.init()
        self.blaster_sound = load_sound("LaserBlast.mp3")
        self.blaster_sound.set_volume(0.5)
        self.explosion_sound = load_sound("explosion.mp3")
        self.crash_sound = load_sound("Crash.mp3")
        self.move_sound = load_sound("whoosh.wav")
        self.move_sound.set_volume(0.3)
        self.click_sound = load_sound("click.wav")
        mixer.music.load(get_music_path("Fire_Aura"))
        mixer.music.set_volume(0.7)
        mixer.music.play(-1)
        self.sounds_on = True

    def play_music(self):
        mixer.music.play(-1)

    def stop_music(self):
        mixer.music.stop()

    def pause_music(self):
        if mixer.music.get_busy():
            mixer.music.pause()
        else:
            mixer.music.unpause()

    def play_blaster_effect(self):
        if self.sounds_on:
            mixer.Sound.play(self.blaster_sound)

    def play_crash_effect(self):
        if self.sounds_on:
            mixer.Sound.play(self.crash_sound)

    def play_explosion_effect(self):
        if self.sounds_on:
            mixer.Sound.play(self.explosion_sound)

    def play_move_effect(self):
        mixer.Sound.play(self.move_sound)

    def play_click_effect(self):
        mixer.Sound.play(self.click_sound)

    def turn_sounds_on_off(self):
        if self.sounds_on:
            self.sounds_on = False
        else:
            self.sounds_on = True