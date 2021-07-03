from tkinter import *
from tkinter.ttk import *
from boltiot import Bolt
import json, time

a_key = "607bfc05-098d-4571-80b3-9644261c0b30"
d_id = "BOLT1117077"
mybolt = Bolt(a_key, d_id)

root = Tk()
root.title('TEMPERATURE MONITOR')
root.wm_attributes('-fullscreen', 1)
root.configure(background = 'black')

l1 = Label(root, font = ('Times', 200, 'bold'), background = 'black', foreground = 'white')
l1.pack(ipadx = 1, ipady = 900)

l2 = Label(root, font = ('Times', 200, 'bold'), background = 'black', foreground = 'white')
l2.pack(ipadx = 1, ipady = 900)

def display():
    content = temp
    l1.config(text = content)
    l1.after(1000, display)
    l2.config(text = time)
    l2.after(1000, display)

def temperature():
    while True:
        response = mybolt.analogRead('A0')
        data = json.loads(response)
        res = int(data['value'])
        temp = (100*res)/1024
        time.sleep(1000)
    return temp

def time():
    string = strftime('%H:%M:%S %p')
    l1.config(text = string)
    l1.after(1000, time)

temperature()
display()
time()
mainloop()


   
                                 
