def kanser(kromozom):
    deger =""
    i=0
    while i<len(kromozom):
        veri=kromozom[i:i+2]
        if veri =="00" :
            deger=deger+"A"
        elif veri =="11" :
            deger=deger+"T"
        elif veri =="01" :
            deger= deger+"C"
        else :
            deger= deger+"G"
        i=i+2
    print deger
    

    j=0
    while j<len(deger):
        yeniveri=deger[j:j+4]
        if yeniveri=="ATCG" :
            print "Pankreas Kanseri Habercisi"
            break
            

        elif yeniveri=="ATCC":
            print "Ýyi Huylu Pankreas Kanseri"
            break

        else:
            print "Kanser Riski Yoktur"
            break

        j+=1
kromozom="00001010110100101010001101101011010101001010111000"

kanser(kromozom)

