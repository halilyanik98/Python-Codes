## En Yüksek Not Alan Öðrencinin Soyadý



sinif=[[123,'ahmet gel',10],[234,'mehmet git',75],[345,'bahri dur',67],[567,'burcu koþ',83],[678,'berna yaz',56],[789,'binan yak',78]]
def yukseknot(sinif):
    enyuksek=0
    for i in range (len(sinif)):
        if sinif[i][2]>enyuksek:
            enyuksek=sinif[i][2]
            yer=i
    ad=sinif[yer][1]
    soyad=ad.split(" ")
    x=soyad[-1]
    print x


yukseknot(sinif)

