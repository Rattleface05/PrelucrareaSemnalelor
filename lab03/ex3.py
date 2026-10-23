import matplotlib.pyplot as plt 
import numpy as np

t = np.linspace(0,1,10000)
W = np.linspace(1,100,100)
N = 10000

def signal(x):
    a = 0.75 * np.sin(2 * np.pi * 10 * x + 0.1) # f1 = 10
    b = 3 * np.sin(2 * np.pi * 90 * x + 2) # f2 = 90
    c = 2 * np.cos(2 * np.pi * 45 * x) # f3 = 45

    return a + b + c

def ft(w, func):
    n = np.arange(N)
    
    return np.array([np.sum(func(t) * np.e ** (-2 * np.pi * 1j * n * freq / N)) for freq in w])

fig, (ax1, ax2) = plt.subplots(1,2)
plt.suptitle("Ex 3")
plt.tight_layout()
fig.set_figheight(6)
fig.set_figwidth(10)


ax1.plot(t,signal(t))
ax1.set_xlabel("Timp (s)")
ax1.set_ylabel("Amplitudine")

ax2.stem(W,np.abs(ft(W, signal)))
ax2.set_xlabel("Frecveta (Hz)")
ax2.set_ylabel("|X(ω)|")


plt.savefig("lab03/ex3.pdf")
plt.show()