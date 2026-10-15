import matplotlib.pyplot as plt 
import numpy as np

import scipy.io.wavfile
import scipy.signal
import sounddevice as sd

# Frecventa de esantionare mentionata in ghid
fs = 44100

fig, axs = plt.subplots(3)

def a(x):
    return np.sin(2 * np.pi * fs/2 * x)

def b(x):
    return np.sin(2 * np.pi * fs/4 * x)

def c(x):
    return np.sin(2 * np.pi * 0 * x)

t = np.linspace(0,1,1000)


axs[0].plot(t,a(t))
axs[0].set_ylabel("a)")
axs[0].set_xlim([0,0.03])
axs[1].plot(t,b(t))
axs[1].set_ylabel("b)")
axs[1].set_xlim([0,0.03])
axs[2].plot(t,c(t) )
axs[2].set_ylabel("c)")
axs[2].set_xlim([0,0.03])

plt.xlabel("Timp (s)")
plt.savefig("lab02/ex6.pdf")
plt.show()

# In timpul in care se termina o perioada pentru fs/4, se termina 2 perioade pentru fs/2.
# Pentru f = 0 Hz, nu se intampla nimic
