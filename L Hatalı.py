
def tablo(dizi) :
        toplam=0
        for j in range(dizi) :
                for i in range(dizi) :
                        if dizi [i] =="1" and dizi [i+1]=="1" and dizi[i+2] =="1" and dizi[i+3] =="1" :
                                if dizi[j]=="1" and dizi[j+1]=="1" and dizi[j+2]=="1" :
                                        toplam+=1
                i+=1
        j+=1
        print toplam
dizi=[["1","0","0","1","1","1","1"],["1","1","1","1","1","1","1"],["1","1","1","1","1","1","1"],["1","1","1","1","1","1","1"],["1","1","1","1","1","1","1"]]
print dizi
