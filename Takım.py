for d in range (1998):
    oyuncusayisi=int(raw_input(" Oyuncu Sayýsý :")) #Toplam Oyuncu Sayýsý Girilecek
    if oyuncusayisi%2==0 :#Oyuncu Sayýsý Çift Olmadýðýnda Tekrardan Deðer Alma
        break
    else:
        print " Hatali Giris Yaptiniz. Oyuncu Sayiniz Cift Olmalidir ...."
        
        



oyuncu=[]# Boþ Bir Oyuncu Listesi .
for a in range(oyuncusayisi):
    r=raw_input("Oyuncunun Adýný Girin : ")
    oyuncu.append(r) # Oyuncu Adlý Listeye Oyuncunun Adý Eklenecek
    

takim1=[]
takim2=[]
import random # Randomu Çagýrma
for i in range((oyuncusayisi)/2):
    x=random.choice (oyuncu) # Oyuncu Listesinden Rastgele Bir Oyuncuyu Seçer (X)
    takim1.append(x)# Oyuncuyu 1. Takýma Ekler
    oyuncu.remove(x)# 1. Takýma Eklenen Oyuncuyu Artýk Siler
    
for j in range((oyuncusayisi)/2):
    x=random.choice (oyuncu)
    takim2.append(x)
    oyuncu.remove(x)

for k in range(1):
    n=random.choice(takim1)
    m=random.choice(takim2)
    


    
    
print ("1. Takimda Oynayacak Oyuncular :",takim1,"Bu Takimin Kalecisi",n )
print ("2. Takimda Oynayacak Oyuncular :",takim2,"Bu Takimin Kalecisi",m )

##oyuncular=["Halil","Veysel","Yusa","Osman","Osman Ali","Dogukan","Burak","Berkay","Muhammet","Ercu"]

    
