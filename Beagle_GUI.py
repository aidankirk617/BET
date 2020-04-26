## Imports
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import Menu
import webbrowser

## Functions
def selected(event):
     print("New Element Selected")

def encrypt(string, shift):

    cipher = ''
    for char in string:
        if char == ' ':
            cipher = cipher + char
        elif  char.isupper():
            cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)

    return cipher

def decrypt(string, shift):

    cipher = ''
    for char in string:
        if char == ' ':
            cipher = cipher + char
        elif  char.isupper():
            cipher = cipher + chr((ord(char) - shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) - shift - 97) % 26 + 97)

    return cipher

def Output():
    print("String= ", (string.get()))

    stringF = string.get()
    shiftF = shift.get()
    codeF = code.get()

    if (codeF == 'e'):
        cipher.set(encrypt(stringF, shiftF))
    else:
        cipher.set(decrypt(stringF, shiftF))

def Reset():
    rand.set("")
    string.set("")
    shift.set("")
    code.set("")
    cipher.set("")

def Exit():
    window.destroy()

## Window
window = tk.Tk()
window.geometry('500x700')

## Combo Box
comboExample = ttk.Combobox(window,
                            values=[
                                    "Caeser",
                                    "Reverse",
                                    "Transposition",
                                    "Viginere"])

comboExample.current(1)

comboExample.bind("<<ComboboxSelected>>", selected)


## String Variables
rand = StringVar()
string = StringVar()
shift = IntVar()
code = StringVar()
cipher = StringVar()

## Labels
strTxt = Label(window, text="String")
shiTxt = Label(window, text="Shift")
codTxt = Label(window, text="Code")
cipTxt = Label(window, text="Cipher")

## Textbox
e1 = tk.Entry(window)
e2 = tk.Entry(window)
e3 = tk.Entry(window)
e4 = tk.Entry(window)

## Buttons
btnOutput = Button(window, text="Output", command=selected)
btnReset = Button(window, text="Reset", command=selected)
btnExit = Button(window, text="Exit", command=selected)

## Grid Position
btnOutput.grid(column=0, row=12)
btnReset.grid(column=1, row=12)
btnExit.grid(column=2, row=12)
comboExample.grid(column=3, row=0)
strTxt.grid(column=0, row=6)
shiTxt.grid(column=0, row=7)
codTxt.grid(column=0, row=8)
cipTxt.grid(column=0, row=9)
e1.grid(row=6, column=1)
e2.grid(row=7, column=1)
e3.grid(row=8, column=1)
e4.grid(row=9, column=1)

## Main
window.mainloop()