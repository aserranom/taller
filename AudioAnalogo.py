import pyaudio
import wave
import BigInput #Objeto de Roberto

class AudioAnalogo:
    chunk = 1024

    def __init__(self):
        """ Init audio stream """ 
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format = pyaudio.paInt16,
            channels = 1,
            rate = 22000,
            input=True,
            output = True
        )

    def playAnalogico(self):
        """ Play entire file """
        data = self.stream.read(self.chunk)
        while data != '':
            self.stream.write(data)
            data = self.stream.read(self.chunk)

    def close(self):
        """ Graceful shutdown """ 
        self.stream.close()
        self.p.terminate()

# Ejemplo para pyaudio
a = AudioAnalogo()
a.playAnalogico()
a.close()
