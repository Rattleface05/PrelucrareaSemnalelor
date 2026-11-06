import numpy as np
import matplotlib.pyplot as plt
import csv 

x = np.genfromtxt("lab05/Train.csv", delimiter=',')[1:]
x = [list[2] for list in x]

'''
a) Fs = 1/3600 Hz in Train.csv, odata la ora
'''
Fs = 1/3600

N = 18288

X = np.fft.fft(x)

X = np.abs(X/N)

X = X[:N//2]

f = Fs*np.linspace(0,N//2,N//2)/N

'''
b) 25.08.2012, 00:00 - 25-09-2014, 23:00, la minut
'''

'''
c) Frecventa maxima este la 0Hz, dar daca ignoram componenta continua, este la 1.5190734866989925017e-08 Hz (luat din codul de mai jos)

for i in range(1,N//2):
    if X[i] == max(X[1:]):
        print(np.float128(f[i]))
'''


'''d)'''


fig, ax = plt.subplots()
fig.suptitle("Ex 1 d)")



ax.plot(f, X)
ax.set_xlabel("Frecventa (Hz)")
ax.set_ylabel("|X(ω)|")
ax.set_yscale('log')

plt.savefig("lab05/ex1d.pdf")
plt.show()

'''e) Scad media semnalului pentru a elimina componenta continua'''

x = np.array(x)-np.mean(x)

X = np.fft.fft(x)

X = np.abs(X/N)

X = X[:N//2]

fig, ax = plt.subplots()
fig.suptitle("Ex 1 e)")


ax.plot(f[1:], X[1:])
ax.set_xlabel("Frecventa (Hz)")
ax.set_ylabel("|X(ω)|")
ax.set_yscale('log')

plt.savefig("lab05/ex1e.pdf")
plt.show()

'''f)'''