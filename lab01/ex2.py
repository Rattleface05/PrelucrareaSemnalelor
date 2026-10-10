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

plt.savefig("lab01/ex2a.pdf")
plt.show()

# b)
fig, ax = plt.subplots()
fig.suptitle("Ex 2 b)")

def b(x): 
    return np.sin(2 * np.pi * 800 * x)

t = np.linspace(0,3,9600)
ax.plot(t,b(t))
ax.set_xlim([0, 0.03])

plt.savefig("lab01/ex2b.pdf")
plt.show()

# c)
fig, ax = plt.subplots()
fig.suptitle("Ex 2 c)")

def sawtooth(x): 
    return (np.mod(240 * x,1) - 0.5) * 2

t = np.linspace(0,1,4800)
ax.plot(t,sawtooth(t))
ax.set_xlim([0, 0.03])

plt.savefig("lab01/ex2c.pdf")
plt.show()

# d)
fig, ax = plt.subplots()
fig.suptitle("Ex 2 d)")

def square(x): 
    return np.sign(np.sin(2 * np.pi * 300 * x))

t = np.linspace(0,1,4800)
ax.plot(t,square(t))
ax.set_xlim([0, 0.03])

plt.savefig("lab01/ex2d.pdf")
plt.show()

# e)
fig, ax = plt.subplots()
fig.suptitle("Ex 2 e)")

array = np.random.rand(128,128)

ax.imshow(array)
plt.savefig("lab01/ex2e.pdf")
plt.show()

# f)
fig, ax = plt.subplots()
fig.suptitle("Ex 2 f)")

array = np.zeros((128,128))

for i in range(128):
    for j in range(128):
        array[i,j] = i + j

ax.imshow(array)
plt.savefig("lab01/ex2f.pdf")
plt.show()

