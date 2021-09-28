import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox
import numpy as np
import pyrebase
from time import sleep
from collections import OrderedDict
import time


config = {
  "apiKey": "apiKey",
  "authDomain": "projectId.firebaseapp.com",
  "databaseURL": "https://ece-4880-lab1-default-rtdb.firebaseio.com/",
  "storageBucket": "projectId.appspot.com"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
def send_button_press(db, change):
    db.child("ReadTemperatureButton").set(change)


def get_stored_temperatures(db):
    temp_data = db.child("Temperature").get().val()
    time_data = db.child("Time").get().val()

    final_temp_data = []
    final_time_data = []
    for element in temp_data:
        final_temp_data.append(temp_data[element])

    for element in time_data:
        final_time_data.append(time_data[element])

    return np.array(final_temp_data), np.array(final_time_data)

    # set_temp(db, 10)

#getting the stored temperatures
a, Time = get_stored_temperatures(db)
send_button_press(db,0)

#test to convert array to float
e = np.array(['nil', 'nil', 3, 4, 5])
f = np.array([])
for x in e:
    if x == 'nil':
        f = np.append(f, None)
    else:
        f = np.append(f,float(x))
#print(f)

#should convert array to float
temp = np.array([])
for i in a:
    if i == 'nil':
        temp = np.append(temp, None)
    else:
        temp = np.append(temp,float(i))
if temp.size == 301:
    temp = np.delete(temp, 0)
temp = np.flip(temp)
#print(temp)



plt.ion()
fig, ax = plt.subplots(sharex = True)
x = np.arange(1,301)
line1, = ax.plot(x,temp, 'b-')
plt.gcf().set_size_inches(9.5, 10)
 

ax.invert_xaxis()
ax.set_ylim([10,50])
ax.set_title("Temperature Data")
ax.set_xlabel("Time (seconds ago)")
ax.set_ylabel("Temperature in C")
 
#button code starts here (changes only stay when anywhere but the button is pressed)

def on_click(event):
    if ("Temperature in C" in ax.get_ylabel()):
        ax.set_ylabel("Temperature in F")
        ax.set_ylim([50,122])
    else:
        ax.set_ylabel("Temperature in C")
        ax.set_ylim([10,50])
    #fig.canvas.draw()
    #fig.canvas.flush_events()
    
#defining real time temperature textbox
graphBox = fig.add_axes([0.3, 0.92, 0.5, 0.075])
txtBox = TextBox(graphBox, "Temperature: ")
txtBox.set_val(str(temp[temp.size - 1]) + " Degrees C")


#defining button
axes = plt.axes([0.81, 0.000001, 0.1, 0.075])
temp_labelbutton = Button(axes, "change units", color = "blue")
temp_labelbutton.on_clicked(on_click)
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
plt.connect('button_press_event', on_click)
while True:
    last_time = Time[Time.size - 1]
    

    fig.canvas.draw()
    fig.canvas.flush_events()
    sleep(1)
    a, Time = get_stored_temperatures(db)
    if Time[Time.size-1] == last_time:
        #display error message
        print("error message")

    #should convert array to float
    temp = np.array([])

    for i in a:
        if i == 'nil':
            temp = np.append(temp, None)
        else:
            temp = np.append(temp,float(i))

    if temp.size == 301:
        temp = np.delete(temp, 0)

    temp = np.flip(temp)
    line1.remove()
    line1, = ax.plot(x,temp, 'b-')
    

    #real time temperature
    if ("Temperature in C" in ax.get_ylabel()):
        txtBox.set_val(str(temp[temp.size - 1]) + " Degrees C")

    else:
        txtBox.set_val(str(temp[temp.size - 1]) + " Degrees F")

