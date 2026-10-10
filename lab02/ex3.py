import matplotlib.pyplot as plt 
import numpy as np

import scipy.io.wavfile
import scipy.signal
import sounddevice as sd

# Frecventa de esantionare mentionata in ghid
fs = 44100
sd.default.samplerate = fs

def a(x): 
    return np.sin(2 * np.pi * 400 * x)

def b(x): 
    return np.sin(2 * np.pi * 800 * x)

# c)
def sawtooth(x): 
    return (np.mod(240 * x,1) - 0.5) * 2

# d)
def square(x): 
    return np.sign(np.sin(2 * np.pi * 300 * x))

t = np.linspace(0,3,4800)

sd.play(a(t))

sd.play(b(t))

sd.play(sawtooth(t))

sd.play(square(t))

scipy.io.wavfile.write("lab02/ex3.wav", fs, square(t))
scipy.io.wavfile.read("lab02/ex3.wav")
#urechile...au

