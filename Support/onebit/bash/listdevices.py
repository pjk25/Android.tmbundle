import sys
import os
import commands

def main(*args):    
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
    
    return device_str

if __name__ == "__main__":
    sys.stdout.write(main(*sys.argv))