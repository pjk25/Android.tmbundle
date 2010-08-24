import sys
import os
import commands

def main(*args):  
    apk = args[1].strip()
    device_str = ""
    if len(args) > 2:
        device = args[2].strip()
        device_str = "-s %s " % device
    
    apkpath = "%s/bin/%s" % (os.environ['TM_PROJECT_DIRECTORY'], apk)
    cmd = '"%s/tools/adb" %sinstall -r "%s"' % (os.environ['ANDROID_SDK'],device_str,  apkpath)
    return commands.getoutput(cmd)
    
if __name__ == "__main__":
    sys.stdout.write(main(*sys.argv))