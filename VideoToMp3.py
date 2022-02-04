#!/usr/bin/env python3

""" Video to Audio Encoder
   Required program
     - ffmpeg(You can use this  code (sudo apt-get install ffmpeg) on terminal or
               use this program (python3 converter.py -f) )
"""

__author__ = "Hüseyin Altunkaynak"
__copyright__ = "Copyright 2017, Hüseyin Altunkaynak"
__license__ = "GNU General Public License"
__version__ = "1.0.0"
__email__ = "huseyin.altunkaynak51@gmail.com"

import subprocess
import argparse
import os
import sys

sort_of_file=["mp4", "mov", "m4a", "3gp", "3g2", "mj2"]
currFileSort="mp4"

def is_file(fileName):
 #dosya türünün desteklenip desteklenmediðini kontrol için
 fileName=fileName.split(".")
 for den in sort_of_file:
   if den == fileName[-1]:
     global currFileSort
     currFileSort = den
     return ".".join(fileName[0:-1])
   else:
     print("Lütfen desteklenen dosya türlerini giriniz.")
     for ben in sort_of_file:
       print(ben)
     sys.exit()

class VideoToAudio(object):
 """Video To Audio Encoder"""
 def __init__(self):
   self.currPath = os.getcwd()

 def app_install(self):
   subprocess.run(["sudo", "apt-get", "install", "ffmpeg"])

 def converter(self, fileName):
   pathWay=self.currPath+"/"+fileName+"."+currFileSort
   subprocess.run(["ffmpeg", "-i", pathWay, self.currPath+"/"+fileName+".mp3"])

 def multipleConvert(self):
   files=os.listdir()
   for sen in files:
     sen = sen.split(".")
     for cen in sort_of_file:
       if cen == sen[-1]:
         currFileSort = cen
         self.converter(".".join(sen[0:-1]))
       else:
         continue


if __name__ == '__main__':
 vta = VideoToAudio()

 parser = argparse.ArgumentParser(description="Video to Audio Encoder",
   epilog="Programý çalýþtýrmak için sistemde ffmpeg yüklü olmalýdýr.\
   Yüklü deðil ise programý -f parametresi ile çalýþtýrýn. Toplu dosya dönüþümü için kullanýlacak olan -m \
   parametresini kullanýrken programý dosyalarýn olduðu dizinde çalýþtýrýn.")
 parser.add_argument("-f", "--ffmpeg", help="ffmpeg paketini sisteme yüklemek için. Tek parametre olarak kullanýlýr.", action="store_true")
 parser.add_argument("-s", "--single", help="Tekli dosya dönüþümü için bulunulan dizindeki dosya adý", metavar="FILE")
 parser.add_argument("-m", "--multiple", help="Çoklu dosya dönüþümü için dosyalarýn bulunduðu klasörde çalýþtýrýn.\
   Tek parametre olarak kullanýlýr.", action="store_true")
 args = parser.parse_args()

 if args.ffmpeg:
   vta.app_install()
   
 if args.single:
   vta.converter(is_file(args.single))

 if args.multiple:
   vta.multipleConvert()
