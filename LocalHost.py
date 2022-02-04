#!/usr/bin/env python3
import os
from Tkinter import *

pencere = Tk()

def kur():
    os.system("sudo apt-get install apache2, mysql-server, php5, php5-mysql, phpmyadmin")
   

a = pencere.title("Kubuntu/Ubuntu Localhost Yükleyici")
uyari = Label(pencere,text="Kurulum Baþlasýn mý ?")
uyari.pack()


dugme1 = Button(text = "Kapat", command = pencere.quit)
dugme1.pack(side = LEFT)

dugme2 = Button(text = "Kur", command = kur)
dugme2.pack(side = RIGHT)

mainloop()

