from tkinter import *
from tkinter import font
import tkinter.messagebox
from turtle import title
from user1 import *
from user2 import *
from user3 import *

window = Tk()
window.title("USER LOGIN PAGE")
window.config(bg= "green")
window.geometry("450x450")


label1 = Label(window,text = "FIRST NAME",font= ("Calibri Bold",20)).place(x=150,y=200)
label2= Label(window, text= "SECOND NAME",font = ("Calibri Bold",20)).place(x=150,y=250)

f_name = StringVar()
f_name = Entry(window,width=20,bg= "yellow",borderwidth=3,textvariable = f_name)
f_name.place(x=400,y=200)


s_name = StringVar()
s_name = Entry(window,width=20,bg= "red",borderwidth=3,textvariable= s_name)
s_name.place(x=400,y=250)

# input1 = StringVar()
# f_name = Text(window,width= 20,bg ="orange").place(x=400,y=200)
# input2 = StringVar()
# s_name = Text(window,width= 20,bg ="blue").place(x=400,y=250)



def open_poppup_error():
    top = Toplevel(window)
    top.geometry("300x300")
    top.config(bg= "white")
    Label(top, text= "User Not Available in system yet!",font = ("Arial",20)).place(x=200,y=200)

def login():
    if (f_name.get() =="Mercy")and (s_name.get() =="Muiruri"):
       window1()

    elif f_name.get() == "Jonathan" and s_name.get() == "Ageyo":
        window2()

    elif f_name.get() == "Lilian" and s_name.get() == "Cheruyiot":
        window3()
    else:
        open_poppup_error()
        

btn = Button(window, text= "LOGIN",fg ="red", bg="green",command = login).place(x=200,y=320)

label3 = Label(window, text="Users available are:Mercy Muiruri,Jonathan Ageyo and Lilian Cheruyiot").place(x=300,y=400)

window.mainloop()