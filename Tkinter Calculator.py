#Tkinter Calculator

#importing tkinter
from tkinter import *

#creating the gui
top = Tk()
top.title("Calculator")
top.geometry("575x525")

#subroutines for button presses
def endProgram():
    exit()
    
def resetText():
    screen.config(text="")

def undoText():
    contains = str(screen.cget("text"))
    containBack = contains[0:len(contains)-1]
    screen.config(text=containBack)
    
def numOpPressed(numOp):
    contains =str(screen.cget("text"))
    screen.config(text=contains + numOp)
    
def equalsPressed():
    screen.config(text=float(eval(screen.cget("text"))))

#text box at the top
screen = Label(top, height=5, font="48")
screen.place(x=0,y=0)

#numbers 7-9
seven = Button(top, text="7", width=15, height=5, command=lambda:numOpPressed("7"))
seven.place(x=0,y=100)
eight = Button(top, text="8", width=15, height=5, command=lambda:numOpPressed("8"))
eight.place(x=115,y=100)
nine = Button(top, text="9", width=15, height=5, command=lambda:numOpPressed("9"))
nine.place(x=230,y=100)

#numbers 4-6
four = Button(top, text="4", width=15, height=5, command=lambda:numOpPressed("4"))
four.place(x=0,y=185)
five = Button(top, text="5", width=15, height=5, command=lambda:numOpPressed("5"))
five.place(x=115,y=185)
six = Button(top, text="6", width=15, height=5, command=lambda:numOpPressed("6"))
six.place(x=230,y=185)

#numbers 1-3
one = Button(top, text="1", width=15, height=5, command=lambda:numOpPressed("1"))
one.place(x=0,y=270)
two = Button(top, text="2", width=15, height=5, command=lambda:numOpPressed("2"))
two.place(x=115,y=270)
three = Button(top, text="3", width=15, height=5, command=lambda:numOpPressed("3"))
three.place(x=230,y=270)

#decimal, zero, and equals
decimal = Button(top, text=".", width=15, height=5, command=lambda:numOpPressed("."))
decimal.place(x=0,y=355)
zero = Button(top, text="0", width=15, height=5, command=lambda:numOpPressed("0"))
zero.place(x=115,y=355)
equals = Button(top, text="=", width=15, height=5, command=equalsPressed)
equals.place(x=230,y=355)

#reset, backspace, and quit
off = Button(top, text="OFF", width=15, height=5, command=endProgram)
off.place(x=0,y=440)
reset = Button(top, text="AC", width=15, height=5, command=resetText)
reset.place(x=115,y=440)
back = Button(top, text="⌫", width=15, height=5, command=undoText)
back.place(x=230, y=440)

#operators
add = Button(top, text="+", width=15, height=5, command=lambda:numOpPressed("+"))
add.place(x=345,y=100)
minus = Button(top, text="-", width=15, height=5, command=lambda:numOpPressed("-"))
minus.place(x=460,y=100)
times = Button(top, text="x", width=15, height=5, command=lambda:numOpPressed("*"))
times.place(x=345,y=185)
divide = Button(top, text="÷", width=15, height=5, command=lambda:numOpPressed("/"))
divide.place(x=460,y=185)
exponent = Button(top, text="^", width=15, height=5, command=lambda:numOpPressed("**"))
exponent.place(x=345,y=270)
oBracket= Button(top, text="(", width=15, height=5, command=lambda:numOpPressed("("))
oBracket.place(x=345,y=355)
cBracket = Button(top, text=")", width=15, height=5, command=lambda:numOpPressed(")"))
cBracket.place(x=460,y=355)
div = Button(top, text="DIV", width=15, height=5, command=lambda:numOpPressed("//"))
div.place(x=345,y=440)
mod = Button(top, text="MOD", width=15, height=5, command=lambda:numOpPressed("%"))
mod.place(x=460,y=440)

#tkinter mainloop
top.mainloop()
