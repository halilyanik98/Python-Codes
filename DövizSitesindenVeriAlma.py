import requests
from bs4 import BeautifulSoup

c = """

Kullanabilmek için komutlar:

Kanada : CAD

EURO   : EUR

DOLAR  :USD

ÝNGÝLÝZ STERLÝNÝ    :GBP

ÝSVÝÇRE: CHF
gibi komutlar vererek kullanabilirsiniz.

"""
print(c)
#--------------------------
bos = []
istek = input("Döviz :")
istek = istek.upper()
#--------------------------
url = "http://www.doviz.com/"
veri = requests.get(url)
soup = BeautifulSoup(veri.content,"html.parser")
#print(soup)
gelen_veri = soup.find_all("div",{"class":"grid4 doviz-column2 btgreen"})
gelen_veri = soup.find_all("ul")
gelen_veri = soup.find_all("li",{"data-table-homepage-key":istek})
#print(gelen_veri)
for i in gelen_veri:
   bos+=i
   print("-------------------")
   for alis_fiyati in bos[5]:
       print("alýþ fiyatý  :{}".format(alis_fiyati))
   for satis_fiyati in bos[7]:
       print("satýþ fiyatý :{}".format(satis_fiyati))
       print("-------------------")
