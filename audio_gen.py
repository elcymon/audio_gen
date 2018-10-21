import sys
import pyaudio
import numpy as np
import time
import wave
exp_dur = 0
pause_t = 0
p = pyaudio.PyAudio()

def send_to_speaker(samples,format,channels,rate,output):
    global p
    stream = p.open(format=format,
                    channels=channels,
                    rate=rate,
                    output=output)

    t = time.time()
    d = time.time() - t
    while d < exp_dur:
            
        # play. May repeat with different volume values (if done interactively)
        t1 = time.time()
        stream.write(samples)
        print('stream duration = ',time.time()-t1)
        t1 = time.time()
        if pause_t > 0:

            time.sleep(pause_t)
        print('pause time = ', time.time()-t1)

        d = round(time.time() - t)
        print(d,exp_dur)
    stream.stop_stream()
    stream.close()

    p.terminate()


if __name__ == '__main__':
    time.sleep(0)
    if len(sys.argv) == 4:
        exp_dur = float(sys.argv[1])
        pause_t = float(sys.argv[3])
        filename = sys.argv[2]
        f = wave.open(filename,'rb')
        samples = f.readframes(f.getnframes())
        format = p.get_format_from_width(f.getsampwidth())
        channels = f.getnchannels()
        rate = f.getframerate()
        output = True
        send_to_speaker(samples,format,channels,rate,output)
    else:
        print('''
                invalid start up
                usage:\n
                python audio_gen.py exp_dur filename pause_t vol\n\n''')
        