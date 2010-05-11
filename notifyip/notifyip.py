#!/usr/bin/python3.1
import time
import urllib.request
import os
import subprocess
import re

log = '/var/log/notifyip.log'
logfile = open(log,'a')
logfile.write('Notifyip service started at {}\n'.format(time.strftime('%#c')))
time.sleep(3)
logfile.close

regex = re.compile('>[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+<')
currentip_file = '/home/jayson/currentip.txt'
#get router status page and extract current ip
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
top_level_url = 'http://192.168.1.1/'
user = 'admin'
password = 'password'
password_mgr.add_password(None, top_level_url, user, password)
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
opener = urllib.request.build_opener(handler)
urllib.request.install_opener(opener)
f = urllib.request.urlopen('http://192.168.1.1/RST_status.htm')
page= str(f.read())
addresses = regex.findall(page)
newestip = addresses[0].strip('<>')


def sendip(ip):
    cmd = ['sendEmail','-f', 'williams.jasyon@gmail.com',
           '-t', 'williams.jayson@gmail.com',
           'jwilli7@amerigroupcorp.com',
           '-u', ip, '-s', 'smtp.gmail.com:587',
           '-xu', 'williams.jayson', '-xp', 'password',
           '-m', ip]

    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    result = process.communicate()[0].decode('UTF')
    logfile = open(log,'a')
    logfile.write(result)
    time.sleep(3)
    logfile.close()
    
    
# get last ip fetch from file or create one
exitflag = False
while not exitflag:

    if os.path.exists(currentip_file):
        file = open(currentip_file,'r')
        lastip  = file.read().strip()
        file.close()
        if lastip == newestip:
            pass
            #print('no change in ip address ', lastip)
        else:
            file = open(currentip_file,'w')
            file.write(newestip)
            file.close
            file = open(log,'a')
            logfile.write('{}-ip changed from {} to {}\n'.format(time.strftime('%#c'), lastip, newestip))
            time.sleep(3)
            sendip(newestip)
    else:
        file = open(currentip_file,'w')
        file.write(newestip)
        logfile = open(log,'a')
        logfile.write('creating currentip.txt file. IP is {}\n'.format(newestip))
        time.sleep(3)
        file.close()
        logfile.close()
        sendip(newestip)

#    exitflag = True
    time.sleep(300)



