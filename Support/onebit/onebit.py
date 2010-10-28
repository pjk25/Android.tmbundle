from jinjalib import Template, Environment
import os

from jinjalib.loaders import FileSystemLoader
env = Environment(loader=FileSystemLoader(os.environ['TM_BUNDLE_SUPPORT']+'/onebit/templates'))
    
    

import commands
cmds = (
    {'test':'which ant', 'error':'You do not have apache ant installed.'},
    {'test':'which "$ANDROID_SDK"/"tools/android"', 'error':'$ANDROID_SDK/tools/android could not be found'},
    {'test':'which "$ANDROID_SDK"/"tools/emulator"', 'error':'$ANDROID_SDK/tools/emulator could not be found'},
    {'test':'which "$ANDROID_SDK"/"tools/adb"', 'error':'$ANDROID_SDK/tools/adb could not be found'},
)
for cmd in cmds:
    if commands.getoutput(cmd['test']) == '':
        import sys
        template = env.get_template("error.html")
        sys.exit(template.render(
            sdk=('ANDROID_SDK' in os.environ),
            title='Error', 
            error=cmd['error'],
        ))



