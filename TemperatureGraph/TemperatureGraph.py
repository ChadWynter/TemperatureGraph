import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import serial
import numpy as np

#ser = serial.Serial("COM3", 9600)
#while True:
#        cc=str(ser.readLine())



#code for interactive graph
x = np.linspace(0, 10*np.pi, 100)
y = np.sin(x)

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title("Temperature Data")
ax.set_xlabel("Time")
ax.set_ylabel("Temperature in C")
line1, = ax.plot(x, y, 'b-')

#need to resize button
def on_click(event):
    if ("Temperature in C" in ax.get_ylabel()):
        ax.set_ylabel("Temperature in F")
    else:
        ax.set_ylabel("Temperature in C")
plt.connect('button_press_event', on_click)
bcut = Button(ax, 'change measurement', color = 'red', hovercolor = 'green')


for phase in np.linspace(0, 10*np.pi, 500):
    line1.set_ydata(np.sin(0.5 * x + phase))
    fig.canvas.draw()
    fig.canvas.flush_events()