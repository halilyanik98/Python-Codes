import random
deger=int(raw_input("Ka� Say� Tahmin Etmek �stersiniz :"))
deger2=int(raw_input("Ka�a Kadar Tahmin Etmek �stersiniz :"))
sistem=[]
kullanici=[]




i=0
for i in range(deger):
    sayi=random.randint(0,(deger2))
    sistem.append(sayi)




j=0
for j in range(deger):
    print j+1,". De�eri Giriniz..0-" , deger2 , " Aras� Bir Say� Tahmin Ediniz :"
    tahmin=int(raw_input("...."))
    kullanici.append(tahmin)
print "Sistemin Belirledi�i Say�lar" ,sistem
print "Sizin Tahmin Etti�iniz Say�lar" , kullanici



puan=0
n=0
m=0
x=0
c=0
for n in range(deger):
    for m in range(deger):
        if sistem[x]==kullanici[c]:
            puan=puan+(100/deger2)
print puan,"TL Kazand�n�z"



    
    
    
    
