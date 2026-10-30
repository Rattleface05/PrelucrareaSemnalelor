import matplotlib.pyplot as plt
import numpy as np

def signal(x):
    return np.sin(2 * np.pi * 3 * x)

N = np.linspace(0,1,9)

t = np.linspace(0,1,1000)

fig, axs = plt.subplots(4)
plt.tight_layout()
fig.set_figheight(8)
fig.set_figwidth(8)
plt.suptitle("Ex 2 (N = 9)")
plt.xlabel("Timp (s)")


axs[0].plot(t, signal(t))
axs[0].set_ylabel("Amplitudine")

axs[1].plot(t, signal(t))
axs[1].scatter(N, signal(N), c='red')
axs[1].set_ylabel("Amplitudine")


axs[2].plot(t, np.sin(2 * np.pi * 11 * t),)
axs[2].scatter(N, signal(N), c='red')
axs[2].set_ylabel("Amplitudine")

axs[3].plot(t, np.sin(2 * np.pi * 19 * t))
axs[3].scatter(N, signal(N), c='red')
axs[3].set_ylabel("Amplitudine")

plt.savefig("lab04/ex2.pdf")
plt.show()