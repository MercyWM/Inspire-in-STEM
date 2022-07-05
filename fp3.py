from tkinter import *
from fp import *
from fp2 import *
from fp3 import *
from fp4 import *

def deposits():
    window = Tk()
    window.title("MONEY IN")
    window.config(bg="green")
    window.geometry("600x600")
    Label(window, text="Enter the money deposited",font=("Arial",25)).place(x=80,y=150)
    Label(window,text="Original Amount:",bg="orange",font=("Arial",25)).place(x=80,y=300)
    Label(window,text="Deposited amount:",bg="orange",font=("Arial",25)).place(x=80,y=400)
    Label(window,text="New amount:",bg="orange",font=("Arial",25)).place(x=80,y=500)
    original_amount = StringVar()
    original_amount= Entry(window,bg="grey",width=50,textvariable=original_amount)
    original_amount.place(x=380,y=300)
    deposited_amount = StringVar()
    deposited_amount =Entry(window,bg="grey",width=50,textvariable=deposited_amount)
    deposited_amount.place(x=380,y=400)
    item1= original_amount.get()
    item2= deposited_amount.get()
    item3= int(item1) + int(item2)
    new_amount =Entry(window,bg="grey",width=50,textvariable= new_amount)  
    new_amount.place(x=380,y=450)  
    new_amount.set(item3)
   
    window.mainloop()
