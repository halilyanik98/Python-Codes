import pynotify , os ,time
not_executed = 1
i=1
fileHandle = open ( 'uyarici.txt' )
while 1:
	time.sleep(50)
	dt = list(time.localtime())
	minute = dt[4]
	if  minute == 15  or minute == 30  or minute==0  or minute==45 :
		lineList = fileHandle.readline()
		fileHandle.tell()
		if lineList == 'end/n' or lineList =='' or lineList == '/n':
			fileHandle.seek (0)
		
		try:
			if pynotify.init("Uyarici"):
				Alert = pynotify.Notification("Ayet", str(lineList))
				Alert.show()
			else:
				print "pynotify baslatilamadi."
		except:
			print "pynotify kurulmadi."

fileHandle.close()

