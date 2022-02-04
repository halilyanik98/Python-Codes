import random
user=int(raw_input("Kaç Kullanýcý Var ? "))
rg=["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l","M","m","N","n","O","o","P","p","R","r","S","s","T","t","U","u","V","v","Y","y","Z","W","w","Q","q","X","x"]
tg=["1","2","3","4","5","6","7","8","9","0"]
yg=["!","+","%","&","=","-"]
y=""
liste=[]
i=0
j=0
for i in range((user)):
    x=raw_input("Kullanici Adinizi Giriniz :")
    for j in range(5):
        a=str(random.choice(rg))
        b=str(random.choice(tg))
        c=str(random.choice(yg))
        y=y+(a)+(b)+(c)
    kullanici= x , y
    print x,"Kullanýcý Adýnýza Ait Þifreniz :",y,"dir"
    print x,"Kullanýcýsý Listeye Eklenmiþtir"
    
    liste.append(kullanici)
    y=""
print liste







