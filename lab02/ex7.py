import matplotlib.pyplot as plt 
import numpy as np

def signal(x):
    return  np.sin(2 * np.pi * 3 * x)

fig,axs = plt.subplots(3)

t = np.linspace(0,1,100)



    
axs[0].plot(t,signal(t))
axs[0].stem(t,signal(t))
axs[0].set_ylabel("a)")
axs[0].set_xlim([0,0.3])
axs[1].plot(t[::4],signal(t)[::4])
axs[1].stem(t[::4],signal(t)[::4])
axs[1].set_ylabel("b)")
axs[1].set_xlim([0,0.3])
axs[2].plot(t[1::4],signal(t)[1::4] )
axs[2].stem(t[1::4],signal(t)[1::4] )
axs[2].set_ylabel("c)")
axs[2].set_xlim([0,0.3])

plt.xlabel("Timp (s)")
plt.savefig("lab02/ex7.pdf")
plt.show()

# Toate semnalele arata la fel