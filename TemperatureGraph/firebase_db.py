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
    db.child("Temperature").set(temp)

if __name__ == "__main__":
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    current_temp = get_temp(db)
    print(current_temp)
    set_temp(db, 10)
    