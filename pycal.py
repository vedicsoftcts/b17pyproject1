from tkinter import *
import tkinter   
from tkinter import messagebox

root=Tk()
root.title("Simple Calculator")
root.geometry('300x300')
#commands
def on_add():
    onadd= A.get()+B.get()
    print(f"A+B = {onadd}")
    return messagebox.showinfo("ADD",message=f"A+B = {onadd}")
def on_sub():
    onsub= A.get()-B.get()
    print(f"A-B = {onsub}")
    return messagebox.showinfo("Subtract",message=f"A-B = {onsub}")
def on_multi():
    onmulti=A.get() * B.get()
    print(f"AxB = {onmulti}")
    return messagebox.showinfo("Multiply",message=f"AxB = {onmulti}")
def on_clear():
    A.set("")
    B.set("")

#variable
A=tkinter.IntVar()
B=tkinter.IntVar()
#labels
Label(root,text="Welcome",borderwidth=15,justify=CENTER).grid()
Label(root,text="A").grid(row=1,column=0)
Label(root,text="B").grid(row=2,column=0)
#entry
Entry(root,textvariable=A,width=10,borderwidth=5).grid(row=1,column=1)
Entry(root,textvariable=B,width=10,borderwidth=5).grid(row=2,column=1)
#button
Add_Button=Button(root,text="ADD",command=on_add).grid(row=3,column=0)
Sub_Button=Button(root,text="Subtract",command=on_sub).grid(row=3,column=1)
Multi_Button=Button(root,text="Mutliply",command=on_multi).grid(row=3,column=2)

Clear_Button=Button(root,text="Clear",command=on_clear).grid()

root.mainloop()