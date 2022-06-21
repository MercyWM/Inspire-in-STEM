from tkinter import *

def window1():
    window = Tk()
    window.title("Welcome USER 1")
    window.config(bg="purple")
    window.geometry("400x400")
    Label(window, text="Name:Mercy Muiruri\nAge:17\nHobby:Travelling\nBirthday:1st July",font=("Calibri Bold",20)).place(x=200,y=200)
    window.mainloop()
