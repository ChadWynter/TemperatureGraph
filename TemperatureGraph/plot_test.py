import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
x = np.linspace(0, 10*np.pi, 100)
y = np.sin(x)

# plt.ion()
fig, ax = plt.subplots()
line1 = ax.plot(x, y)

ax.set(xlabel='Time', ylabel='Temperature in C', title='Temperature Data')
ax.grid()

# plt.show()

for phase in np.linspace(0, 10*np.pi, 500):
    line1.set_ydata(np.sin(0.5 * x + phase))
    fig.canvas.draw()
    fig.canvas.flush_events()