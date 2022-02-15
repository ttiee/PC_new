import qpy

import androidhelper
droid = androidhelper.Android()

ret = droid. cameraCapturePicture(qpy.tmp+"/test.png").result
#ret = droid. cameraInteractiveCapturePicture(qpy.tmp+"/test.png").result

print("Result:"+str(ret))
print("Please open "+qpy.tmp+"/test.png"+" to check the picutre")
