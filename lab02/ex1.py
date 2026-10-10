import matplotlib.pyplot as plt 
import numpy as np

import scipy.io.wavfile
import scipy.signal
import sounddevice

# Frecventa de esantionare mentionata in ghid
fs = 44100

# Ex 1 
def sinusul(t):
    return np.sin(2 * np.pi * 20 * t + np.pi / 2)

def cosinusul(t):
    return np.cos(2 * np.pi * 20 * t)

t = np.linspace(0,1,2000)
fig, axs = plt.subplots(2)
plt.suptitle("Ex 1")

axs[0].plot(t,sinusul(t))
axs[0].set_ylabel("Sinus")

axs[1].plot(t,cosinusul(t))
axs[1].set_ylabel("Cosinus")
axs[1].set_xlabel("Timp (s)")

for ax in axs:
    ax.set_xlim([0,0.3])

plt.savefig("lab02/ex1.pdf")
plt.show()

