
##!usr/bin/python

##########################
#      ANALOG CLOCK
#      Name: Mercy Muiruri
#      
###########################

#list of imported modules
from tkinter import *
from math import cos, sin
from time import gmtime, sleep

#defining of secondary functions

def drawcircle(Alpha,Beta,Rayon,Couleur,can): #draw a circle base on center coord radius and color
    x1,y1,x2,y2=Alpha-Rayon, Beta-Rayon, Alpha+Rayon, Beta+Rayon
    can.create_oval(x1,y1,x2,y2,fill=Couleur)

def drawPetAig(CoordA, CoordZ, Taille, Omega, can): #function to drawn the second hand of the clock
    Pi = 3.141592
    Omega = ((Omega/60)+1)*30
    can.create_line(CoordA + (Taille/3) * cos(Pi*(Omega/180)), CoordZ + (Taille/3) * sin(Pi*(Omega/180)), CoordA - (Taille/8) * cos(Pi*(Omega/180)), CoordZ - (Taille/8) * sin(Pi*(Omega/180)) )

def drawGrdAig(CoordA, CoordZ, Taille, Omega, can): #function to draw the minute hand, based on center coord and minutes.
    Pi = 3.141592
    Omega = (Omega-15)*6
    can.create_line(CoordA + (Taille/1.5) * cos(Pi*(Omega/180)), CoordZ + (Taille/1.5) * sin(Pi*(Omega/180)), CoordA - (Taille/6) * cos(Pi*(Omega/180)), CoordZ - (Taille/6) * sin(Pi*(Omega/180)))

def drawSecAig(CoordA, CoordZ, Taille, Omega, can): #function to draw the hour hand
    Pi = 3.141592
    Omega = (Omega-15) *6
    can.create_line(CoordA + (Taille/1.5) * cos(Pi*(Omega/180)), CoordZ + (Taille/1.5) * sin(Pi*(Omega/180)), CoordA - (Taille/6) * cos(Pi*(Omega/180)), CoordZ - (Taille/6) * sin(Pi*(Omega/180)), fill = "red")

def fondhorloge(CoordA, CoordZ, Taille, can1):  #function drawing the backgroud of the clock
    Pi = 3.141592
    drawcircle(CoordA, CoordZ, Taille + (Taille/10), "grey6",can1) #drawing the surrounding of the clock
    drawcircle(CoordA, CoordZ, Taille, "ivory3",can1)#backgroud
    drawcircle(CoordA, CoordZ, Taille/80, "grey6",can1)#central point/needle articulation
    can1.create_line(CoordA + (Taille - (Taille/15)), CoordZ, CoordA + (Taille - (Taille/5)), CoordZ) #drawing the N/S/E/W decorativ hour position
    can1.create_line(CoordA, CoordZ + (Taille - (Taille/15)), CoordA, CoordZ + (Taille - (Taille/5)))
    can1.create_line(CoordA - (Taille - (Taille/15)), CoordZ, CoordA - (Taille - (Taille/5)), CoordZ)
    can1.create_line(CoordA, CoordZ - (Taille - (Taille/15)), CoordA, CoordZ - (Taille - (Taille/5)))

    #here, this 4*2 line defined the position of the 8 intermediate line between the N/S/E/W decorativ line.
    can1.create_line(CoordA + (Taille/1.05) * cos(Pi*(30/180)), CoordZ + (Taille/1.05) * sin(Pi*(30/180)), CoordA + (Taille/1.20) * cos(Pi*(30/180)), CoordZ + (Taille/1.20) * sin(Pi*(30/180)))
    can1.create_line(CoordA + (Taille/1.05) * cos(Pi*(60/180)), CoordZ + (Taille/1.05) * sin(Pi*(60/180)), CoordA + (Taille/1.20) * cos(Pi*(60/180)), CoordZ + (Taille/1.20) * sin(Pi*(60/180)))

    can1.create_line(CoordA - (Taille/1.05) * cos(Pi*(30/180)), CoordZ - (Taille/1.05) * sin(Pi*(30/180)), CoordA - (Taille/1.20) * cos(Pi*(30/180)), CoordZ - (Taille/1.20) * sin(Pi*(30/180)))
    can1.create_line(CoordA - (Taille/1.05) * cos(Pi*(60/180)), CoordZ - (Taille/1.05) * sin(Pi*(60/180)), CoordA - (Taille/1.20) * cos(Pi*(60/180)), CoordZ - (Taille/1.20) * sin(Pi*(60/180)))

    can1.create_line(CoordA + (Taille/1.05) * cos(Pi*(30/180)), CoordZ - (Taille/1.05) * sin(Pi*(30/180)), CoordA + (Taille/1.20) * cos(Pi*(30/180)), CoordZ - (Taille/1.20) * sin(Pi*(30/180)))
    can1.create_line(CoordA + (Taille/1.05) * cos(Pi*(60/180)), CoordZ - (Taille/1.05) * sin(Pi*(60/180)), CoordA + (Taille/1.20) * cos(Pi*(60/180)), CoordZ - (Taille/1.20) * sin(Pi*(60/180)))

    can1.create_line(CoordA - (Taille/1.05) * cos(Pi*(30/180)), CoordZ + (Taille/1.05) * sin(Pi*(30/180)), CoordA - (Taille/1.20) * cos(Pi*(30/180)), CoordZ + (Taille/1.20) * sin(Pi*(30/180)))
    can1.create_line(CoordA - (Taille/1.05) * cos(Pi*(60/180)), CoordZ + (Taille/1.05) * sin(Pi*(60/180)), CoordA - (Taille/1.20) * cos(Pi*(60/180)), CoordZ + (Taille/1.20) * sin(Pi*(60/180)))

#PRINCIPLE FUNCTION (here the problem starts)

def HORLOGE1(Gamma, Pi, Epsylon):# draw a clock with the center position x/x = gamma/pi and the radius = epsylon

    fondhorloge(Gamma, Pi, Epsylon, can1)# extracting time value
    patate = gmtime()
    heure = patate[3] + 1  # "+1" is changing time from english time to french time :P
    minute = patate[4]
    seconde = patate[5]

    print(heure, minute, seconde) # a simple test to watch what the programm is doing (run it, and you'll see, that this test is done tausend time per second, that why I think the problem is here.)
    drawPetAig(Gamma, Pi, Epsylon, minute, can1)
    drawGrdAig(Gamma, Pi, Epsylon, minute, can1)
    drawSecAig(Gamma, Pi, Epsylon, seconde, can1)
    fen1.after(1000, lambda: HORLOGE1(250, 250, 200))

#execution of the main function

fen1 = Tk()
can1 = Canvas(fen1, bg="white", height=500, width=500)
can1.pack()

HORLOGE1(250, 250, 200)

fen1.mainloop()
fen1.destroy()