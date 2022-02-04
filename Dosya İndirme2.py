#-*-coding:utf8-*-
#qpy:2
#qpy:console

import platform, time, os, sys, subprocess, re, urlparse, base64
from urllib import unquote_plus, quote_plus

if platform.platform().startswith("Linux"):
    try:
        import requests
    except:
        arg="pip install requests"
        os.system(sys.executable+" "+sys.prefix+"/bin/"+arg)
        os.execv(sys.executable, ['python'] + sys.argv)
else:
    try:
        import requests
    except:
        subprocess.call(["python","-m","pip","install","requests"])
        import requests

print "\nqpython.net\n"

br = 1024**2
csize = 1024*8

deneme = 5

sessiz = False

def remove(string, table):
    for i in table:
        string = string.replace(i, '')
    return string

def get_real_url(url):
    return unquote_plus(remove(url, ['http://webproxy.at/surf/printer.php?u=', '&b=4']))

def get_name_cont(url):
    url = get_real_url(url)
    name = None
    if not sessiz: print 'Sunucudan dosya adı alınıyor'
    while True:
        try:
            r = requests.get(url, timeout = 30, stream = True)
            r.close()
            name = filename_from_headers(r.headers)
            break
        except:
            time.sleep(0.1)
    return name

def get_name(url):
    url = get_real_url(url)
    name = None
    if not sessiz: print 'Sunucudan dosya adı alınıyor'
    for i in range(deneme):
        try:
            r = requests.get(url, timeout = 5, stream = True)
            r.close()
            name = filename_from_headers(r.headers)
            break
        except:
            if not sessiz: print 'Deneme %s/%s' % (i+1, deneme)
            time.sleep(0.1)
    if name == None and not sessiz: print 'Sunucudan dosya adı alınamadı'
    return name

def select_name(url):
    name = get_name(url)
    if name == None:
        name = filename_from_url(url)
    return name

def get_size(filename):
    size = os.path.getsize(filename)
    if size < 0:
        output = subprocess.Popen(['ls', '-l', filename], stdout=subprocess.PIPE).communicate()[0]
        size = long(re.split(r'\s+', output)[3])
    return size

def format_size(bytes):
    if bytes >= br:
        return '%.1f MB' % (bytes/float(br))
    elif bytes >= 1024:
        return '%.1f KB' % (bytes/1024.0)
    else:
        return '%i B' % bytes

def filename_from_url(url):
    fname = os.path.basename(urlparse.urlparse(url).path)
    if len(fname.strip(" \n\t.")) == 0:
        return None
    return fname

def filename_from_headers(headers):
    if type(headers) == str:
        headers = headers.splitlines()
    if type(headers) == list:
        headers = dict([x.split(':', 1) for x in headers])
    cdisp = headers.get("Content-Disposition")
    if not cdisp:
        return None
    cdtype = cdisp.split(';')
    if len(cdtype) == 1:
        return None
    if cdtype[0].strip().lower() not in ('inline', 'attachment'):
        return None
    fnames = [x for x in cdtype[1:] if x.strip().startswith('filename=')]
    if len(fnames) > 1:
        return None
    name = fnames[0].split('=')[1].strip(' \t"')
    name = os.path.basename(name)
    if not name:
        return None
    return name

def exit(msg):
    print msg
    raise SystemExit()

def download_file(f, url):
    if not sessiz: print 'Dosya yolu: ', f
    if os.path.exists(f):
        existSize = get_size(f)
        hdrs = {'Range': 'bytes=%d-' % existSize}
    else:
        existSize = 0
        hdrs = {}
    if url.startswith('http://webproxy.at/'):
        hdrs['Referer'] = 'http://webproxy.at/surf/printer.php'
    if not sessiz: print 'İndirilen boyut:', format_size(existSize)
    try:
        r = requests.get(url, headers=hdrs, stream=True, timeout = 5)
        if not sessiz:
            print 'Sunucu cevabı: %d (%s)' % (r.status_code, r.reason)
            print 'URL:', r.url
        if not r.ok:
            if not sessiz: print 'İstek başarısız, durduruluyor.'
            return
        try:
            clength = int(r.headers['Content-Length']) + existSize
            if not sessiz: print 'Toplam boyut:', format_size(clength)
        except:
            clength = None
            if not sessiz: print 'Toplam boyut belirsiz'
        with open(f, 'ab') as fl:
            son = time.time()
            sayi=0
            for chunk in r.iter_content(csize):
                fl.write(chunk)
                existSize += csize
                sayi+=csize
                if sayi % br == 0 and not sessiz:
                    print existSize/br, 'MB' + (clength and ' | %' + str(existSize*100/clength) or ''), '|', format_size(br/(time.time()-son))+'/s'
                    son = time.time()
    except Exception as e:
        if not sessiz:
            print e
            print 'Bağlantı hatası, yeniden deneniyor'
        time.sleep(0.1)
        download_file(f, url)

if __name__ == '__main__':
    try:
        try:
            import android
            droid = android.Android()
            print 'android modülü yüklendi'
        except:
            import androidhelper
            droid = androidhelper.Android()
            print 'androidhelper modülü yüklendi'
    except:
        droid = None

    if droid:
        d = '/sdcard/'
    else:
        d = 'Download/'

    if not os.path.isdir(d):
        os.mkdir(d)

    def webproxy(link):
        return 'http://webproxy.at/surf/printer.php?u=' + quote_plus(link) + '&b=4'

    if droid:
        droid.dialogCreateAlert("İndirme tipi seçin")
        droid.dialogSetSingleChoiceItems(['webproxy.at', 'direkt indirme', 'toplu indirme'])
        droid.dialogSetPositiveButtonText("Tamam")
        droid.dialogShow()
        droid.dialogGetResponse()
        sonuc=droid.dialogGetSelectedItems().result[0]
        if sonuc < 2:
            link = droid.dialogGetInput('Dosya İndirici', 'Link girin:', droid.getClipboard().result).result
            if not link: exit('Geçersiz link')
            if not (link.startswith('http://') or link.startswith('https://')):
                exit('Geçersiz protokol')
            fname = select_name(link)
            fname = droid.dialogGetInput('Dosya İndirici', 'Dosyaya isim verin', fname).result
            if sonuc == 0:
                link = webproxy(link)
            download_file(d + fname, link)
        elif sonuc == 2:
            liste = droid.dialogGetInput('Dosya İndirici', 'Liste yolunu girin', '/sdcard/liste.txt').result
            with open(liste, 'r') as fl:
                lst = fl.read()
            tbl = lst.splitlines()
            for line in tbl:
                ln = line.split(',')
                if ln[2] == '1':
                    ln[1] = webproxy(ln[1])
                download_file(d+ln[0], ln[1])
    else:
        print '1 - webproxy'
        print '2 - direkt indirme'
        print '3 - liste indirme'
        sonuc = int(raw_input('Seçimini yap: '))
        if sonuc < 3:
            link = raw_input('Link girin: ')
            if not link: exit('Geçersiz link')
            if not (link.startswith('http://') or link.startswith('https://')):
                exit('Geçersiz protokol')
            fname = select_name(link)
            print 'Varsayılan dosya adı: %s' % fname
            fname2 = raw_input('Dosya ismi gir (girmezseniz varsayılan ad kullanılır): ')
            if fname2:
                fname = fname2
            if sonuc == 1:
                link = webproxy(link)
            download_file(d + fname, link)
        elif sonuc == 3:
            with open('liste.txt', 'r') as fl:
                lst = fl.read()
            tbl = lst.splitlines()
            for line in tbl:
                ln = line.split(',')
                if ln[2] == '1':
                    ln[1] = webproxy(ln[1])
                download_file(d+ln[0], ln[1])
