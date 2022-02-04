#-*-coding:utf8;-*-
#qpy:2
#qpy:console

class renk:
    pembe = '\033[95m'
    mavi = '\033[94m'
    yesil = '\033[92m'
    sari = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    beyaz='\x1b[m'
print renk.pembe,"Dipnot: Renk kodlarini gecemordan ogrendim saol abi"
print renk.FAIL,"========== QPYTHON.NET ========="
#Dipnot hatalar olabilir ilk defa boyle bir kod yaziyorum sizin kadar bilgili değilim 
print "\n\tINTERNET KULLANIMI HESAPLAMA"
print renk.yesil,"================================"
soru=input("Kaç Mb Internetiniz Var=")
soru2=input(" Kaç Gun kullanacaksin=")
print renk.yesil," Cevap = " ,  (soru / soru2 ) 
print renk.sari," GUNLUK BU KADAR KULLANMALISIN \nDIKKAT ET PAKETINI ASMA :) "
print renk.mavi,"GUNLUK BU KADAR KULLANMALISIN     \nDIKKAT ET PAKETINI ASMA :) "
print renk.FAIL,"GUNLUK BU KADAR KULLANMALISIN     \nDIKKAT ET PAKETINI ASMA :) "
print renk.yesil,"Gecemor Abi Renk Kodlari Icin Teşekkür Ederim :) "
