#!/usr/bin/python3.1

import subprocess
import time

subprocess.Popen('clear')

t = time.localtime()
start_time = "{0}-{1:02d}-{2:02d} {3:02}:{4:02}".format(t.tm_year, t.tm_mon, t.tm_mday,
                                                    t.tm_hour, t.tm_min)
temps = []
while True:
    process = subprocess.Popen(["acpi", "-tf"], shell=False,
                            stdout = subprocess.PIPE)

    result = process.communicate()[0].decode('UTF8')
    temp_string = result.split(',')[1].strip()
    temp = float(temp_string.split()[0])
    temps.append(temp)
    adverage_temp = sum(temps) / len(temps)
    print('Adverage temp is {0:.2f} as of {1}'.format(adverage_temp, start_time))
    print('Actual temp is {0:.2f}'.format(temp))
    print('{} samples'.format(len(temps)))
    time.sleep(30)
    subprocess.Popen('clear')
    
