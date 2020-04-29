## Imports
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import Menu
import webbrowser

## Window
window = tk.Tk()
window.geometry('600x220')
window.title("Beagle Beta (Build 0.01)")

## String Variables
rand = StringVar()
string = StringVar()
shift = IntVar()
cipher = StringVar()
var1 = tk.IntVar()
var2 = tk.IntVar()

## Combo Box
cb = ttk.Combobox(window,
                            values=[
                                    "Caeser",
                                    "Reverse",
                                    "Transposition",
                                    "Viginere"])

cb.current(1)

## Functions
def donothing():
   filewin = Toplevel(window)
   button = Button(filewin, text="Do nothing button")
   button.pack()

def selected(event):
     print("New Element Selected")

def cEnc(string, shift):

    cipher = ''
    for char in string:
        if char == ' ':
            cipher = cipher + char
        elif  char.isupper():
            cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)

    return cipher

def cDec(string, shift):

    cipher = ''
    for char in string:
        if char == ' ':
            cipher = cipher + char
        elif  char.isupper():
            cipher = cipher + chr((ord(char) - shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) - shift - 97) % 26 + 97)

    return cipher

def split_len(seq, length):                                                     #Transposition
    return [seq[i:i + length] for i in range(0, len(seq), length)]

def tEnc(shift, string):

    order = {
        int(val): num for num, val in enumerate(shift)
    }

    ciphertext = ''
    for index in sorted(order.keys()):
        for part in split_len(string, len(shift)):
            try:
                ciphertext += part[order[index]]
            except IndexError:
                continue

def rEnc(string, cipher):

    p1 = string

    cipher = ''

    i = len(p1) - 1

    while i >= 0:

        cipher = cipher + p1[i]

        i = i - 1

    return cipher

def rDec(string, cipher):

    cipher = ''

    i = len(string) + 1

    while i <= 0:

        cipher = cipher+ string[i]

        i = i + 1

    return cipher

## Output
def output():
    if cb.get() == "Caeser":
        print("String= ", (string.get()))

        stringF = string.get()
        shiftF = shift.get()

        if (var1.get() == 1) & (var2.get() == 0):
            cipher.set(cEnc(stringF, shiftF))
        elif (var1.get() == 0) & (var2.get() == 1):
            cipher.set(cDec(stringF, shiftF))
        elif (var1.get() == 0) & (var2.get() == 0):
            print("Please Select a Cipher")
        else:
            print("Please Select a Cipher")


    if cb.get() == "Reverse":
        print("String= ", (string.get()))

        stringF = string.get()
        cipherF = shift.get()

        if (var1.get() == 1) & (var2.get() == 0):
            cipher.set(rEnc(stringF, cipherF))
        elif (var1.get() == 0) & (var2.get() == 1):
            cipher.set(rDec(stringF, cipherF))
        elif (var1.get() == 0) & (var2.get() == 0):
            print("Please Select a Cipher")
        else:
            print("Please Select a Cipher")

    elif cb.get() == "Transposition":
        print("String= ", (string.get()))

        stringF = string.get()
        shiftF = shift.get()

        if (var1.get() == 1) & (var2.get() == 0):
            cipher.set(tEnc(shiftF, stringF))
        elif (var1.get() == 0) & (var2.get() == 1):
            print("Not yet a possibility")
        elif (var1.get() == 0) & (var2.get() == 0):
            print("Please Select a Cipher")
        else:
            print("Please Select a Cipher")


def Reset():
    rand.set("")
    string.set("")
    shift.set("")
    cipher.set("")

def Exit():
    window.destroy()

## Menu Bar
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=Exit)
filemenu.add_command(label="Reset", command=Reset)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

## Labels
lblStr = Label(window, text="String")
lblShi = Label(window, text="Shift")
lblOut = Label(window, text="Output")
lblTitle = Label(window, text="Beagle", relief="solid",
width=20,font=("arial",19,"bold"))

## Textbox
txtStr = tk.Entry(window, textvariable = string, justify = 'right')
txtShi = tk.Entry(window, textvariable = shift, justify = 'right')
txtOut = tk.Entry(window, textvariable = cipher, justify = 'right')

## Buttons
btnOutput = Button(window, text="Output", command= output)
eChk = tk.Checkbutton(window, text='Encrypt',variable=var1, onvalue=1, offvalue=0, command=output).grid(row=1, column=3)
dChk = tk.Checkbutton(window, text='Decrypt',variable=var2, onvalue=1, offvalue=0, command=output).grid(row=2, column=3)

## Grid Position
cb.grid(column=1, row=4)
lblTitle.grid(column=0, row=0)
lblStr.grid(column=0, row=1)
lblShi.grid(column=0, row=2)
lblOut.grid(column=0, row=3)
txtStr.grid(row=1, column=1)
txtShi.grid(row=2, column=1)
txtOut.grid(row=3, column=1)

## Main
print("    ____                   __    ")
print("   / __ )___  ____ _____ _/ /__      ")
print("  / __  / _ \/ __ `/ __ `/ / _ \  ")
print(" / /_/ /  __/ /_/ / /_/ / /  __/ ")
print("/_____/\___/\__,_/\__, /_/\___/")
print("                   /____/              ")
window.config(menu=menubar)
window.mainloop()