#This program will record a snippet of audio
#and play it back

import sounddevice as sd                    # allows the program to access the sound device
import numpy as numpy
import scipy.io.wavfile as wav              # allows the program to make a wav file

fs = 44100                                  # sample rate                        in cycles per second
duration = 3                                # Duration of the recording          in seconds
myRecording = sd.rec(duration * fs, samplerate=fs, channels=1, dtype='float64') #take a recording
print('Recording Audio')                    # print to the console that a recording is taking place
sd.wait()                                   # wait for the recording to finish
print("Recording complete")                 # Print to the console that recording is over
sd.play(myRecording, fs)                    # play the recording
sd.wait()                                   # wait while the recording plays