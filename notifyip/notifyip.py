#!/usr/bin/python3.1
from time import sleep
import filecmp
import urllib
import os
import subprocess
home = os.path.expanduser('~')
site = 'http://admin:password@192.168.1.1/RST_status.htm'
def save_current_ip():

    os.chdir(os.path.expanduser('~'))
    get_page = subprocess.Popen(['wget', '-q', '-O', 'RST_status.htm', site])
    sleep(3)

    txt_conv = subprocess.Popen(['html2text', '-o', 'rst-status.txt', 'RST_status.htm',])

    fetchip = subprocess.Popen(['grep', '-m 1', 'IP Address', 'rst-status.txt'],
                           stdout = subprocess.PIPE).stdout.read()
    currentip = fetchip[21:].strip()
    print('currentip' , currentip)
    f = open('/home/jayson/currentip.txt','w')
    f.write(currentip)
    sleep(3)
    f.close()
    
    #os.remove('rst-status.txt')
    #os.remove('RST_status.htm')



    #os.system('dig jwmlt2 +short > currentip.txt')
    #ip = urllib.urlopen('http://whatismyip.org').read()
    ip = open('/home/jayson/currentip.txt','r').read()
    return ip

if os.path.isfile(home + '/currentip.txt') != True:
    print('\nipchange',)
    save_current_ip()
    
    os.system('/home/jayson/ipstatus')
else:
    lastip = open('/home/jayson/currentip.txt','r').read()


    get_page = subprocess.Popen(['wget', '-q','-O', 'RST_status.htm', site])
#    sleep(1)
    txt_conv = subprocess.Popen(['html2text', '-o', 'rst-status.txt', 'RST_status.htm',])
    sleep(1)

    fetchip = subprocess.Popen(['grep', '-m 1', 'IP Address', 'rst-status.txt'],
                           stdout = subprocess.PIPE).stdout.read()
    currentip = fetchip[21:].strip()
    f = open('/home/jayson/newestip.txt','w',)
    f.write(currentip)
    f.close()
    
    #os.system('dig jwmlt2 +short > /home/jayson/newestip.txt')
    newestip = open('/home/jayson/newestip.txt','r').read()
    #currentip = urllib.urlopen('http://whatismyip.org').read()
    if lastip.strip() != newestip.strip():
        os.remove('/home/jayson/currentip.txt')
        save_current_ip()
        os.system('/home/jayson/ipstatus')
        print "ipchange " + " to " + newestip
    else:
        print "NO CHANGE"
        
#if os.path.exists('/home/jayson/rst-status.txt') : os.remove('/home/jayson/rst-status.txt')
#if os.path.exists('/home/jayson/RST_status.htm') : os.remove('/home/jayson/RST_status.htm')
