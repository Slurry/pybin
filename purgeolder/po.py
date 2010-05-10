#!/usr/bin/python3.1

import os
import sys
import time
secaday = 86400 #seconds in a day
targetDir=sys.argv[1] #'/home/jayson/pybin/purgeolder/podcasts-testing' #
daysOld=int(sys.argv[2])
now = time.time()
directories=os.walk(targetDir)
def purge():

    if len(sys.argv) < 4:
        mode = 'dud'
        return 'dud. nothing done'
    
    mode = sys.argv[3]

    if sys.argv[3] != 'clobber':
        mode = 'donoharm'

    if mode != 'dud':
        for r, d, f in directories:
            for entry in f:
                path = str(r) + '/' + entry
                filectime = os.path.getctime(path)
                age = int((now - filectime) / secaday)
                if age >= daysOld:
                    if mode == 'donoharm':
                        print(entry, age, 'days old.')
                    
                    if mode == 'clobber':
                        print(entry, age, 'days old. REMOVING')
                        os.remove(path)
                        
        return "mode =" + mode
    else:
        print('dud. nothing done')
                
print(purge())
    
