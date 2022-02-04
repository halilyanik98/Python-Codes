



sinif=[[123,'ahmet gel',10],[234,'mehmet git',75],[345,'bahri dur',67],[567,'burcu koþ',83],[678,'berna yaz',56],[789,'binan yak',78]]
def numara(sinif):
    sonnot=101
    for i in range (len(sinif)):
        veri=sinif[i][1]
        if veri[0:1]=="b" :
            if sonnot>sinif[i][2] :
                sonnot=sinif[i][2]
                yer=i
    x=sinif[yer][0]
    return x
print numara(sinif)
