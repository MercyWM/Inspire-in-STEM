from tkinter import *
from fp import *
from fp2 import *
from fp3 import *
from fp4 import *

def displaydeposit():
    window = Tk()
    window.title("MONEY AFTER DEPOSIT")
    window.config(bg="blue")
    window.geometry("600x600")
    new_amount = int(original_amount.get())+int(deposited_amount.get())
    return new_amount
    lbl= Label(window,bg="red",text="Your new account balance is " + str(new_amount),font=("Arial",25)).place(x=300,y=150)
    window.mainloop()