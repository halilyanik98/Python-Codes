def pankreas (dizi) :
        yeni=" "
        i=0
        while i <len(dizi) :
                veri=dizi[i:i+2]
                if veri== "00" :
                        yeni=yeni+"A"
                elif veri =="11" :
                        yeni=yeni+"T"
                elif veri =="01":
                        yeni=yeni+"C"
                else:
                        yeni=yeni+"G"
                i+=2
                 
        print yeni

        
                yeni1=" "
                j=0
                while j<len(dizi1) :
                        veri1= dizi[j:j+4]
                        if veri1=="ATCG" :
                                print "Pankreas Kanseri Riski"
                        if veri1=="ATCC" :
                                print "İyi Huylu Pankreas Kanseri"
                        j+=4
        print yeni1
        yeni=dizi1



dizi="010010101101010010001010101101"
pankreas(dizi)
pankreas1(yeni)

