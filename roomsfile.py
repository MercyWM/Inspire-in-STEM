
from tkinter import *



def win4():
    window4=Toplevel()
    window4.title('rooms file')
    window4.geometry('600x600')
    window4.configure(bg='#F0E68C')

    # class room:
    
    #      def __init__(self, capacity, wing, name):
    #          self.cap=capacity
    #          self.wing= wing
    #          self.name= name

    #      def details(self):
    #          print( f' The {self.cap} building, wing {self.wing} has a capacity of {self.cap}')
    
    
    
    lbl= Label(window4, text='ensure you have filled all fields'.upper(), bg='#F0E68C')
    lbl.place(x= 20, y=10)



#btn 1
    input1= StringVar()
    e_s= Entry(window4, width= 40, borderwidth=3, fg='grey', textvariable=input1)
    e_s.insert(0, 'enter room capacity')
    e_s.place(x= 20, y= 70)
#btn 2
    input2= StringVar()
    e_s2= Entry(window4, width= 40, borderwidth=3, fg='grey', textvariable=input2)
    e_s2.insert(0, 'enter enter room name')
    e_s2.place(x= 20, y= 100)
#btn 3
    input3= StringVar()
    e_s3= Entry(window4, width= 40, borderwidth=3, fg='grey', textvariable=input3)
    e_s3.insert(0, 'enter enter room wing')
    e_s3.place(x= 20, y= 130)
# #btn 4
#     input4= StringVar()
#     e_s4= Entry(window4, width= 40, borderwidth=3, fg='grey', textvariable=input4)
#     e_s4.insert(0, 'enter subject cluster')
#     e_s4.place(x= 20, y= 160)
# #btn 5
#     input5= StringVar()
#     e_s5= Entry(window4, width= 40, borderwidth=3, fg='grey', textvariable=input5)
#     e_s5.insert(0, 'enter salary')
#     e_s5.place(x= 20, y= 190)


    btn1=Button(window4, text='submitt', width=50, font='forte', bg='green', fg='#000000')
    btn1.place(x=20, y=500)

    def click2():
        btn2.config(text= 'details have not been processed')
    btn2=Button(window4, text='clear', width=50, font='forte', bg='pink', fg='#FF0000')
    btn2.place(x=20, y=550)



    
    
       
    
    window4.mainloop