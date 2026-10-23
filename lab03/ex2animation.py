import matplotlib.pyplot as plt 
import matplotlib.animation as anmt
import numpy as np

def signal(x):
    return np.sin(2 * np.pi *  10 * x )

def fourier(x,w=1):
    return signal(x) * np.e ** (-2 * np.pi * 1j* w *x)



fig, (ax1, ax2) = plt.subplots(1,2)

t = np.linspace(0,1,3000)
plt.suptitle("Ex 2 Figura 1")
plt.tight_layout()
fig.set_figheight(6)
fig.set_figwidth(10)

punct1 = ax1.plot([], [], 'ro', markersize=8)[0]
punct2 = ax2.plot([], [], 'ro', markersize=8)[0]


line1 = ax1.plot(t,signal(t))[0]
ax1.set_xlabel("Timp (s)")
ax1.set_ylabel("Amplitudine")

line2 = ax2.plot(fourier(t).real,fourier(t).imag)[0]
ax2.set_xlim([-1.1,1.1])
ax2.set_ylim([-1.1,1.1])
ax2.set_xlabel("Real")
ax2.set_ylabel("Imaginar")

def updatefig1(frame):
    # update the line plot:
    line1.set_xdata(t[:frame])
    line1.set_ydata(signal(t)[:frame])
    
    line2.set_xdata(fourier(t).real[:frame])
    line2.set_ydata(fourier(t).imag[:frame])

    punct1.set_data([t[frame]], [signal(t)[frame]])
    punct2.set_data([fourier(t).real[frame]], [fourier(t).imag[frame]])
    return (line1, line2, punct1, punct2)

anim = anmt.FuncAnimation(fig=fig, func=updatefig1, frames=len(t), interval=1, blit=True, repeat=False)
plt.show()


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2)
plt.suptitle("Ex 2 Figura 2")
plt.tight_layout()
fig.set_figheight(8)
fig.set_figwidth(10)

W = [1,5,10,18] 
lines = []
points = []

for (w,ax) in zip(W, [ax1, ax2, ax3, ax4]):
    line = ax.plot(fourier(t,w).real,fourier(t,w).imag)[0]
    point = ax.plot([], [], 'ro', markersize=8)[0]
    
    points.append(point)
    lines.append(line)
    ax.title.set_text(f"ω = {w}")
    ax.set_xlim([-1.1,1.1])
    ax.set_ylim([-1.1,1.1])
    ax.set_xlabel("Real")
    ax.set_ylabel("Imaginar")



def updatefig2(frame):
    # update the line plot:
    line1.set_xdata(t[:frame])
    line1.set_ydata(signal(t)[:frame])
    
    line2.set_xdata(fourier(t).real[:frame])
    line2.set_ydata(fourier(t).imag[:frame])

    for (line,point, w) in zip(lines,points,W):
        line.set_xdata(fourier(t,w).real[:frame])
        line.set_ydata(fourier(t,w).imag[:frame])
        point.set_data([fourier(t,w).real[frame]],[fourier(t,w).imag[frame]])

    return tuple(lines + points)

anim = anmt.FuncAnimation(fig=fig, func=updatefig2, frames=len(t), interval=1, blit=True)
plt.show() 
