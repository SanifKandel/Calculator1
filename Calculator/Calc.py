#import tkinter from built-in namespace or library
from tkinter import *
root = Tk()

#Customizing Tkinter Windows
root.resizable(0,0)
root.title("Calculator")

#Creating Display Screen of the Calculator
value = StringVar() #It manage the Value of the widget i.e Entry Value
screen = Entry(root, width = 40, borderwidth = 10,font =("Verdana",10,"bold"),textvariable=value,justify= "right",
               highlightbackground = "black",highlightthickness = 4 )
screen.grid(row = 0, column = 0 ,columnspan = 16 ,padx = 15,pady = 10,ipadx = 15, ipady =10)

#Defining Button Function
current = ""
def buttonClick(exp):
    global current
    current = current +str(exp)
    value.set(current)
def buttonClear():
    global current
    current = ""
    value.set("")
def button_Equal():
    global current
    result = str(eval(current)) #Eval function takes string as an expression and determine its value.
    value.set(result)
    current = ""



#Creating Buttons                       #lamda is an anonymous function with only one expression
button7 = Button(root, text = "7",borderwidth=5,fg ="orange",command = lambda : buttonClick("7"))
button8 = Button(root, text = "8",borderwidth=5,fg ="orange",command = lambda : buttonClick("8"))
button9 = Button(root, text = "9",borderwidth=5,fg ="orange",command = lambda : buttonClick("9"))
buttonAC = Button(root, text = "AC",borderwidth=5,bg= "#404040",fg ="black",command = lambda : buttonClear())
button4 = Button(root, text = "4" ,borderwidth=5,fg ="orange",command = lambda : buttonClick("4"))
button5 = Button(root, text = "5" ,borderwidth=5,fg ="orange",command = lambda : buttonClick("5"))
button6 = Button(root, text = "6" ,borderwidth=5,fg ="orange",command = lambda : buttonClick("6"))
button1 = Button(root, text = "1" ,borderwidth=5,fg ="orange",command = lambda : buttonClick("1"))
button2 = Button(root, text = "2" ,borderwidth=5,fg ="orange",command = lambda : buttonClick("2"))
button3 = Button(root, text = "3" ,borderwidth=5,fg ="orange",command = lambda : buttonClick("3"))
button0 = Button(root, text = "0" ,borderwidth=5,fg ="orange",command = lambda : buttonClick("0"))
buttonPoint = Button(root, text = "." ,borderwidth=5,fg ="orange",command = lambda : buttonClick('.'))
buttonPlus = Button(root, text = "+" ,borderwidth=5,fg ="black",command = lambda : buttonClick("+"))
buttonMinus = Button(root, text = "-" ,borderwidth=5,fg ="black",command = lambda : buttonClick("-"))
buttonMul = Button(root, text = "x" ,borderwidth=5,fg ="black",command = lambda : buttonClick("*"))
buttonDiv = Button(root, text = "÷" ,borderwidth=5,fg ="black",command = lambda : buttonClick("/"))
buttonEqual = Button(root, text = "=" ,borderwidth=5,fg ="black",command = lambda : button_Equal())

#Placing Buttons
button7.grid(row = 1,column = 1,ipadx = 20,ipady = 10,pady = 5)
button8.grid(row = 1,column = 2,ipadx = 20,ipady = 10,pady = 5)
button9.grid(row = 1,column = 3,ipadx = 20,ipady = 10,pady = 5)
buttonAC.grid(row = 1,column = 10,columnspan = 2,ipadx = 52,ipady = 10,pady = 5)
button4.grid(row = 2,column = 1,ipadx = 20,ipady = 10,pady = 5)
button5.grid(row = 2,column = 2,ipadx = 20,ipady = 10,pady = 5)
button6.grid(row = 2,column = 3,ipadx = 20,ipady = 10,pady = 5)
button1.grid(row = 3,column = 1,ipadx = 20,ipady = 10,pady = 5)
button2.grid(row = 3,column = 2,ipadx = 20,ipady = 10,pady = 5)
button3.grid(row = 3,column = 3,ipadx = 20,ipady = 10,pady = 5)
button0.grid(row = 4,column = 1,ipadx = 20,ipady = 10,pady = 5)
buttonPoint.grid(row = 4,column = 2,ipadx = 23,ipady = 10,pady = 5)
buttonPlus.grid(row = 2,column = 10,ipadx = 20,ipady = 10,pady = 5)
buttonMinus.grid(row = 2,column = 11,ipadx = 20,ipady = 10,pady = 5)
buttonMul.grid(row = 3,column = 10,ipadx = 20,ipady = 10,pady = 5)
buttonDiv.grid(row = 3,column = 11,ipadx = 20,ipady = 10,pady = 5)
buttonEqual.grid(row = 4,column = 10,columnspan = 2,ipadx = 52,ipady = 10,pady = 5)

#MainLoop runs the program infinity times
root.mainloop()