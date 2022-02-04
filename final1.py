dizi=[[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,1,1,1]]
yenidizi=[]
def soru1 (dizi) :
    for i in range (len(dizi)):
        for j in range(len(dizi)):
            if dizi[j+1]==1 :
                yenidizi.append(dizi[j][i])
            else :
                i+=1
                j=j-1
                
soru1(dizi)
