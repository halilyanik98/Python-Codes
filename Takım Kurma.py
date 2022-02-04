##1.Bölüm --Arayüz için idle dýþý çalýþtýrma kodu
from Tkinter import *
import time
pencere = Tk()

bilgiler = ("Halil", "123123")
denemeHakki=3
zaman=0

##5.Bölüm-- Butonun görevi
def girisYap():
    ##6.Bölüm--Kalan Deneme Hakkýný Kodlama
    global denemeHakki, zaman
    if denemeHakki<=0:
        if time.time()-zaman>=5:
            denemeHakki=3
        else:
            sonuc.config(tet = u"Lutfen 5 Saniye Bekleyiniz...")
            return False
    ##5.Bölüm Devam
    kAdi = isim.get()
    parola = sifre.get()
    print kAdi, " - ", parola
    print "Kontrol ediliyor ..."
    if kAdi == bilgiler[0] and parola == bilgiler[1]:
        print "Bilgiler dogru!"
        sonuc.config(text = u"Oturum acma islemi basarili.")
    else:

        print "Bilgiler yanlis!"
        ##6.Bölüm Devam
        denemeHakki-=1
        if denemeHakki==0:
            zaman=time.time()
            
        sonuc.config(text = u"Bilgiler Yanlis. Kalan Deneme Hakki : %d" %denemeHakki)
##7.Bölüm Oyuncu Listesini gösterme
def kayitlar():
    pass
    
##2. Bölüm -- Arayüzü oluþturma kodu
pencere.title(u"Takim Kurma Programi")
pencere.geometry("290x200+100+100")
pencere.resizable(width=FALSE, height=FALSE)

karsilama = Label(pencere)
karsilama.config(text = u"Hosgeldiniz, lutfen giris yapiniz.")
karsilama.pack()

##3.Bölüm --Arayüzde giriþ bölümü
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

##4.Bölüm --Buton oluþturma (girisYap fonksiyonu yukarýda)
buton = Button(pencere)
buton.config(text = u"Giris Yap", command = girisYap)
buton.pack()
kapat = Button(text = "Cýkýs Yap",command=pencere.quit)
kapat.pack()
kayit = Button(text = "Kayitlari Goster", command=kayitlar)
kayit.pack()

sonuc = Label(pencere)
sonuc.config(text = u"Giris yapilmadi.")
sonuc.pack()

mainloop ()
