def soru (dizi):
    i=0
    yeni=[]
    for i in dizi :
        while dizi[i]<dizi[i-1] :
            yeni.append (dizi[i+1])
        while dizi[i]>dizi[i-1]:
            yeni.append ( dizi[i])
            
    print yeni
dizi =[15,21,15,45]
soru(dizi)
