import matplotlib.pyplot as plt
import numpy as np
import time

# Fie un semnal pe care sa testez transformarile
def signal(x):
    return np.sin(2 * np.pi * x) + 0.9 * np.cos(2 * np.pi * 3 * x)

def dft(a, N=-1):
    if N < 0:
        N = len(a)

    if N == 1:
        return [a[0]]
    
    return [np.sum([a[n] * np.e ** (-2 * np.pi * 1j* w * n / N) for n in range(N)]) for w in range(N)]

def fft(a, N = -1):
    if N < 0:
        N = len(a)

    if N == 1:
        return [a[0]]

    X = np.zeros(N,dtype=complex)

    even = fft(a[:N:2])
    odd = fft(a[1:N:2])

    for k in range(N//2):
        X[k] = even[k] + np.e ** (-2 * np.pi * 1j* k / N) * odd[k]
        X[k + N // 2] = even[k] - np.e ** (-2 * np.pi * 1j* k / N) * odd[k]

    return X



N_valori = [128, 256, 512, 1024, 2048, 4096, 8192]
personal_fft_timp = []
numpy_fft_timp = []

for N in N_valori:
    t = np.linspace(0,1,N)
    signal_t = signal(t)

    start = time.time()
    fft(signal_t)
    end = time.time()

    personal_fft_timp.append(end - start)

    start = time.time()
    np.fft.fft(signal_t)
    end = time.time()
    
    numpy_fft_timp.append(end - start)


fig, ax = plt.subplots()
plt.suptitle("Ex 1 personal implementation")
ax.set_yscale("log") # log scale
fig.set_figheight(6)
fig.set_figwidth(6)

ax.plot(N_valori, personal_fft_timp)
ax.set_xlabel("N")
ax.set_ylabel("Timp")

plt.savefig("lab04/ex1pers.pdf")
plt.show()

fig, ax = plt.subplots()
plt.suptitle("Ex 1 numpy implementation")
ax.set_yscale("log") # log scale
fig.set_figheight(6)
fig.set_figwidth(6)

ax.plot(N_valori, numpy_fft_timp)
ax.set_xlabel("N")
ax.set_ylabel("Timp")

plt.savefig("lab04/ex1np.pdf")
plt.show()


