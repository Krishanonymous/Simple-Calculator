from tkinter import *

root=Tk()
root.title('Simple Calculator')
root.iconbitmap('calculator.ico.ico')

MyEntry=Entry(root,width=47)
MyEntry.grid(row=0,column=0,columnspan=3)
#display
def display(n):
    MyEntry.insert(END,n)
#clear
def clear():
    MyEntry.delete(0,END)
#Backspace
def Backspace():
    a=MyEntry.get()
    b=''
    for i in range(0,len(a)-1):
        b+=a[i]
    MyEntry.delete(0,END)
    MyEntry.insert(0,b)
#add
def add():
    global ct
    ct=1
    a=MyEntry.get()
    global add
    add=int(a)
    MyEntry.delete(0,END)
#subtract
def sub():
    global ct
    ct=2
    a=MyEntry.get()
    global sub
    sub=int(a)
    MyEntry.delete(0,END)
#multiply
def mult():
    global ct
    ct=3
    a=MyEntry.get()
    global mult
    mult=int(a)
    MyEntry.delete(0,END)
#division
def div():
    global ct
    ct=4
    a=MyEntry.get()
    global div
    div=int(a)
    MyEntry.delete(0,END)
#equal to
def equal():
    global ct
    b=MyEntry.get()
    if ct==1:
        global add
        add+=int(b)
        MyEntry.delete(0,END)
        MyEntry.insert(0,add)
    if ct==2:
        global sub
        sub-=int(b)
        MyEntry.delete(0,END)
        MyEntry.insert(0,sub)
    if ct==3:
        global mult
        mult=mult*int(b)
        MyEntry.delete(0,END)
        MyEntry.insert(0,mult)
    if ct==4:
        global div
        div=div/int(b)
        MyEntry.delete(0,END)
        MyEntry.insert(0,div)
#Clear
MyButtons=Button(root,text='Clear',padx=30,pady=10,command=clear).grid(row=1,column=0)
#Backspace
MyButtons=Button(root,text='Backspace',padx=65,pady=10,command=Backspace).grid(row=1,column=1,columnspan=2)    
#1
MyButtons=Button(root,text='1',padx=40,pady=10,command=lambda: display(1)).grid(row=2,column=0)
#2
MyButtons=Button(root,text='2',padx=40,pady=10,command=lambda: display(2)).grid(row=2,column=1)
#3
MyButtons=Button(root,text='3',padx=40,pady=10,command=lambda: display(3)).grid(row=2,column=2)
#4
MyButtons=Button(root,text='4',padx=40,pady=10,command=lambda: display(4)).grid(row=3,column=0)
#5
MyButtons=Button(root,text='5',padx=40,pady=10,command=lambda: display(5)).grid(row=3,column=1)
#6
MyButtons=Button(root,text='6',padx=40,pady=10,command=lambda: display(6)).grid(row=3,column=2)
#7
MyButtons=Button(root,text='7',padx=40,pady=10,command=lambda: display(7)).grid(row=4,column=0)
#8
MyButtons=Button(root,text='8',padx=40,pady=10,command=lambda: display(8)).grid(row=4,column=1)
#9
MyButtons=Button(root,text='9',padx=40,pady=10,command=lambda: display(9)).grid(row=4,column=2)
#0
MyButtons=Button(root,text='0',padx=40,pady=10,command=lambda: display(0)).grid(row=5,column=0)
#+
MyButtons=Button(root,text='+',padx=40,pady=10,command=add).grid(row=5,column=1)
#-
MyButtons=Button(root,text='-',padx=40,pady=10,command=sub).grid(row=5,column=2)
#X
MyButtons=Button(root,text='X',padx=40,pady=10,command=mult).grid(row=6,column=0)
#/
MyButtons=Button(root,text='/',padx=40,pady=10,command=div).grid(row=6,column=1)
#=
MyButtons=Button(root,text='=',padx=40,pady=10,command=equal).grid(row=6,column=2)
    
