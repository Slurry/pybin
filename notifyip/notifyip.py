#!/usr/bin/env python

import filecmp
import urllib
import os
import subprocess
home = os.path.expanduser('~')

def save_current_ip():

    os.chdir(os.path.expanduser('~'))
    os.system('dig jwmlt2 +short > currentip.txt')
    #ip = urllib.urlopen('http://whatismyip.org').read()
    ip = open('/home/jayson/currentip.txt','r').read()
    return ip

if os.path.isfile(home + '/currentip.txt') != True:
    save_current_ip()
    os.system('/home/jayson/ipstatus')
else:
    lastip = open('/home/jayson/currentip.txt','r').read()
    os.system('dig jwmlt2 +short > /home/jayson/newestip.txt')
    newestip = open('/home/jayson/newestip.txt','r').read()
    #currentip = urllib.urlopen('http://whatismyip.org').read()
    if lastip.strip() != newestip.strip():
        os.remove('/home/jayson/currentip.txt')
        save_current_ip()
        os.system('/home/jayson/ipstatus')
        print "IP address changed from " + lastip + " to " + newestip
    else:
        print "NO CHANGE"
        
