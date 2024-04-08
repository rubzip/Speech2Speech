import sounddevice as sd
from scipy.io.wavfile import write


class Audio:
    def __init__(self, duration: int, path: str):
        self.fs = 88000
        self.duration = duration
        self.path = path
        self.recording = None

    def record(self):
        self.recording = sd.rec(int(self.duration * self.fs), samplerate=self.fs, channels=2)
        self.wait()
    
    def save(self):
        try:
            write(self.path, self.fs, self.recording)
            self.recording = None
        except Exception as e:
            print(e)
