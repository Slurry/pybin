#!/usr/bin/python3.1
import subprocess
import time
import os

log = open('/var/log/notifyip.log','a')
log.write('notify ip servers started at {}\n'.format(time.strftime('%#c')))
log.flush()

while True:
    process = subprocess.Popen('notifyip', shell=None, stdout=subprocess.PIPE)
    result = process.communicate()[0].decode('UTF8').strip()
    process.wait()
    #print(result)
    if "ipchange" in result:
        log.write('{} {}\n'.format(time.strftime('%#c'), result))
        log.flush()
    time.sleep(300)
