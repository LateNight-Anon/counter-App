from threading import Thread
from tkinter import Tk, Button, Label
from time import sleep

def incrament() -> None:
    global count
    while True:
        sleep(1)
        if isRunning:
            count += 1
            countLabel.configure(text=count)

def reset() -> None:
    global count
    count = 0
    countLabel.configure(text=count)

def start() -> None:
    global isRunning
    isRunning = True

def stop() -> None:
    global isRunning
    isRunning = False

def load() -> None:
    global count
    with open("save.csv", 'r') as file:
        try:
            count = int(file.readline())
            countLabel.configure(text=count)
        except Exception:
            print("file has been tampered with")
            exit()

def save() -> None:
    with open("save.csv", 'w') as file:
        file.write(str(count))
        
count: int = 0
isRunning: bool = False
thread = Thread(target=incrament)
thread.start()

app = Tk()
app.title("counter")
app.resizable(width=False, height=False)
app.geometry("250x350")
app.configure(bg="light grey")
Label(text="counter", bg="light grey", font=("Arial",35)).place(x=40, y=10)
countLabel = Label(text=count, bg="light grey", font=("Arial", 35))
countLabel.place(x=105, y=70)
Button(text="start", font=("Arial", 15), borderwidth=2, relief="solid",command=start).place(x=20,y=200)
Button(text="pause", font=("Arial", 15), borderwidth=2, relief="solid",command=stop).place(x=90,y=200)
Button(text="reset", font=("Arial", 15), borderwidth=2, relief="solid",command=reset).place(x=170,y=200)
Button(text="save", font=("Arial", 15), borderwidth=2, relief="solid",command=save).place(x=50,y=250)
Button(text="load", font=("Arial", 15), borderwidth=2, relief="solid",command=load).place(x=135,y=250)

app.mainloop()
