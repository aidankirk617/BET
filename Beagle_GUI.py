"""
Todo: Fix decryption features
Run other functions through
Work on graphical overhaul
"""

## Imports
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import Menu
import webbrowser

## Window
window = tk.Tk()
window.geometry('500x700')

## String Variables
rand = StringVar()
string = StringVar()
shift = IntVar()
code = StringVar()
cipher = StringVar()

## Combo Box
cb = ttk.Combobox(window,
                            values=[
                                    "Caeser",
                                    "Reverse",
                                    "Transposition",
                                    "Viginere"])

cb.current(1)

## Functions
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

def split_len(seq, length): #Transposition
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


def output():
    if cb.get() == "Caeser":
        print("String= ", (string.get()))

        stringF = string.get()
        shiftF = shift.get()
        codeF = code.get()

        if (codeF == 'e'):
            cipher.set(cEnc(stringF, shiftF))
        else:
            cipher.set(cDec(stringF, shiftF))

    if cb.get() == "Reverse":
        print("String= ", (string.get()))

        stringF = string.get()
        cipherF = shift.get()
        codeF = code.get()

        if (codeF == 'e'):
            cipher.set(rEnc(stringF, cipherF))
        elif (codeF == 'd'):
            cipher.set(rDec(stringF, cipherF))

    elif cb.get() == "Transposition":
        print("String= ", (string.get()))

        stringF = string.get()
        shiftF = shift.get()
        codeF = code.get()

        if (codeF == 'e'):
            cipher.set(tEnc(shiftF, stringF))
        else:
            print("Not yet a possibility")


def Reset():
    rand.set("")
    string.set("")
    shift.set("")
    code.set("")
    cipher.set("")

def Exit():
    window.destroy()

## Labels
lblStr = Label(window, text="String")
lblShi = Label(window, text="Shift")
lblCod = Label(window, text="Code")
lblOut = Label(window, text="Cipher")

## Textbox
txtStr = tk.Entry(window, textvariable = string, justify = 'right')
txtShi = tk.Entry(window, textvariable = shift, justify = 'right')
txtCod = tk.Entry(window, textvariable = code, justify = 'right')
txtOut = tk.Entry(window, textvariable = cipher, justify = 'right')

## Buttons
btnOutput = Button(window, text="Output", command= output)
btnReset = Button(window, text="Reset", command= Reset)
btnExit = Button(window, text="Exit", command= Exit)

## Grid Position
btnOutput.grid(column=0, row=12)
btnReset.grid(column=1, row=12)
btnExit.grid(column=2, row=12)
cb.grid(column=3, row=0)
lblStr.grid(column=0, row=6)
lblShi.grid(column=0, row=7)
lblCod.grid(column=0, row=8)
lblOut.grid(column=0, row=9)
txtStr.grid(row=6, column=1)
txtShi.grid(row=7, column=1)
txtCod.grid(row=8, column=1)
txtOut.grid(row=9, column=1)

## Main
window.mainloop()