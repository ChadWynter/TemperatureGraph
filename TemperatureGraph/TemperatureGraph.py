import matplotlib.pyplot as plt
import serial
import numpy as np

#ser = serial.Serial("COM3", 9600)
#while True:
#        cc=str(ser.readLine())


x = np.linspace(0, 10*np.pi, 100)
y = np.sin(x)

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot(x, y, 'b-')

for phase in np.linspace(0, 10*np.pi, 500):
    line1.set_ydata(np.sin(0.5 * x + phase))
    fig.canvas.draw()
    fig.canvas.flush_events()
