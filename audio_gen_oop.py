import sys
import pyaudio
import numpy as np
import time
import wave

class Audio_gen:
    def __init__(self,exp_dur,filename,pause_t):
        self.p = pyaudio.PyAudio()
        self.exp_dur = exp_dur
        self.filename = filename
        self.pause_t = pause_t
    # Initialize audio stream parameters
        self.f = wave.open(filename,'rb')
        self.samples = self.f.readframes(self.f.getnframes())
        self.format = self.p.get_format_from_width(self.f.getsampwidth())
        self.channels = self.f.getnchannels()
        self.rate = self.f.getframerate()
        self.output = True
        
    def send_to_speaker(self):
        stream = self.p.open(format=self.format,
                    channels=self.channels,
                    rate=self.rate,
                    output=self.output)

        t = time.time()
        d = time.time() - t
        while d < self.exp_dur:
                
            # play. May repeat with different volume values (if done interactively)
            t1 = time.time()
            stream.write(self.samples)
            print('stream duration = ',time.time()-t1)
            t1 = time.time()
            if self.pause_t > 0:

                time.sleep(pause_t)
                print('pause time = ', time.time()-t1)

            d = round(time.time() - t)
            print(d,self.exp_dur)
        stream.stop_stream()
        stream.close()

        self.p.terminate()


if __name__ == '__main__':
    exp_dur = float(sys.argv[1])
    print exp_dur
    audio_gen = Audio_gen(exp_dur,'White-noise-sound-20sec-mono-44100Hz.wav',0)
    audio_gen.send_to_speaker()
