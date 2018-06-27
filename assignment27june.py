#assignment27june
import tkinter
#question1
from tkinter import *
box=Tk()
hi=Label(box,text='hi world')
hi.pack()
btn=Button(box,text='exit',command=" ")
btn.pack()
box.mainloop()

#question2
isha=tkinter.Tk()
def close():
    isha.destroy()
def write():
    print("hi")
isha.title("jai mata di")
isha.geometry("500x500")
butn=tkinter.Button(isha,text="exit",command=close)
btn1=tkinter.Button(isha,text="click",command=write)

butn.pack()
btn1.pack()
btn1.place(x=90,y=90)
butn.place(x=50,y=50)
isha.mainloop()

#Question3
from tkinter import *
xyz=Tk()
frame=Frame(xyz)
frame.pack()
lab=Label(xyz,text='working with frames')
lab.pack()
button1=Button(frame,text='exit',fg='blue')
button1.pack()
button2=Button(frame,text='change label',fg='red')
button2.pack()
mainloop()

#Question4
from tkinter import *
kite=Tk()
kite.geometry("100x100")
Label(kite,text='input').grid(row=0)
e1=Entry(kite)
e1.grid(row=0,column=1)
mainloop()