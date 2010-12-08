import onebit
import os
import commands
import re

template = onebit.env.get_template("logcat.html")

cmd = "%s/platform-tools/adb devices" % (os.environ['ANDROID_SDK'])
devices = commands.getoutput(cmd)
devices = devices.replace("List of devices attached \n", "").split("\n")
device_str = ''
device_count = 0
for device in devices:
    if device!='':
        device_count+=1
        device_str += (device.split("\t")[0]+" ")
    
if device_str[0:20] == "* daemon not running":
    device_str = ""
    device_count = 0

print template.render(
    title='Logcat', 
    device_str=device_str,
)