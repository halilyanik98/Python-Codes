a=int(raw_input("1.Köþe Deðerini Giriniz"))
b=int(raw_input("2.Köþe Deðerini Giriniz"))
c=int(raw_input("3.Köþe Deðerini Giriniz"))
if a==b and b==c :
    print "Eþ kenar üçgen"
elif a==b and b!=c :
    print " Ýkiz Kenar Üçgen"
elif a==c and b!=c :
    print " Ýkizkenar üçgen"
else :
    print "Çeþitkenar Üçgen"
