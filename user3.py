from tkinter import *

def window3():
    window = Tk()
    window.title("Welcome USER 3")
    window.config(bg="yellow")
    window.geometry("400x400")
    Label(window, text="Name:Lilian Cheruyiot\nAge:20\nHobby:Cooking\nBirthday:1st August",font=("Calibri Bold",20)).place(x=200,y=200)
    window.mainloop()

