import sys
import os
import pexpect

def main(*args):  
    
    cmd = '"%s/tools/android" create avd -n %s -t %s' % (os.environ['ANDROID_SDK'], args[1], args[2])
         
    child = pexpect.spawn(cmd)
    
    try:
        child.expect('Do you wish to create.*')

        child.sendline("yes")

        child.expect('SD Card support.*')
        child.sendline(args[3])

        child.expect('Abstracted.*')
        child.sendline(args[4])

        child.expect('DPad support.*')
        child.sendline(args[5])

        child.expect('Accelerometer.*')
        child.sendline(args[6])

        child.expect('Maximum horizontal.*')
        child.sendline(args[7])

        child.expect('Cache partition.*')
        child.sendline(args[8])

        child.expect('Audio playback.*')
        child.sendline(args[9])

        child.expect('Track-ball support.*')
        child.sendline(args[10])

        child.expect('Maximum vertical.*')
        child.sendline(args[11])

        child.expect('Camera support.*')
        child.sendline(args[12])

        child.expect('Battery support.*')
        child.sendline(args[13])

        child.expect('Touch-screen support.*')
        child.sendline(args[14])

        child.expect('Audio recording support.*')
        child.sendline(args[15])

        child.expect('GPS support.*')
        child.sendline(args[16])
        
        child.expect('Cache partition support.*')
        child.sendline(args[17])

        child.expect('Keyboard support.*')
        child.sendline(args[18])

        child.expect('Max VM application.*')
        child.sendline(args[19])

        child.expect('Device ram size.*')
        child.sendline(args[20])

        child.expect('GSM modem support.*')
        child.sendline(args[21])

        child.expect ('\r\n')
        
        if(str(child).find("before (last 100 chars): hw.gsmModem [yes]:yes")!=-1 or str(child).find("exitstatus: None")!=-1):
            return str("OK")

        return str(child)
            
    except Exception, e:
        return str(e)
    
    
    
        
if __name__ == "__main__":
    sys.stdout.write(main(*sys.argv))