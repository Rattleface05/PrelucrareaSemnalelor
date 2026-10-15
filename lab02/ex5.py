import matplotlib.pyplot as plt 
import numpy as np

import scipy.io.wavfile
import scipy.signal
import sounddevice as sd

# Frecventa de esantionare mentionata in ghid
fs = 44100
sd.default.samplerate = fs

def signal_100(x): 
    return np.sin(2 * np.pi * 100 * x)

def signal_117(x): 
    return np.sin(2 * np.pi * 117 * x)

t = np.linspace(0,4,fs)


symphony = np.append(signal_100(t), signal_117(t))

scipy.io.wavfile.write("lab02/ex5.wav", fs, symphony)
scipy.io.wavfile.read("lab02/ex5.wav")


