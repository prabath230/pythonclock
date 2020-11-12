
from tkinter import *
from tkinter.dialog import *
from time import strftime

root = Tk()
root.title("timer")

def time():
    string = strftime('%-I:%M:%S: %p')
    lable.config(text=string)
    lable.after(1000, time)

lable = Label(root, background="black", foreground="cyan")
lable.pack(anchor='center')
time()

mainloop()