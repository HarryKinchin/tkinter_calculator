#Tkinter Calculator

#importing tkinter
from tkinter import *

#creating the gui
top = Tk()
top.title("Calc")
top.geometry("200x200")

#subroutines for button presses
def endProgram():
    exit()
def resetText():
    screen.config(text="")
def numOpPressed(numOp):
    contains =str(screen.cget("text"))
    screen.config(text=contains + numOp)

#text box at the top
screen = Label(top, height=5)
screen.place(x=0,y=0)

#numbers 7-9
seven = Button(top, text="7", width=4, lambda: command=numOpPressed("7"))
seven.place(x=0,y=100)
eight = Button(top, text="8", width=4, lambda: command=numOpPressed("8"))
eight.place(x=40,y=100)
nine = Button(top, text="9", width=4, lambda: command=numOpPressed("9"))
nine.place(x=80,y=100)

#numbers 4-6
four = Button(top, text="4", width=4, lambda: command=numOpPressed("4"))
four.place(x=0,y=125)
five = Button(top, text="5", width=4, lambda: command=numOpPressed("5"))
five.place(x=40,y=125)
six = Button(top, text="6", width=4, lambda: command=numOpPressed("6"))
six.place(x=80,y=125)

#numbers 1-3
one = Button(top, text="1", width=4, lambda: command=numOpPressed("1"))
one.place(x=0,y=150)
two = Button(top, text="2", width=4, lambda: command=numOpPressed("2"))
two.place(x=40,y=150)
three = Button(top, text="3", width=4, lambda: command=numOpPressed("3"))
three.place(x=80,y=150)

#decimal, zero, and equals
decimal = Button(top, text=".", width=4, lambda: command=numOpPressed("."))
decimal.place(x=0,y=175)
zero = Button(top, text="0", width=4, lambda: command=numOpPressed("0"))
zero.place(x=40,y=175)
equals = Button(top, text="=", width=4)
equals.place(x=80,y=175)

#reset, and quit
off = Button(top, text="OFF", width=4, lambda: command=endProgram)
off.place(x=120,y=100)
reset = Button(top, text="AC", width=4, lambda: command=resetText)
reset.place(x=160,y=100)

#operators
add = Button(top, text="+", width=4, lambda: command=numOpPressed("+"))
add.place(x=120,y=125)
minus = Button(top, text="-", width=4, lambda: command=numOpPressed("-"))
minus.place(x=120,y=150)
times = Button(top, text="x", width=4, lambda: command=numOpPressed("*"))
times.place(x=160,y=125)
divide = Button(top, text="÷", width=4, lambda: command=numOpPressed("/"))
divide.place(x=160,y=150)
div = Button(top, text="DIV", width=4, lambda: command=numOpPressed("//"))
div.place(x=120,y=175)
mod = Button(top, text="MOD", width=4, lambda: command=numOpPressed("%"))
mod.place(x=160,y=175)

#tkinter mainloop
top.mainloop()
