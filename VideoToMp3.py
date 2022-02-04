#!/usr/bin/env python3

""" Video to Audio Encoder
   Required program
     - ffmpeg(You can use this  code (sudo apt-get install ffmpeg) on terminal or
               use this program (python3 converter.py -f) )
"""

__author__ = "H�seyin Altunkaynak"
__copyright__ = "Copyright 2017, H�seyin Altunkaynak"
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
 #dosya t�r�n�n desteklenip desteklenmedi�ini kontrol i�in
 fileName=fileName.split(".")
 for den in sort_of_file:
   if den == fileName[-1]:
     global currFileSort
     currFileSort = den
     return ".".join(fileName[0:-1])
   else:
     print("L�tfen desteklenen dosya t�rlerini giriniz.")
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
   epilog="Program� �al��t�rmak i�in sistemde ffmpeg y�kl� olmal�d�r.\
   Y�kl� de�il ise program� -f parametresi ile �al��t�r�n. Toplu dosya d�n���m� i�in kullan�lacak olan -m \
   parametresini kullan�rken program� dosyalar�n oldu�u dizinde �al��t�r�n.")
 parser.add_argument("-f", "--ffmpeg", help="ffmpeg paketini sisteme y�klemek i�in. Tek parametre olarak kullan�l�r.", action="store_true")
 parser.add_argument("-s", "--single", help="Tekli dosya d�n���m� i�in bulunulan dizindeki dosya ad�", metavar="FILE")
 parser.add_argument("-m", "--multiple", help="�oklu dosya d�n���m� i�in dosyalar�n bulundu�u klas�rde �al��t�r�n.\
   Tek parametre olarak kullan�l�r.", action="store_true")
 args = parser.parse_args()

 if args.ffmpeg:
   vta.app_install()
   
 if args.single:
   vta.converter(is_file(args.single))

 if args.multiple:
   vta.multipleConvert()
