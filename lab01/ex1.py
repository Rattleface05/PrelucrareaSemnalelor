import matplotlib.pyplot as plt 
import numpy as np

# fig, axs = plt.subplots(n)
# fig.suptitle("Titlu principal")


# EX 1

def x(t):
    return np.cos(520 * np.pi * t + np.pi/3)

def y(t):
    return np.cos(280 * np.pi * t - np.pi/3)

def z(t):
    return np.cos(120 * np.pi * t + np.pi/3)

fig, axs = plt.subplots(3)
fig.suptitle("Ex 1")

# plt.show()

t = np.linspace(0, 0.03, 61)

axs[0].plot(t, x(t))
axs[0].set_xlabel("Timp (s)")
axs[0].set_ylabel("X")
axs[1].plot(t, y(t))
axs[1].set_xlabel("Timp (s)")
axs[1].set_ylabel("Y")
axs[2].plot(t, z(t))
axs[2].set_xlabel("Timp (s)")
axs[2].set_ylabel("Z")

# c)
n = np.linspace(0, 1, 200)
axs[0].stem(n, x(n))
axs[1].stem(n, y(n))
axs[2].stem(n, z(n))

for ax in axs.flat:
    ax.set_xlim([0, 0.03])


plt.savefig("lab01/ex1.pdf")
plt.show()







