import matplotlib.pyplot as plt 
import numpy as np

import scipy.io.wavfile
import scipy.signal
import sounddevice as sd

# Frecventa de esantionare mentionata in ghid
fs = 44100
sd.default.samplerate = fs


def signal(x): 
    return np.sin(2 * np.pi * 400 * x)

def square(x): 
    return np.sign(np.sin(2 * np.pi * 400 * x))

t = np.linspace(0,1,100)

fig,axs = plt.subplots(3)
plt.suptitle("Ex 4")


axs[0].plot(t,signal(t))
axs[0].set_ylabel("Sinus")
axs[1].plot(t,square(t))
axs[1].set_ylabel("Square")
axs[2].plot(t,signal(t) + square(t))
axs[2].set_ylabel("Sinus + square")

plt.xlabel("Timp (s)")
plt.savefig("lab02/ex4.pdf")
plt.show()
