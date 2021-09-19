import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import numpy as np
import pyrebase
  
import pyrebase

config = {
  "apiKey": "apiKey",
  "authDomain": "projectId.firebaseapp.com",
  "databaseURL": "https://ece-4880-lab1-default-rtdb.firebaseio.com/",
  "storageBucket": "projectId.appspot.com"
}

def get_temp(db):
    return db.child("Temperature").get().val()

def set_temp(db, temp):
    db.child("Temperature").push(temp)

if __name__ == "__main__":
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    current_temp = get_temp(db)
    print(current_temp)
    # set_temp(db, 10)
    
x = np.linspace(0, 10*np.pi, 100)
y = np.sin(x)

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
#ax = fig.add_axes([0,0,1,1])
line1, = ax.plot(x, y, 'b-')
ax.set_title("Temperature Data")
ax.set_xlabel("Time")
ax.set_ylabel("Temperature in C")
#ax.set_ylim(-100,100)
#ax.set_ylim(-100,100)

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