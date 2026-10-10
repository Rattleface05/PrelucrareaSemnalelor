import matplotlib.pyplot as plt 
import numpy as np
from math import sqrt

import scipy.io.wavfile
import scipy.signal
import sounddevice as sd

# Frecventa de esantionare mentionata in ghid
fs = 44100

def signal(t, phase=0):
    return np.sin(2 * np.pi * 2 * t + phase)

fig, axs = plt.subplots(4)
plt.suptitle("Ex 2")

t = np.linspace(0,1,100)

axs[0].plot(t,signal(t))
axs[0].set_ylabel("Faza = 0")
axs[1].plot(t,signal(t, np.pi / 4))
axs[1].set_ylabel("Faza = pi/4")
axs[2].plot(t,signal(t, np.pi / 3))
axs[2].set_ylabel("Faza = pi/3")
axs[3].plot(t,signal(t, np.pi / 2))
axs[3].set_ylabel("Faza = pi/4")

plt.xlabel("Timp (s)")
plt.savefig("lab02/ex2.pdf")
plt.show()

# Noise
fig, axs = plt.subplots(4)
plt.suptitle("Ex 2 cu Noise")

np.random.seed(67)
z = np.random.normal(size=len(t))

gamma = []
for (snr,faza) in [(0.1, 0), (1, np.pi / 2), (10, np.pi / 3), (100, np.pi / 4)]:
    #snr = norm(x) ^ 2 / (gamma ^ 2 * norm(z) * 2) => gamma = norm(x) / (sqrt(snr) * norm(z))
    aux = np.linalg.norm(signal(t,faza)) / (sqrt(snr) * np.linalg.norm(z))
    gamma.append(aux)

axs[0].plot(t,signal(t))
axs[0].stem(t,signal(t) + gamma[0] * z)
axs[0].set_ylabel("Faza = 0")
axs[1].plot(t,signal(t, np.pi / 4))
axs[1].stem(t,signal(t, np.pi / 4) + gamma[1] * z)
axs[1].set_ylabel("Faza = pi/4")
axs[2].plot(t,signal(t, np.pi / 3))
axs[2].stem(t,signal(t, np.pi / 3) + gamma[2] * z)
axs[2].set_ylabel("Faza = pi/3")
axs[3].plot(t,signal(t, np.pi / 2))
axs[3].stem(t,signal(t, np.pi / 2) + gamma[3] * z)
axs[3].set_ylabel("Faza = pi/4")

plt.xlabel("Timp (s)")
plt.savefig("lab02/ex2noise.pdf")
plt.show()