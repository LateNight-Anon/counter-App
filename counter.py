from threading import Thread
from tkinter import Tk, Button, Label, messagebox
from time import sleep

def closeApp(isFatalError: bool) -> None:
    global appIsRunning
    appIsRunning = False
    if isFatalError: messagebox.showinfo(title = "fatal error", message = "file not found")
    app.destroy()
    exit()

def incrament() -> None:
    global count
    while appIsRunning:
        sleep(1)
        if isRunning:
            count += 1
            countLabel.configure(text = count)

def reset() -> None:
    global count
    count = 0
    countLabel.configure(text = count)

def startAndStop(val: bool) -> None:
    global isRunning
    isRunning = val

def load() -> None:
    global count
    try:
        with open("save.csv", 'r') as file:
                count = int(file.readline())
                countLabel.configure(text = count)
    except FileNotFoundError: closeApp(True)

def save() -> None:
    with open("save.csv", 'w') as file: file.write(str(count))

count: int = 0
isRunning: bool = False
appIsRunning: bool = True
Thread(target = incrament).start()

app = Tk()
app.title("counter")
app.resizable(width = False, height = False)
app.geometry("250x350")
app.configure(bg = "light grey")
app.protocol("WM_DELETE_WINDOW", lambda: closeApp(False))
Label(text = "counter", bg = "light grey", font = ("Arial", 35)).place(x = 40, y = 10)
countLabel = Label(text = count, bg = "light grey", font = ("Arial", 35))
countLabel.place(x = 105, y = 70)
Button(text = "start", font = ("Arial", 15), borderwidth = 2, relief = "solid", command = lambda: startAndStop(True)).place(x = 20, y = 200)
Button(text = "pause", font = ("Arial", 15), borderwidth = 2, relief = "solid", command = lambda: startAndStop(False)).place(x = 90, y = 200)
Button(text = "reset", font = ("Arial", 15), borderwidth = 2, relief = "solid", command = reset).place(x = 170, y = 200)
Button(text = "save", font = ("Arial", 15), borderwidth = 2, relief = "solid", command = save).place(x = 50, y = 250)
Button(text = "load", font = ("Arial", 15), borderwidth = 2, relief = "solid", command = load).place(x = 135, y = 250)

app.mainloop()
