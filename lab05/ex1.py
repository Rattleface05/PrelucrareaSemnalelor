import numpy as np
import matplotlib.pyplot as plt
import csv 

x = np.genfromtxt("lab05/Train.csv", delimiter=',')[1:]
x = [list[2] for list in x]

'''
a) N = 18288 de esantioane din Train.csv
'''

N = 18288

X = np.fft.fft(x)

X = np.abs(X/N)

X = X[:N//2]

'''
b) 25.08.2012, 00:00 - 25-09-2014, 23:00
'''

'''
c) Frecventa maxima a fost 1244
'''

fig, ax = plt.subplots()

ax.set_xlabel("Frecventa (Hz)")
ax.set_ylabel("|X(ω)|")


