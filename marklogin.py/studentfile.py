
from tkinter import *
from tkinter import messagebox


def win2():
    window2=Toplevel()
    window2.title('student file')
    window2.geometry('600x600')
    window2.configure(bg='#F0E68C')




    class student:
        def __init__(self, name, pronoun, ADM_no, subject, av_grade):
            self.pronoun= pronoun
            self.name= name
            self.grade= av_grade
            self.ADM_no= ADM_no
            self.subject= subject
            

        def details(self):
            print( f'{self.pronoun}, {self.name}, admission number{self.ADM_no} has scored an average of {self.grade} in the following subjects {self.subject}')

    student_1= student('Mr','Mark', '10105', 'A-', 'Essentials\n All sciences\n Geogrphy\n Art') 
    student_1.details()
    
    lbl= Label(window2, text='ensure you have filled all fields'.upper(), bg='#F0E68C')
    lbl.place(x= 20, y=10)


#btn 1
    input1= StringVar()
    e_s= Entry(window2, width= 40, borderwidth=3, fg='grey', textvariable=input1)
    e_s.insert(0, 'enter your describing pronoun')
    e_s.place(x= 20, y  = 70)
#btn 2
    input2= StringVar()
    e_s2= Entry(window2, width= 40, borderwidth=3, fg='grey', textvariable=input2)
    e_s2.insert(0, 'enter your name')
    e_s2.place(x= 20, y= 100)
#btn 3
    input3= StringVar()
    e_s3= Entry(window2, width= 40, borderwidth=3, fg='grey', textvariable=input3)
    e_s3.insert(0, 'admission number')
    e_s3.place(x= 20, y= 130)
#btn 4
    input4= StringVar()
    e_s4= Entry(window2, width= 40, borderwidth=3, fg='grey', textvariable=input4)
    e_s4.insert(0, 'average grade')
    e_s4.place(x= 20, y= 160)
#btn 5
    input5= StringVar()
    e_s5= Entry(window2, width= 40, borderwidth=3, fg='grey', textvariable=input5)
    e_s5.insert(0, 'enter taken subject cluster')
    e_s5.place(x= 20, y= 190)
    def click1():
        messagebox.showinfo(text=input1+ input2+' admission number '+input3+' has scored an average of'+ input4+ 'in the following subject cluster'+ input5)

    # btn1=Label(window2, text='busted', fg='black', font=('Arial', 2))
    # btn1.place(x=10, y=550)
   

    sign=Button(window2, text='submitt', width=50, font='forte', bg='green', fg='#000000', command=click1)
    sign.place(x=20, y=450)

    def click2():
        btn2.config(text= 'details have not been processed')
    btn2=Button(window2, text='clear', width=50, font='forte', bg='pink', fg='#FF0000')
    btn2.place(x=20, y=500)



    
    window2.mainloop 