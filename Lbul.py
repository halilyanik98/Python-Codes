dizi=[[0,0,0,0,1,0,0],[0,0,0,1,0,1,0,0],[0,0,0,1,0,1,0,0],[1,0,0,1,0,1,1,1],[1,0,0,0,1,1,1,0,0],[1,0,0,0,0,0,0,0],[1,1,1,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
def Lbul (dizi) :
    i=0
    j=0
    for i in range (len(dizi)) :
        for j in range (len(dizi)) :
            print dizi[i][j]
        print
    sayac=0
    for j in range(0,len(dizi)-2):
        for i in range(0,len(dizi)-3) :
            if dizi[i][j]==1 :
                if dizi[i+3][j+2]==1 :
                    if dizi[i+3][j+1]==1 :
                       if dizi[i+3][j]==1 :
                           if dizi[i+2][j]==1 :
                               if dizi[i+1][j]==1 :
                                   sayac=sayac+1
    print sayac
Lbul(dizi)
