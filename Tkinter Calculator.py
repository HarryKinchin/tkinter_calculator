#Calculator

#importing tkinter
from tkinter import *

#creating the gui
top = Tk()
top.title("Calculator")
top.geometry("200x200")

#subroutines for the off and reset buttons
def endProgram():
    exit()
def resetText():

#text box at the top
screen = Text(top, height=5)
screen.place(x=0,y=0)

#numbers 7-9
seven = Button(top, text="7", width=4)
seven.place(x=0,y=100)
eight = Button(top, text="8", width=4)
eight.place(x=40,y=100)
nine = Button(top, text="9", width=4)
nine.place(x=80,y=100)

#numbers 4-6
four = Button(top, text="4", width=4)
four.place(x=0,y=125)
five = Button(top, text="5", width=4)
five.place(x=40,y=125)
six = Button(top, text="6", width=4)
six.place(x=80,y=125)

#numbers 1-3
one = Button(top, text="1", width=4)
one.place(x=0,y=150)
two = Button(top, text="2", width=4)
two.place(x=40,y=150)
three = Button(top, text="3", width=4)
three.place(x=80,y=150)

#decimal, zero, and equals
decimal = Button(top, text=".", width=4)
decimal.place(x=0,y=175)
zero = Button(top, text="0", width=4)
zero.place(x=40,y=175)
equals = Button(top, text="=", width=4)
equals.place(x=80,y=175)

#Reset, and the operators
off = Button(top, text="OFF", width=4, command=endProgram)
off.place(x=120,y=100)
reset = Button(top, text="AC", width=4, command=resetText)
reset.place(x=160,y=100)
add = Button(top, text="+", width=4)
add.place(x=120,y=125)
minus = Button(top, text="-", width=4)
minus.place(x=120,y=150)
times = Button(top, text="x", width=4)
times.place(x=160,y=125)
divide = Button(top, text="÷", width=4)
divide.place(x=160,y=150)
div = Button(top, text="DIV", width=4)
div.place(x=120,y=175)
mod = Button(top, text="MOD", width=4)
mod.place(x=160,y=175)

top.mainloop()
