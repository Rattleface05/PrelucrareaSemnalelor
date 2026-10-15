import matplotlib.pyplot as plt 
import numpy as np



def taylor(x):
    return x

def pade(x):
    return (x - 7 * (x ** 3) / 60) / (1 + (x ** 2) / 20)

fig,axs = plt.subplots(4)
fig.set_figheight(7)
fig.set_figwidth(6)

alpha = np.linspace(-np.pi/2,np.pi/2,1000)

axs[0].plot(alpha, taylor(alpha))
axs[0].plot(alpha, np.sin(alpha),color='red')
axs[0].set_ylabel("Aprox Taylor")
axs[1].plot(alpha, abs(taylor(alpha) - np.sin(alpha)))
axs[1].set_ylabel("Error Taylor")
axs[2].plot(alpha, pade(alpha))
axs[2].plot(alpha, np.sin(alpha),color='red')
axs[2].set_ylabel("Aprox Pade")
axs[3].plot(alpha, abs(pade(alpha) - np.sin(alpha)))
axs[3].set_ylabel("Error Pade")

plt.xlabel("Timp (s)")
plt.savefig("lab02/ex8.pdf")
plt.show()

# Axa y logaritmica
fig,axs = plt.subplots(4)
fig.set_figheight(7)
fig.set_figwidth(6)

alpha = np.linspace(-np.pi/2,np.pi/2,1000)

for ax in axs:
    ax.set_yscale("log")

axs[0].plot(alpha, taylor(alpha))
axs[0].plot(alpha, np.sin(alpha),color='red')
axs[0].set_ylabel("Aprox Taylor")
axs[1].plot(alpha, abs(taylor(alpha) - np.sin(alpha)))
axs[1].set_ylabel("Error Taylor")
axs[2].plot(alpha, pade(alpha))
axs[2].plot(alpha, np.sin(alpha),color='red')
axs[2].set_ylabel("Aprox Pade")
axs[3].plot(alpha, abs(pade(alpha) - np.sin(alpha)))
axs[3].set_ylabel("Error Pade")

plt.xlabel("Timp (s)")
plt.savefig("lab02/ex8log.pdf")
plt.show()
