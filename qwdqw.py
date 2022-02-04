deger=[12,65,28,96,-85,-94,-25,0]
toplam1=0
toplam2=0
toplam3=0
i=0
for i in range (len(deger)):
    if deger>0 :
        toplam1=toplam1+1
    elif deger==0 :
        toplam2=toplam2+1
    else :
        toplam3=toplam3+1
print toplam1 , toplam2 ,toplam3
