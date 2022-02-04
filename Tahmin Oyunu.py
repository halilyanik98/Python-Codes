import random
deger=int(raw_input("Kaç Sayý Tahmin Etmek Ýstersiniz :"))
deger2=int(raw_input("Kaça Kadar Tahmin Etmek Ýstersiniz :"))
sistem=[]
kullanici=[]




i=0
for i in range(deger):
    sayi=random.randint(0,(deger2))
    sistem.append(sayi)




j=0
for j in range(deger):
    print j+1,". Deðeri Giriniz..0-" , deger2 , " Arasý Bir Sayý Tahmin Ediniz :"
    tahmin=int(raw_input("...."))
    kullanici.append(tahmin)
print "Sistemin Belirlediði Sayýlar" ,sistem
print "Sizin Tahmin Ettiðiniz Sayýlar" , kullanici



puan=0
n=0
m=0
x=0
c=0
for n in range(deger):
    for m in range(deger):
        if sistem[x]==kullanici[c]:
            puan=puan+(100/deger2)
print puan,"TL Kazandýnýz"



    
    
    
    
