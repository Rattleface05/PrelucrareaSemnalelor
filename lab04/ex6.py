import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

frecventa, file = sp.io.wavfile.read("lab04/ex5sounds/BoltThrower-TheKillchain.wav")

array = np.array(file,dtype=float)

if array.ndim == 2:
    array = np.mean(array, axis=1)


N = len(array)

L_grup = round(0.01 * frecventa)
pas = round(0.005 * frecventa)

grupuri = []

i = 0

while i + L_grup < N:
    aux = np.abs(np.fft.rfft(array[i: i + L_grup]))

    aux = np.log10(aux)

    grupuri.append(aux)
    i = i + pas

grupuri = np.array(grupuri).T

plt.figure(figsize=(12, 6))

plt.imshow(grupuri, aspect='auto', origin='lower', cmap='viridis', interpolation='nearest')

plt.colorbar(label="Amplitudine (dB)")
plt.xlabel("Timp (s)")
plt.ylabel("Frecventa (kHz)")
plt.suptitle("Ex 6")

plt.show()