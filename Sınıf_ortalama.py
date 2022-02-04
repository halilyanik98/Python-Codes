sinif=[[123,'ahmet gel',10],[234,'mehmet git',75],[345,'bahri dur',67],[567,'burcu koþ',83],[678,'berna yaz',56],[789,'binan yak',78]]

def ortalama(sinif) :
    toplam=0
    sayi=0
    for i in range (0,len(sinif)):
        toplam=toplam+sinif[i][2]
    ortalama=toplam/len(sinif)
    for i in range (0,len(sinif)):
        if sinif[i][2]>ortalama:
            sayi=sayi+1
    return sayi



print ortalama(sinif)
ortalama(sinif)
        
        
