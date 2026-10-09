import matplotlib.pyplot as plt
import numpy as np

# EX 2


# a)
fig, ax = plt.subplots()
fig.suptitle("Ex 2 a)")
def a(x): 
    return np.sin(2 * np.pi * 400 * x)

t = np.linspace(0,1,1600)
ax.plot(t,a(t))
ax.set_xlim([0, 0.03])

plt.show()

# b)
fig, ax = plt.subplots()
fig.suptitle("Ex 2 b)")

def b(x): 
    return np.sin(2 * np.pi * 800 * x)

t = np.linspace(0,3,4800)
ax.plot(t,b(t))
ax.set_xlim([0, 0.03])

plt.show()

# c)
fig, ax = plt.subplots()
fig.suptitle("Ex 2 c)")

def sawtooth(x): 
    return np.mod(240 * x,1)

t = np.linspace(0,1,4800)
ax.plot(t,sawtooth(t))
ax.set_xlim([0, 0.03])

plt.show()

# d)
fig, ax = plt.subplots()
fig.suptitle("Ex 2 c)")

def square(x): 
    return np.sign(np.sin(2 * np.pi * 300 * x),1)

t = np.linspace(0,1,4800)
ax.plot(t,square(t))
ax.set_xlim([0, 0.03])

plt.show()