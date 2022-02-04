#!/usr/bin/env python
#-*-coding:utf-8-*-

from Tkinter import *
import os

dosya ="~/mp3/1.mp3"

pencere = Tk()
pencere.geometry("200x150+150+150")
pencere.resizable(width=FALSE, height=FALSE)
baslik = pencere.title("TkMp3")


def player():
	os.system("mpg123 -q "+dosya+" &")

def durdur():
	os.system("killall mpg123")
	
dosyayaz=Label(text=dosya)
dosyayaz.pack()
dugme3 = Button(text = "KAPAT",command=pencere.quit)
dugme2 = Button(text = "DUR", command=durdur)
dugme = Button(text = "ÇAL", command=player)
dugme.pack()
dugme2.pack()
dugme3.pack()

mainloop()
