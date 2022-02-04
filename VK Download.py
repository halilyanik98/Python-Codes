#-*-coding:utf8;-*-
#qpy:2
#qpy:console

import re, base64
import urllib2
    

gir=d.getClipboard().result

print "\033[94mAçılıyor Bekleyin.. \x1b[m "
a="QnUgS29kIHFweXRob24ubmV0IEFkcmVzaW5lIEFpdHRpci4="
def oku():
    try: 
        bul='\?oid=.*?hd=\d'
        vk=urllib2.urlopen(gir).read()
        lnk=re.findall(bul,vk)[0]
        print lnk
        vk='http://vk.com/video_ext.php'+lnk
        v=vk.replace('#038;','')
        print v
        cs=urllib2.urlopen(v).read()
        if '.240.mp4' in cs:
            print '1- 240p'
        if '.360.mp4' in cs:
            print '2- 360p'
        if '.480.mp4' in cs:
            print '3- 480p'
        if '.720.mp4' in cs:
            print '4- 720p'
        if '.1080.mp4' in cs:
            print '5- 1080p'
        kalite=raw_input('kalite?: ')
        ara= 'url\d+=(.+?)&'
        global link
        link=re.findall(ara,cs)[int(kalite)-1]
        print link
        d.setClipboard(link)
        d.makeToast("indirme linki panoya kopyalandi")
    except:
        ara1="http://cs.*?\.vk\.me/.*?/.*?/.*?\.(\d+)\.mp4?.*? "
        vk=urllib2.urlopen(gir).read()
        lnk=re.findall(ara1,vk)
        say=0  
        p=[]  
        for i in lnk:
            say+=1   
            p.append(i)
            print say,'-',i

        ara="http://cs(.+?) "
        vk=urllib2.urlopen(gir).read()
        lnk=re.findall(ara,vk)
        v="http://cs"+lnk[0]
        link1=v.replace('"','')
        kalite=raw_input('kalite?: ')
        link=link1.replace('.240.','.'+p[int(kalite)-1]+'.')
        print link
        d.setClipboard(link)
        d.makeToast("indirme linki panoya kopyalandi")
print base64.decodestring(a)
oku() 
