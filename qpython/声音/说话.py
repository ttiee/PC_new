import androidhelper

droid = androidhelper.Android()
#while True:
#	message = input('What?\n')
#	droid.ttsSpeak(message)
	
#a = droid.getClipboard().result
#print(a)
#droid.vibrate(100)

#droid.viewHtml('/storage/emulated/0/qpython/爬虫/01.html')
#droid.viewMap('披萨')
#droid.search('https://h5mota.com/games/51/')
#a = droid.readBatteryData()
#print(a)
#a = droid.batteryGetTemperature()
#print(a)

#droid.dialogCreateNFCBeamSlave('标题','消息')

#droid.dialogCreateTimePicker(24,60,True)

#droid.dialogCreateAlert('标题','没电了！')

droid.notify('title',' message')

#droid.cameraCapturePicture('/storage/emulated/0/qpython/爬虫/')


a = droid.getInput('title', 'message').result
print(a)
droid.makeToast('message')











