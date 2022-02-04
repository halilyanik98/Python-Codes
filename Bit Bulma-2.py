def soru (dizi) :
        yenidizi= [ ]
        yenidizi.append(dizi[0])
        j=1
        while j<len(dizi) :
                yenidizi.append ( dizi[ j ] -dizi [ j - 1 ] )
                j+=1
        print yenidizi
dizi=[15,16,15,14,16,15,15,14]
soru(dizi)

