import onebit
import os
import commands
import re

template = onebit.env.get_template("deleteapp.html")

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

try:
    f = open(os.environ['TM_PROJECT_DIRECTORY']+"/AndroidManifest.xml")
    text = f.read()
    com = re.compile('package[ ]*=[ ]*"[ 0-9a-zA-Z\.]+[ ]*"')
    package=''
    if com.search(text):
        package = com.search(text).group(0).replace(" ","").replace('package=', '').replace('"','');


    print template.render(
        title='Delete Android App', 
        package = package,
        device_str=device_str,
    )
except Exception, e:
    template = onebit.env.get_template("error.html")
    print template.render(
        title='Error',
        error=os.environ['TM_PROJECT_DIRECTORY']+"/AndroidManifest.xml not found."
    )


