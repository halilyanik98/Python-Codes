#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from Tkinter import *

defanskadro=[]
ortasahakadro=[]
forvetkadro=[]

pencere = Tk()

def oyuncu ():
    
    Label(pencere, text="Oyuncunun Adı :").grid(row=0)
    Label(pencere, text="Oyuncunun Soyadı :").grid(row=1)
    Label(pencere, text="Oyuncunun Mevkisi :").grid(row=2)



    e1 = Entry(pencere)
    e2 = Entry(pencere)
    e3 = Entry(pencere)


    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)


Label(pencere, text="Toplam Oyumcu Sayısı :").grid(row=0)
e1 = Entry(pencere)
e1.grid(row=0, column=1)



mainloop( )
