import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani

fig, ax = plt.subplots()
x = np.linspace(0, 10*np.pi, 200)
y = np.sin(x)
line, = ax.plot(x, y)

def update(frame):
    y = np.sin(x + frame/10)
    line.set_ydata(y)
    return line,

youwerethechosenone = ani.FuncAnimation(fig, update, frames=200, interval=60, blit=True)
plt.show()
