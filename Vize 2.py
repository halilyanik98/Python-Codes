###Vize 2. Soru##
T=True
while T:
    Deger= int(raw_input("100-500 Aras�nda De�er Giriniz : "))
    if Deger>500 or Deger<100 :
        print "Ko�ullara Uygun De�er Giriniz..."
    else :
        T=False
saat=8*60+30
Deger=Deger+saat
XX=Deger/60
YY=Deger%60


print "S�nav�n Ba�lang�� Saati 8.30 dur ",Deger,"saat sonra saat",XX,":",YY,"dir"


