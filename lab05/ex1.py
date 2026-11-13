import numpy as np
import matplotlib.pyplot as plt

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
b) 25.08.2012, 00:00 - 25-09-2014, 23:00, la ora
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

'''f) Selectam cele mai mari 8 semanle din fourier'''
fourth_biggest = sorted(X, reverse=True)[:8]
componente = []

for freq in fourth_biggest:
    for i in range(1,N//2):
        if X[i] == freq:
            componente.append(np.float128(f[i]))

transform = [(60, 'minut'), (60, 'ora'), (24, 'zi'), (30, 'luna'), (365, 'an')]

for componenta in componente:
    aux_nr = componenta
    aux_unitate = 's'
    i = 0
    while aux_nr < 1:
        if i >= len(transform):
            break
        else:
            nr, unitate = transform[i]
        if unitate == 'luna':
            aux_nr = aux_nr / 30 * nr
        else:
            aux_nr *= nr
        aux_unitate = unitate
        i+=1
    print(f"Componenta de {componenta} Hz inseamna {aux_nr} pe {aux_unitate}")
'''
Results:
Componenta de 1.5190734866989925e-08 Hz inseamna 0.47905501476539425 pe an
Componenta de 3.038146973397985e-08 Hz inseamna 0.9581100295307885 pe an
Componenta de 1.1575339968646325e-05 Hz inseamna 1.0001093732910424 pe zi
Componenta de 4.557220460096978e-08 Hz inseamna 1.437165044296183 pe an
Componenta de 1.6557901005019021e-06 Hz inseamna 52.21699660942799 pe an
Componenta de 6.07629394679597e-08 Hz inseamna 1.916220059061577 pe an
Componenta de 1.1590530703513315e-05 Hz inseamna 1.0014218527835503 pe zi
Componenta de 7.595367433494964e-08 Hz inseamna 2.395275073826972 pe an
'''

'''g) Alegem esantionul 5256, 01-04-2013 00:00'''

x = np.genfromtxt("lab05/Train.csv", delimiter=',')[1:]
x = [list[2] for list in x]
g = x[5256:5256 + 720] # 720, aka o luna, de esantioane din 01-04-2013

fig, ax = plt.subplots()
fig.suptitle("Ex 1 g)")


ax.plot(range(len(g)), g)
ax.set_xlabel("Esantioane")
ax.set_ylabel("Masini")

plt.savefig("lab05/ex1g.pdf")
plt.show()

'''h) Datorita spike-ului care apare la inceputul saptmanii, putem merge in fata si in spate pe semnal pentru
    a determina cand a fost ziua de luni si cand va fi din nou, si asa aflam in ce zi a saptamanii suntem.
    Nu putem, totusi, sa aflam data fixa, putem maxim sa aflam ziua saptamanii
'''

'''i) Facem ultimele 1000 de frecvente 0 si dupa inversam'''

x = np.genfromtxt("lab05/Train.csv", delimiter=',')[1:]
x = [list[2] for list in x]

X = np.fft.fft(x)

# X = np.abs(X/N)

# X = X[:N//2]
# Nu mai e necesar, fac de la -1000 de la mijloc la + 1000 de la mijloc

for i in range(N//2 - 9000, N//2 + 9000):
    X[i] = 0

inverse_x = np.fft.ifft(X)

inverse_x = np.abs(inverse_x)

fig, ax = plt.subplots()
fig.suptitle("Ex 1 i)")

ax.plot(range(len(x)), x, label="Semnal brut")

ax.plot(range(len(inverse_x)), inverse_x, c='red', label="Semnal filtrat")

ax.legend()
ax.set_xlim([10000,11000])
ax.set_ylim([0,500])

plt.xlabel("Esantioane")
plt.savefig("lab05/ex1i.pdf")
plt.show()