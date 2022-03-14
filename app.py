import tkinter, socketio, websocket, threading
from tkinter import messagebox

class Handle():
    def __init__(self):
        self.client = socketio.Client()
        thread = threading.Thread(target=self.aftershock)
        thread.start()

    def aftershock(self):
        def connect():
            print("connection established!")

        try:
            self.client.connect("http://localhost:5000")
        except:
            messagebox.showerror("Connection Error!", "There was a problem connection you to the network, please try again later.")

handle = Handle()

class Draw():
    def __init__(self):
        list = root.pack_slaves()
        for i in list:
            i.pack_forget()

    def main_screen():
        label




root = tkinter.Tk()

label = tkinter.Label(root, text="Connecting you to the network, please wait..")
label.pack()

root.mainloop()