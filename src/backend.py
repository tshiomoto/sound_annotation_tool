import librosa
import numpy as np

class SATSystem():
    def __init__(self):
        self.wav_path = None
        self.sound = None
        self.sr = None
        self.durtion = None
        self.annotation = None

    def get_sound(self, wav_path):
        self.wav_path = wav_path
        self.sound, self.sr = librosa.load(self.wav_path, sr=None)
        self.duration = librosa.audio.get_duration(self.sound, self.sr)

        return self.sound, self.sr

    def get_target_data(self, start_sec, window_length):
        return self.sound[start_sec:(start_sec+window_length)]

    def read_sat_file(self, sat_path):
        pass

    def write_sat_file(self, sat_path):
        pass
