from tkinter import *

def window2():
    window = Tk()
    window.title("Welcome USER 2")
    window.config(bg="white")
    window.geometry("400x400")
    Label(window, text="Name:Jonathan Ageyo\nAge:19\nHobby:Skydiving\nBirthday:1st June",font=("Calibri Bold",20)).place(x=200,y=200)
    window.mainloop()