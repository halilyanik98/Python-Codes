
dizi=[25,36,15,28,65,45,52,88]
def siralama(dizi):
    for i in range(len(dizi)):
        if dizi[0]<dizi[1]:
            x=dizi[i]
            dizi[i]=dizi[i+1]
            dizi[i+1]=x
            print dizi
        
            
        
siralama(dizi)
