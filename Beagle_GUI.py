## Imports/Globals
from tkinter import *
from tkinter import Menu
import webbrowser

## Menu Bar
window = Tk()
window.title("Beagle (Build 0.0.1)")
menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='New')
new_item.add_command(label='Open')
new_item.add_separator()
new_item.add_command(label='Exit')
menu.add_cascade(label='File', menu=new_item)
menu.add_cascade(label='View', menu=new_item)
menu.add_cascade(label='Window', menu=new_item)
menu.add_cascade(label='Tools', menu=new_item)
menu.add_cascade(label='Help', menu=new_item)

## Window Size
window.geometry('300x200')

## Textbox
lbl = Label(window, text="Caeser Encryption")
bbl = Label(window, text="Caeser Decryption")
lbl.grid(column=0, row=0)
bbl.grid(column=0, row=1)
txt = Entry(window,width=10)
txt.grid(column=1, row=0)
txt = Entry(window,width=10)
txt.grid(column=1, row=1)

## Buttons
def clicked():
    res = "This shit don't work yet lol"
    lbl.configure(text= res)
    webbrowser.open('https://www.youtube.com/watch?v=mFzrq0jpnZw')  # Divine Punishment
btn = Button(window, text="Encrypt", command=clicked)
btn.grid(column=2, row=0)
ctn = Button(window, text="Decrypt", command=clicked)
ctn.grid(column=2, row=1)

## Caeser Cipher

## RSA

## Reverse

## Transposition

## Affine

## Multiplicative

## Substitution

## Exit Loop
window.config(menu=menu)
window.mainloop()

## Executable