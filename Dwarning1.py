

import tkinter.font as font
from email import message
from tkinter import *


def warn1():
    warn=Toplevel()
    warn.title('          notice!!!'.upper())
    warn.geometry('300x130')
    warn.configure(bg='#F0E68C')


    exFont= font.Font(family = 'helvetica', size= 50)
    Label(warn, text='{ ! }', font=exFont, bg= '#F0E68C', fg='maroon').pack()


    exFont2=font.Font(family= 'ariel', size= 10)
    Label(warn, text='you entered a wrong pasword !!!'.upper(), font=exFont2, bg='#F0E68C', fg='red').pack()