from openal import *
from mido import MidiFile


class Song:
    def __init__(self, songPath):
        self.songPath = songPath

        self.listener = oalGetListener()

        self.song = oalOpen(f"{songPath}/song.ogg")
        self.guitar = oalOpen(f"{songPath}/guitar.ogg")
        self.rhythm = oalOpen(f"{songPath}/rhythm.ogg")

        self.midi = MidiFile(f"{songPath}/notes.mid")

        self.time_signature = {
            "numerator": 4,
            "denominator": 4,
        }
        self.tempo = 500000  # default to 120 bpm
        self.notes = []

        self.parse_midi()

    def play(self):
        self.song.play()
        self.guitar.play()
        self.rhythm.play()

    def get_state(self):
        return self.song.get_state()

    def parse_midi(self):
        for i, track in enumerate(self.midi.tracks):
            for msg in track:
                if msg.is_meta and msg.time == 0:
                    if msg.type == "time_signature":
                        self.time_signature = {
                            "numerator": msg.numerator,
                            "denominator": msg.denominator,
                        }
                    if msg.type == "set_tempo":
                        self.tempo = msg.tempo

            if track.name == "PART GUITAR":
                self.notes = track
