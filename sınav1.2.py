def sirala(listegel):
    bitti=False
    devam=1
    while bitti!=True:
        devam=1
        for i in range(0,len(listegel)-1):
            if listegel[i]>listegel[i+1]:
                yeni=listegel[i+1]
                listegel[i+1]=listegel[i]
                listegel[i]=yeni
                devam=0
            if devam!=0:
                bitti=True
    print listegel
sirala(random.sample(sayilar, 10))
