import matplotlib.pyplot as plt 
import numpy as np
import math

N = 8

w = math.e ** (-2 * np.pi * 1j / N)

DFT_matrix = np.zeros((N,N),dtype=complex)

for i in range(N):
    for j in range(N):
        DFT_matrix[i][j] = w ** (i*j % N)

DFT_matrix = DFT_matrix / np.sqrt(N)

print(np.allclose(np.dot(DFT_matrix, DFT_matrix.conj().T), np.eye(DFT_matrix.shape[0])))

fig,axs = plt.subplots(8)
fig.set_figheight(9)
fig.set_figwidth(9)
fig.suptitle("DFT Mapped")

for ax in range(8):
    axs[ax].stem(DFT_matrix[ax].real,DFT_matrix[ax].imag)
    axs[ax].set_ylabel("Imag")
    axs[ax].set_xlabel(f"Real (Coloana {ax+1})")
plt.tight_layout()

plt.savefig("lab03/ex1.pdf")
plt.show()