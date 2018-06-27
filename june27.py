#import tkinter as tk
#top=tk.Tk() #top is containers's name
#top.title("isha")
#top.geometry("100x100")
#btn=tk.Button(top,text="abc",command="") #to make a button
#btn.pack()
#btn.place(x=50,y=50)
#top.mainloop() #should always be in the end

from tkinter import *
#here * initialises all variables
master=Tk()
w=Canvas(master,width=40,height=60)
#w.pack()
#Canvas_height=20
#Canvas_width=200
#y=int(Canvas_height/2)
#w.create_line(0,y,Canvas_width,y)\
#var1=IntVar()
#Checkbutton(master, text='male', variable=var1).grid(row=0)
#var2=IntVar()
#Checkbutton(master, text='female', variable=var2).grid(row=1)
#w.mainloop()


#Label(master,text='first name').grid(row=0)
#Label(master,text='last name').grid(row=1)
#e1=Entry(master)
#e2=Entry(master)
#e1.grid(row=0,column=1)
#e2.grid(row=1,column=1)
#w.mainloop()



root=Tk()
frame=Frame(root)
frame.pack()
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)
redbutton=Button(frame, text='red' , fg='red')
redbutton.pack(side=LEFT)
redbutton=Button(frame, text='yello' , fg='yellow')
redbutton.pack(side=LEFT)
bluebutton=Button(frame, text='blue' , fg='blue')
bluebutton.pack(side=LEFT)
root.mainloop()







