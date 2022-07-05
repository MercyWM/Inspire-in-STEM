

from tkinter import *
from fp import *
from fp2 import *
from fp3 import *
from fp4 import *

window = Tk()
window.title("FINANCEMASTER")
window.config(bg="purple")
window.geometry("650x500")

# the main labels
Label(window, bg="violet", text="USERNAME",font=("Calibri Bold Italics",26)).place(x=50,y=100)
Label(window,bg="violet",  text="USEREMAIL",font=("Calibri Bold Italics",26)).place(x=50,y=150)
Label(window,bg="violet",  text="PASSWORD",font=("Calibri Bold Italics",26)).place(x=50,y=200)


# THE ENTRY BOXES
name_entry = StringVar()
name_entry = Entry(window, width=50,bg="turquoise")
name_entry.place(x=300,y=100)

email_entry = StringVar()
email_entry = Entry(window, width=50,bg="turquoise")
email_entry.place(x=300,y=150)

#inputting the password.

import random
character = (str(name_entry)+str(email_entry))
password = ""
for x in range(0,8):
    password = password + random.choice(character)
print(password)


password_entry = StringVar()
password_entry = Entry(window, width=50,bg="turquoise")
password_entry.place(x=300,y=200)


# error page
def error():
    window = Tk()
    window.title("ERROR PAGE")
    window.config(bg="grey")
    window.geometry("600x600")
    Label(window,text="Wrong password entered. Check your VS Code terminal for the generated password and input it again!").place(x=300,y=300)
    window.mainloop()
    
    
    
# authorization
def authorize():
    if password_entry.get() == password:
        fp2()
    else:
        error()


def fp2():
    window = Tk()
    window.title("FINANCE MASTER")
    window.config(bg="red")
    window.geometry("600x600")
    Label(window, text="Choose the option you need",font=("Arial",25)).place(x=100,y=150)
    Button(window,text="ALL RECORDS",bg="yellow").place(x=100,y=300)
    Button(window,text="DEPOSITS",bg="yellow",command=deposits).place(x=100,y=400)
    Button(window,text="WITHDRAWALS",bg="yellow").place(x=100,y=500)
    window.mainloop()
    
# creating the LOGIN BUTTON
Button(window,text="LOGIN",bg="green",fg="red",width = 70,borderwidth= 20,command = authorize).place(x=100,y=350)

window.mainloop()