for d in range (1998):
    oyuncusayisi=int(raw_input(" Oyuncu Say�s� :")) #Toplam Oyuncu Say�s� Girilecek
    if oyuncusayisi%2==0 :#Oyuncu Say�s� �ift Olmad���nda Tekrardan De�er Alma
        break
    else:
        print " Hatali Giris Yaptiniz. Oyuncu Sayiniz Cift Olmalidir ...."
        
        



oyuncu=[]# Bo� Bir Oyuncu Listesi .
for a in range(oyuncusayisi):
    r=raw_input("Oyuncunun Ad�n� Girin : ")
    oyuncu.append(r) # Oyuncu Adl� Listeye Oyuncunun Ad� Eklenecek
    

takim1=[]
takim2=[]
import random # Randomu �ag�rma
for i in range((oyuncusayisi)/2):
    x=random.choice (oyuncu) # Oyuncu Listesinden Rastgele Bir Oyuncuyu Se�er (X)
    takim1.append(x)# Oyuncuyu 1. Tak�ma Ekler
    oyuncu.remove(x)# 1. Tak�ma Eklenen Oyuncuyu Art�k Siler
    
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

    
