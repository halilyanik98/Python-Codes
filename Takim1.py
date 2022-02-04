

from Tkinter import *
pencere=Tk()
takim=[]
pencere.title(u"Takim Kurma Programi")
pencere.geometry("290x200+100+100")
pencere.resizable(width=TRUE, height=TRUE)
defanskadro=[]
ortasahakadro=[]
forvetkadro=[]

               
##Yeni Komut Dosya Yolu hatalý mý ?


def hayir ():
    secenek1.destroy()
    secenek2.destroy()
    secenek.destroy()
    sayi.destroy()
    sayi1.destroy()
    for i in range(sayi):
        pass
### Oyuncu Sayýsý Kadar pencere Ekleme Komutu ?
    
def evet ():
    secenek1.destroy()
    secenek2.destroy()
    secenek.destroy()
    sayi.destroy()
    sayi1.destroy()
    def kayit():
        pass
        
    defans=Label(pencere)
    defans.config(text=u"Defans Kisi Sayisini Giriniz")
    defans.pack()

    defans=Entry(pencere)
    defans.pack()
    aadefans=defans.get()

    ortasaha=Label(pencere)
    ortasaha.config(text=u"Orta Saha Kisi Sayisini Giriniz")
    ortasaha.pack()

    ortasaha=Entry(pencere)
    ortasaha.pack()
    aaortasaha=ortasaha.get()

    forvet=Label(pencere)
    forvet.config(text=u"Forvet Kisi Sayisini Giriniz")
    forvet.pack()

    forvet=Entry(pencere)
    forvet.pack()
    aaforvet=forvet.get()

     
    
    dugme2=Button(text="Devam",command=kayit)
    dugme2.pack()


    
    ## GÝRÝLEN OYUNCUNUN ADINI LÝSTEYE EKLEMEYE ÇALIÞIYORUM
    ##AMA HER SEFERÝNDE LÝSTEDE BOÞ ÝSÝMLER OLUYOR SORUN NEY 
    
    
    


sayi = Label(pencere)
sayi.config(text = u"Toplam Oyuncu Sayisini Giriniz :")
sayi.pack()

sayi1=Entry(pencere)
sayi1.pack()
aasayi1=sayi1.get()



secenek=Label(pencere)
secenek.config(text= u"Mevkiyi Sistem Belirlesin")
secenek.pack()

secenek1=Button(text="Evet",command=evet)
secenek1.pack(),
secenek2=Button(text="Hayir",command=hayir)
secenek2.pack()

secenek=Label(pencere)
secenek.config(text= u"Hack Yiyen Hak Yer")
secenek.pack()




mainloop()
print aasayi1
print takim
