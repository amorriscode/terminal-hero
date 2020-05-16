from openal import *

class Song:
    def __init__(self, songPath):
        self.songPath = songPath

        self.listener = oalGetListener()

        self.song = oalOpen(f"{songPath}/song.ogg")
        self.guitar = oalOpen(f"{songPath}/guitar.ogg")
        self.rhythm = oalOpen(f"{songPath}/rhythm.ogg")

    def play(self):
        self.song.play()
        self.guitar.play()
        self.rhythm.play()

    def get_state(self):
        return self.song.get_state()
    