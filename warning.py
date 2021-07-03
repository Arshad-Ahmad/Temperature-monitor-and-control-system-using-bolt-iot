import random
import tkinter as tk
from tkinter import *
from playsound import playsound
import threading

#######################################################################################
#Code block for the monitor display

def CreateWidgets():
    root.SignLabel = Label(root, text = "⚠", bg = "black", font=("Times, 200"))
    root.SignLabel.grid(row = 1, column = 2, padx = 350, pady = 10)
    showSign()

    root.TextLabel = Label(root, text = "WARNING", bg = "black", font=("Times, 205"))
    root.TextLabel.grid(row = 4, column = 0, columnspan=4, padx = 20, pady = 10)

    showText()


def showSign():
    x = format(random.randint(0, 255), '02x')
    y = format(random.randint(0, 255), '02x')
    z = format(random.randint(0, 255), '02x')

    color = "#"+str(x)+str(y)+str(z)
    root.SignLabel.config(fg=color) 
    root.SignLabel.after(105, showSign)


def showText():
    x = format(random.randint(0, 255), '02x')
    y = format(random.randint(0, 255), '02x')
    z = format(random.randint(0, 255), '02x')

    color = "#"+str(x)+str(y)+str(z)
    root.TextLabel.config(fg=color)
    root.TextLabel.after(10, showText)

def sound():
    playsound('warn.mp3')

 

if __name__ == '__main__':

    root = tk.Tk()
    root.title("ShoW")
    root.wm_attributes('-fullscreen','true')
    root.config(background = "black")
    root.after(15000, lambda: root.destroy())
    root.geometry('1900x1280')
    CreateWidgets()
    soundd = threading.Thread(target = sound)
    soundd.start()
    root.mainloop()

#########################################################################################
