from tkinter import *
from tkinter.filedialog import askopenfile


def cmd1():
    lb1.configure(text="xyz")

def cmd2():
    a=askopenfile()

root =  Tk()
menu=Menu(root)
root.config(menu=menu) #root ka menu bar new menu assign kia h
filemenu=Menu(menu)
menu.add_cascade(label='file' , menu=filemenu)
filemenu.add_command(label='New' , command=cmd1)
filemenu.add_command(label='open',command=cmd2)
filemenu.add_separator()
filemenu.add_command(label='exit', command=root.quit)
lb1=Label(root,text="hello")
lb1.pack()
mainloop()


from tkinter import*
main=Tk()
ourMessage='this is our Message '
messageVar=Message(main,text=ourMessage)
messageVar.config(bg='blue')
main.mainloop()
messageVar.pack()

from tkinter import*
master=Tk()
w=Scale(master,from_=0,to=42)
w.pack()
w=Scalew=Scale(master,from_=0,to=200,orient=HORIZONTAL)
w.pack()
mainloop()


from tkinter import*
master=Tk()
w=Scale(master,from_=0,to=42)
