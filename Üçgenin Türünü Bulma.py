a=int(raw_input("1.K��e De�erini Giriniz"))
b=int(raw_input("2.K��e De�erini Giriniz"))
c=int(raw_input("3.K��e De�erini Giriniz"))
if a==b and b==c :
    print "E� kenar ��gen"
elif a==b and b!=c :
    print " �kiz Kenar ��gen"
elif a==c and b!=c :
    print " �kizkenar ��gen"
else :
    print "�e�itkenar ��gen"
