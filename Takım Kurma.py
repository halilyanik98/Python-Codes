##1.B�l�m --Aray�z i�in idle d��� �al��t�rma kodu
from Tkinter import *
import time
pencere = Tk()

bilgiler = ("Halil", "123123")
denemeHakki=3
zaman=0

##5.B�l�m-- Butonun g�revi
def girisYap():
    ##6.B�l�m--Kalan Deneme Hakk�n� Kodlama
    global denemeHakki, zaman
    if denemeHakki<=0:
        if time.time()-zaman>=5:
            denemeHakki=3
        else:
            sonuc.config(tet = u"Lutfen 5 Saniye Bekleyiniz...")
            return False
    ##5.B�l�m Devam
    kAdi = isim.get()
    parola = sifre.get()
    print kAdi, " - ", parola
    print "Kontrol ediliyor ..."
    if kAdi == bilgiler[0] and parola == bilgiler[1]:
        print "Bilgiler dogru!"
        sonuc.config(text = u"Oturum acma islemi basarili.")
    else:

        print "Bilgiler yanlis!"
        ##6.B�l�m Devam
        denemeHakki-=1
        if denemeHakki==0:
            zaman=time.time()
            
        sonuc.config(text = u"Bilgiler Yanlis. Kalan Deneme Hakki : %d" %denemeHakki)
##7.B�l�m Oyuncu Listesini g�sterme
def kayitlar():
    pass
    
##2. B�l�m -- Aray�z� olu�turma kodu
pencere.title(u"Takim Kurma Programi")
pencere.geometry("290x200+100+100")
pencere.resizable(width=FALSE, height=FALSE)

karsilama = Label(pencere)
karsilama.config(text = u"Hosgeldiniz, lutfen giris yapiniz.")
karsilama.pack()

##3.B�l�m --Aray�zde giri� b�l�m�
isimSor = Label(pencere)
isimSor.config(text = u"Kullanici Adi:")
isimSor.pack()

isim = Entry(pencere)
isim.pack()

sifreSor = Label(pencere)
sifreSor.config(text= u"Sifreniz:")
sifreSor.pack()

sifre = Entry(pencere)
sifre.pack()

##4.B�l�m --Buton olu�turma (girisYap fonksiyonu yukar�da)
buton = Button(pencere)
buton.config(text = u"Giris Yap", command = girisYap)
buton.pack()
kapat = Button(text = "C�k�s Yap",command=pencere.quit)
kapat.pack()
kayit = Button(text = "Kayitlari Goster", command=kayitlar)
kayit.pack()

sonuc = Label(pencere)
sonuc.config(text = u"Giris yapilmadi.")
sonuc.pack()

mainloop ()
