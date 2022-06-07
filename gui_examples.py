#!usr/bin/python


##########################
#      GUI_EXAMPLES USING TKINTER
#      Name: Mercy Muiruri
#      Date: 7/6/2022
###########################

# a user interface is a window
# it has labels,buttons,hidden menu,images,the textbox etc.

from tkinter import * # this imports everything from the tkinter to create a user interface

window  = Tk()        # this creates an empty window
window.title("Welcome to my app!") # this adds the title
window.configure(bg= "yellow")      # this creates a background colour to the user interface
window.geometry("400x400")        # this specifies the size of the user interface

f_name = Label(window, text="FIRST NAME",font=("Calibri Bold",20)) # this ads labels to the interface and you have to specify the font you want and the size of the text
s_name = Label(window, text="SECOND NAME",font=("Calibri Bold",20))

f_name.grid(column = 60,row = 100)    # this specifys where exactly on the window it will print out
s_name.grid(column = 60,row = 120)

def open_poppup():
    top = Toplevel(window)
    top.geometry("300x300")
    top.title(" POPPUP WINDOW")
    top.configure(bg="purple")
    msg = Label(top,text ="Welcome user!",font = ("Arial",18))

btn = Button(window,text = "Click here to start",bg="red",fg="green",command = open_poppup()) # this creates a button to click and specifys the background colour and foreground colour
btn.grid(column = 120,row = 150)    #this just specifys on the grid where the button is to be

f_name_box = Entry(window,width=20,bg="green")
f_name_box.grid(column = 100,row = 100)
s_name_box = Entry(window,width=20,bg="green")
s_name_box.grid(column = 100,row = 120)




window.mainloop()                # i think this is the closing part
