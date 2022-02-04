##1.Bölüm --Arayüz için idle dýþý çalýþtýrma kodu
from Tkinter import *
import time
pencere = Tk()

liste=[]
denemeHakki=3
zaman=0

##5.Bölüm-- Butonun görevi
def girisYap():
    liste.append(isimSor)
        
##7.Bölüm Oyuncu Listesini gösterme
def kayitlar():
    pass
    
##2. Bölüm -- Arayüzü oluþturma kodu
pencere.title(u"Takim Kurma Programi")
pencere.geometry("390x200+400+400")
pencere.resizable(width=TRUE, height=TRUE)



##3.Bölüm --Arayüzde giriþ bölümü
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

##4.Bölüm --Buton oluþturma (girisYap fonksiyonu yukarýda)
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
