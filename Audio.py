import pyaudio
import wave


class Audio:
    def __init__(self, duration: int, path: str):
        self.chunk = 1024  # Record in chunks of 1024 samples
        self.sample_format = pyaudio.paInt16  # 16 bits per sample
        self.channels = 2
        self.fs = 44100  # Record at 44100 samples per second
        self.seconds = duration
        self.filename = path
        
    def record(self):
        p = pyaudio.PyAudio()
        stream = p.open(format=self.sample_format,
                channels=self.channels,
                rate=self.fs,
                frames_per_buffer=self.chunk,
                input=True)
        frames = []
        for i in range(0, int(self.fs / self.chunk * self.seconds)):
            data = stream.read(chunk)
            frames.append(data)

        # Stop and close the stream 
        stream.stop_stream()
        stream.close()
        # Terminate the PortAudio interface
        p.terminate()


    
    def save(self):
        try:
            write(self.path, self.fs, self.recording)
            self.recording = None
        except Exception as e:
            print(e)
