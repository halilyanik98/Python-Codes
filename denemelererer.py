##1.B�l�m --Aray�z i�in idle d��� �al��t�rma kodu
from Tkinter import *
import time
pencere = Tk()

liste=[]
denemeHakki=3
zaman=0

##5.B�l�m-- Butonun g�revi
def girisYap():
    liste.append(isimSor)
        
##7.B�l�m Oyuncu Listesini g�sterme
def kayitlar():
    pass
    
##2. B�l�m -- Aray�z� olu�turma kodu
pencere.title(u"Takim Kurma Programi")
pencere.geometry("390x200+400+400")
pencere.resizable(width=TRUE, height=TRUE)



##3.B�l�m --Aray�zde giri� b�l�m�
sayi = Label(pencere)
sayi.config(text = u"Toplam Oyuncu Sayisini Giriniz :")
sayi.pack()

sayi1 = Entry(pencere)
sayi1.pack()

isimSor = Label(pencere)
isimSor.config(text = u"Oyuncunun Adini Giriniz:")
isimSor.pack()

isim = Entry(pencere)
isim.pack()

sifreSor = Label(pencere)
sifreSor.config(text= u"Oyuncu Numarasi:")
sifreSor.pack()

sifre = Entry(pencere)
sifre.pack()

##4.B�l�m --Buton olu�turma (girisYap fonksiyonu yukar�da)
buton = Button(pencere)
buton.config(text = u"Kaydet", command = girisYap)
buton.pack()

bilgi = Label(pencere)
bilgi.config(text = u"Oyuncularin Tamamini Kaydettikten Sonra Takim Olusacaktir")
bilgi.pack()

dugme = Button(text = "Kayitlari Goster", command=kayitlar)
dugme.pack()


mainloop ()
print liste
