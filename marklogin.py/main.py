from tkinter import *
from tkinter import font
import tkinter.messagebox
from turtle import title
from studentfile import *
from teacherfile import *
from roomsfile import *
from tkinter import font as tkFont
from Dwarning1 import *



# import os



window =Tk()
window.title("information center".capitalize())

window.configure(bg= '#D3D3D3')
Frame(window, height=500, width=750, bg='grey')

# j=0                                                                                                                                          
# r=0
# for i in range (100):
#     c=str(222222+r)
#     Frame(window, width=10, height=900, bg='#'+c).place(x=j, y=0)
#     j=j+10
#     r=r+1

#window.Title("school information desk")
# def main_screen():
#     screen=Tk
#     screen.geometry('1280x720+150+80')
#     screen.configure(bg='D3D3D3')
#     #trying to get a good icon
#     image_icon=PhotoImage(file='Wasserabweisend Homedeco Coral sea weed.jfif')
#     screen.iconphoto(False, image_icon)
#     screen.title('main window'.upper())
# main_screen()
window.geometry('750x900')

# class login:
#     def __init__(self, window):
#         self.window = window
#         self.bg= ImageTK.PhotoImage(file='images/1.jpg')
#         self.bg_image=Label(self.window, image= self.bg).place(x=0,y=0, relwidth=1, relheight=1)


Label(window, text= 'please enter your password :'.upper(), bg='#D3D3D3', border=0).place(x=150, y=40)
########################### password ####################3


#creating a pop up message for accepted password

#giving a function  to password button



def passC():
    
    if pass1.get()=='1234' and name_.get()=='mark':
        messagebox.showinfo('LOGIN SUCCESSFUL!','       WELCOME *-*    ')

    elif pass1.get()!='1234' and name_.get()=='mark':
        messagebox.showerror('notice'.upper(), 'YOU ENTERED THE WRONG PASSWORD\n \tPLEASE RETRY') 

    elif pass1.get()=='1234' and name_.get()!='mark':
        messagebox.showerror('NOTICE', 'THE USERNAME IS NOT LOGGED IN THE DATABASE\n \t\tSORRY')   
    else:
        messagebox.showerror('ACCESS DENIED', '   YOUR DETAILS DO NOT MATCH ANY OF OUR FILES  :(')
        
        
    
    
#lcd = tkFont.Font(family='lcdmono2', size=36, weight='bold')

buttonpass= Button(window, height=3, width=45, command=passC,text='SUBMIT?', font='elephant', bg='grey', borderwidth=7).place(x=150, y=120)



#adding a text place for password
global pass1
pass1=StringVar()
pass1=Entry(window, width=23, borderwidth=3, bg='#D3D3D3', textvariable=pass1)
pass1.insert(0,'PASSWORD')
pass1.place(x=150, y=60)





#adding directing message
Label(window, text='Please enter your name :'.upper(), bg='#D3D3D3').place(x=500, y=40)

# buttonpass= Button(window, height=5, width=20, text='Submit ! *-*').place(x=500, y=120)

name_=StringVar()
name_=Entry(window, width=24, borderwidth=3, bg='#D3D3D3')
name_.insert(0,'NAME')
name_.place(x=500, y=60)


label=Label(window, text='-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------', bg='#D3D3D3').place(x=1,y=220)

Label(window, text= 'student info:', bg='#D3D3D3').place(x=20, y=240) 
# s_name_box=Entry(window)
# e= Entry(window, width= 50, bg= '#D3D3D3',borderwidth= '5' )
# e.insert(0, 'Enter student name, pronoun, admission number, subject and average grade')
# e.place(x=150, y=20)
#btn 1
# input1= StringVar()
# e_s= Entry(window, width= 40, borderwidth=3, fg='grey', textvariable=input1)
# e_s.insert(0, 'enter your name')
# e_s.place(x= 20, y= 70)
# #btn 2
# input2= StringVar()
# e_s2= Entry(window, width= 40, borderwidth=3, fg='grey', textvariable=input2)
# e_s2.insert(0, 'enter your password')
# e_s2.place(x= 20, y= 100)
def myClick():
    if pass1.get()=='1234' and name_.get()=='mark':
        myLabel= Label (window, text= 'submiting', bg='#D3D3D3')
        myLabel.place(x=350, y=600)
        win2()
    else:
        messagebox.showerror('NOTICE', 'YOU ARE CURRENTLY NOT LOGGED IN')
    
    # myLabel= Label (window, text= 'submiting', bg='#D3D3D3')
    # myLabel.place(x=350, y=600)

mybutton=Button (window, text='Browse',width=70, command= myClick, bg='#D3D3D3', fg='#000000')
mybutton.place(x= 150, y=240)

f_name_box=Entry(window,width=20)

####################################################################################################################
#mybutton.grid(row=2, column=2)
Label(window, text='teachers information', bg='#D3D3D3').place(x= 20, y=310)

# e_1= Entry(window, width= 50, bg= '#D3D3D3',borderwidth= '5' )

# e_1.insert(0, 'enter teacher info')
# e_1.place(x= 150, y= 70)


emptyLabel= Label(window, text='')
#emptyLabel.grid(row=2, column= 2)


def myClick_1():
    if pass1.get()=='1234' and name_.get()=='mark':
       myLabel= Label (window, text= 'submiting', bg='#D3D3D3')
       myLabel.place(x=350, y=600) 
       win3()  

    else:
        messagebox.showerror('NOTICE','YOU ARE CURRENTLY NOT LOGGED IN!') 
    # myLabel= Label (window, text= 'submiting', bg='#D3D3D3')
    # myLabel.place(x=350, y=600)
mybutton=Button (window, text='Browse', width=70, command= myClick_1, bg='#D3D3D3', fg='#000000')
mybutton.place(x= 150, y=310)

f_name_box=Entry(window,width=20)
################################################################################################################3
Label(window, text='information on rooms', bg='#D3D3D3'). place(x=20, y= 380)
# e_2= Entry(window, width= 50, bg= '#D3D3D3',borderwidth= '5' )
# e_2.insert(0, 'enter room info')
# e_2.place(x= 150, y=130)

def myClick_2():
    if pass1.get()=='1234' and name_.get()=='mark':
        myLabel= Label (window, text= 'submiting', bg='#D3D3D3')
        myLabel.place(x=350, y=600)
        win4()
    else:
        messagebox.showerror('NOTICE', '   YOU ARE CURRENTLY NOT LOGGED IN!')


# myLabel= Label (window, text= 'submiting', bg='#D3D3D3')
# myLabel.place(x=350, y=600)

mybutton=Button (window, text='browse',width=70, command= myClick_2, bg='#D3D3D3', fg='#000000')
mybutton.place(x=150, y=380)
f_name_box=Entry(window,width=20)
####################################################################################################################################3


from tkinter import Label, Tk
import time


label_time=Label(window, text= ' time of login :'.upper(), font=('ariel', 15, tkFont.BOLD), bg='light grey')
label_time.place(x=0, y=1)


clock= Label(window, font=('lcdmono2', 20), fg='black', border=0, bg='light grey')
clock.place(x=200, y=1)

def digital_watch():
    current_time= time.strftime('%H: %M: %S')
    clock.config(text=current_time)
    clock.after(200, digital_watch)
digital_watch()




window.mainloop()