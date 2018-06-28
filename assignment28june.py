my_dict = {'name':'xyz', 'phno':"9876543210 "} #dictionary
from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter import messagebox
box = Tk()
box.title("Dictionary")
box.geometry("600x500")
scrollbar = Scrollbar(box)
scrollbar.pack( side = RIGHT, fill = Y )

list = Listbox(box, yscrollcommand = scrollbar.set)
list.insert(END, "NAME- "+ my_dict['name'])
list.insert(END, "PHONENO- " + str(my_dict['phno']))

list.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = list.yview )

lb=Label(box,text="GUI")
lb.pack()

def cmd():
    root = Tk()
    root.title("*Insert details*")
    root.geometry("500x900")
    name_label = Label(root, text="Updated name")
    name_label.pack()

    name_text_box =(Entry(root, bd=1))
    name_text_box.pack()

    ph_label = Label(root, text="Updated phn number ")
    ph_label.pack()

    ph_text_box =(Entry(root, bd=1))
    ph_text_box.pack()

    def add_new():
        name=name_text_box.get()
        print(name)
        phn=ph_text_box.get()
        print(phn)
        my_dict = {'name': name, 'phno':phn}
        label1 = Label(root, text="information entered to the dictionary")
        label1.pack()

    enter_button = Button(root, text="Add", command=add_new)
    enter_button.pack()
    root.mainloop()

print(my_dict['name'])
print(my_dict.get('phno'))

import tkinter as tk
frame= tk.Frame(box)
frame.pack()
slogan = tk.Button(frame,text="Enter New Details",bg='turquoise',fg='black',command=cmd)
slogan.pack(side=tk.LEFT)

butn = tk.Button(frame,text="QUIT",fg="magenta",bg='white',command=quit)
butn.pack(side=tk.LEFT)
mainloop()