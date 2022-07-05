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
 # this ads labels to the interface and you have to specify the font you want and the size of the text
s_name = Label(window, text="SECOND NAME",font=("Calibri Bold",20))
f_name = Label(window, text="FIRST NAME",font=("Calibri Bold",20))

f_name.grid(column = 60,row = 100)    # this specifys wont=("Calibri Bold",20)here exactly on the window it will print out
s_name.grid(column = 60,row = 120)



def open_poppup():
    top = Toplevel(window)
    top.geometry("300x300")
    top.title(" POPPUP WINDOW")
    top.configure(bg="white")
    Label(top,text ="Welcome user!\n Have a great Day",font = ("Arial",20)).place(x= 75,y=100) # when you want to show the place on the grid, 
#if you want to use the words column anmd row,use grid, if not, just say x(column) and y(grid)
    Button(top,text = "Inspirational",bg = "red").place(x=100,y=200)
    Button(top,text = "Comical",bg= "green").place(x=250,y=200)


f_name_box = Entry(window,width=20,bg="green")
f_name_box.grid(column = 100,row = 100)
s_name_box = Entry(window,width=20,bg="green")
s_name_box.grid(column = 100,row = 120)

btn = Button(window,text = "Click here to start",bg="red",fg="green",command = open_poppup)# this creates a button to click and specifys the background colour and foreground colour
btn.grid(column = 120,row = 150)   #this just specifys on the grid where the button is to be






window.mainloop()                # i think this is the closing part
