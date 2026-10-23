import matplotlib.pyplot as plt 
import numpy as np

def signal(x):
    return np.sin(2 * np.pi *  10 * x )

def fourier(x,w=1):
    return signal(x) * np.e ** (-2 * np.pi * 1j* w *x)

fig, (ax1, ax2) = plt.subplots(1,2)

t = np.linspace(0,1,3000)
axe = np.linspace(-2,2,1000)
plt.suptitle("Ex 2 Figura 1")
plt.tight_layout()
fig.set_figheight(6)
fig.set_figwidth(10)

ax1.scatter(t,signal(t),c=np.sqrt(t**2 + signal(t)**2))
ax1.plot(axe,[0] * len(axe),color='black')
ax1.set_xlim([0,1])
ax1.set_xlabel("Timp (s)")
ax1.set_ylabel("Amplitudine")

ax2.scatter(fourier(t).real,fourier(t).imag,c=np.sqrt(fourier(t).real**2 + fourier(t).imag**2))
ax2.plot(axe,[0] * len(axe),color='black')
ax2.plot([0] * len(axe),axe,color='black')
ax2.set_xlim([-1.1,1.1])
ax2.set_ylim([-1.1,1.1])
ax2.set_xlabel("Real")
ax2.set_ylabel("Imaginar")

plt.savefig("lab03/ex2fig1.pdf")
plt.show()


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2)
plt.suptitle("Ex 2 Figura 2")
plt.tight_layout()
fig.set_figheight(6)
fig.set_figwidth(10)

W = [1,5,10,18] 

for (w,ax) in zip(W, [ax1, ax2, ax3, ax4]):
    ax.scatter(fourier(t,w).real,fourier(t,w).imag,c=np.sqrt(fourier(t,w).real**2 + fourier(t,w).imag**2))
    ax.plot(axe,[0] * len(axe),color='black')
    ax.plot([0] * len(axe),axe,color='black')
    ax.set_xlim([-1.1,1.1])
    ax.set_ylim([-1.1,1.1])
    ax.set_xlabel("Real")
    ax.set_ylabel("Imaginar")


plt.savefig("lab03/ex2fig2.pdf")
plt.show() 
