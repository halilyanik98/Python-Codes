def  soru1(dizi) :
        i=0
        toplam=0
        for i in dizi :
                bit=1
                while i>1 :
                        i=i/2
                        bit+=1
                toplam+=bit
        print toplam

dizi=[4,4,4,4,4,4]
soru1(dizi)

