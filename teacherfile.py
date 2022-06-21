
from tkinter import *
from tkinter import messagebox


def win3():
    window3=Toplevel()
    window3.title('teacher file')
    window3.geometry('600x600')
    window3.configure(bg='#F0E68C')







    class teacher:
        def __init__(self, name, gender, TSC_no, salary, subjects):
            self.name= name
            self.pronoun=gender
            self.num= TSC_no
            self.cash= salary
            self.subjects= subjects
        # spec_gen=''
        # if spec_gen== 'male':
        #     gender= 'he'
        # else:
        #     gender = 'she'    


        def details(self):
            print ( f'{self.name} is a certified member of Kagumo highschool, TSC number: {self.num}.\n subjects teaching include {self.subjects}\n for this {self.pronoun} earns {self.cash}\n\n')



    lbl= Label(window3, text='ensure you have filled all fields'.upper(), bg='#F0E68C')
    lbl.place(x= 20, y=10)



#btn 1
    input1= StringVar()
    e_s= Entry(window3, width= 40, borderwidth=3, fg='grey', textvariable=input1)
    e_s.insert(0, 'enter your describing pronoun')
    e_s.place(x= 20, y= 70)
#btn 2
    input2= StringVar()
    e_s2= Entry(window3, width= 40, borderwidth=3, fg='grey', textvariable=input2)
    e_s2.insert(0, 'enter your name')
    e_s2.place(x= 20, y= 100)
#btn 3
    input3= StringVar()
    e_s3= Entry(window3, width= 40, borderwidth=3, fg='grey', textvariable=input3)
    e_s3.insert(0, 'enter your TSC number')
    e_s3.place(x= 20, y= 130)
#btn 4
    input4= StringVar()
    e_s4= Entry(window3, width= 40, borderwidth=3, fg='grey', textvariable=input4)
    e_s4.insert(0, 'enter subject cluster')
    e_s4.place(x= 20, y= 160)
#btn 5
    input5= StringVar()
    e_s5= Entry(window3, width= 40, borderwidth=3, fg='grey', textvariable=input5)
    e_s5.insert(0, 'enter salary')
    e_s5.place(x= 20, y= 190)


    btn1=Button(window3, text='submitt', width=50, font='forte', bg='green', fg='#000000')
    btn1.place(x=20, y=500)

    def click2():
        btn2.config(text= 'details have not been processed')
    btn2=Button(window3, text='clear', width=50, font='forte', bg='pink', fg='#FF0000')
    btn2.place(x=20, y=550)



    
    window3.mainloop  