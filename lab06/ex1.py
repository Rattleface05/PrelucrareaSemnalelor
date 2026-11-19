import matplotlib.pyplot as plt 
import numpy as np

t = np.linspace(-3,3,1000)
hz1 = np.linspace(-3,3,7)
hz1_5 = np.linspace(-3,3,11)
hz2 = np.linspace(-3,3,15)
hz4 = np.linspace(-3,3,29)
B = 1

fig, (axs1, axs2) = plt.subplots(2,2)
fig.suptitle("sinc^2(Bt)")
plt.tight_layout()

axs1[0].set_title("Fs = 1.00 Hz")
axs1[0].stem(hz1, (np.sinc(B * hz1))**2, linefmt='orange')
axs1[0].plot(t, (np.sinc(B * t))**2 )

axs1[1].set_title("Fs = 1.50 Hz")
axs1[1].stem(hz1_5, (np.sinc(B * hz1_5))**2, linefmt='orange' )
axs1[1].plot(t, (np.sinc(B * t))**2 )

axs2[0].set_title("Fs = 2.00 Hz")
axs2[0].stem(hz2, (np.sinc(B * hz2))**2, linefmt='orange' )
axs2[0].plot(t, (np.sinc(B * t))**2 )

axs2[1].set_title("Fs = 4.00 Hz")
axs2[1].stem(hz4, (np.sinc(B * hz4))**2, linefmt='orange' )
axs2[1].plot(t, (np.sinc(B * t))**2 )

plt.show()
