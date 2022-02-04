100 elemanl�� bir liste 



#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
2-100 aras�ndaki asal say�lar� bulur
for-else yap�s� kullan�ld�
bayrak de�i�keni kullan�m�na gerek yok
"""

for x in range(2,100):
    for i in range(2,x-1):
        if x%i==0:
            break
    else:
        print x


#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 22:14:32 2018
Asal sayi �rne�i klasik ve for-else ile ��z�m�
@author: sntr
"""


"""
#Klasik y�ntem - Kontrol de�i�keni kullan�l�yor
x=25
asal=True    #Asal de�i�keni kontrol de�i�kenimiz
for i in range(2,x/2+1):
    if x%i==0:
        asal=False
        break
if asal:
    print x,"asal bir sayidir"
else:
    print x,"asal degildir"
"""

x=25
#Kontrol de�i�kenine gerek yok
for i in range(2,x/2+1):
    if x%i==0:
        print x,"asal sayi de�ildir"
        break

else:
    print x,"asal bir sayidir"




    #!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 15:26:41 2018
@author: sntr
"""

a=10
b=0

try:
    c=a/b
    print c
except ZeroDivisionError as e:
    print "hata"
finally:
    print "bittik"




    #!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 15:01:41 2018
Liste �retme �rnekleri
0-100 aras�nda say�lardan olu�an liste �retir
@author: sntr
"""


"""
#1.yol
x=[]
for i in range(100):
    x.append(i)
"""


#2.yol
x=range(100)



print x




#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 15:01:41 2018
Liste �retme �rnekleri
1,4,9,16,25 ... n^2 serisinden olu�an bir liste �retmek
@author: sntr
"""


"""
#1.yol
x=[]
for i in range(100):
    x.append(i**2)
"""


#2.yol
x=[i**2 for i in range(100)]



print x




#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 15:17:10 2018
@author: sntr
"""


str="Hayat K�sa Python O�renin"

x=[i for i in str if i.isupper()]
print x




#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 14:52:16 2018
@author: sntr
"""

"""
#Klasik y�ntem - Kontrol de�i�keni kullan�l�yor
x=23
i=1
asal=True
while i<(x/2)+1:
    i+=1
    if x%i==0:
        asal=False
        break
if asal:
    print x,"asal bir sayidir"
else:
    print x,"asal bir sayi degildir"
"""


x=17
i=1
while i<(x/2)+1:
    i+=1
    if x%i==0:
        print x,"asal bir sayi degildir"
        break

else:
    print x,"asal bir sayidir"
