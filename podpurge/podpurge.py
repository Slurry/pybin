#!/usr/bin/env python2.5

"""
podpurge will remove mp3 and mpg files in the specified folder that
are older than the number of days given specified.

podpurge base_path number_of_days_old
"""

import sys
import os
import time

def check_arguments(p, d):
    """ check_path expects a valid path and a numeric value. If either
    are not present False is returned
    """
    base_path = False
    days = False

    if os.path.exists(p):
        base_path = p

    try:
        days = int(d)
    except:
        pass
    return base_path, days

def prefix_zero(n):
    if int(n) < 10:
        return '0' + n
    else:
        return n

def get_old_files(p, d):
    seconds_in_day = 86400
    delete_files_dict = {}
    today = float(time.time())
    curyear = str(time.gmtime().tm_year)
    curmonth = prefix_zero(str(time.gmtime().tm_mon))
    curday = prefix_zero(str(time.gmtime().tm_mday))
    days = d
    path = p
    for (path, dirs, files) in os.walk(path):
#        print(path, dirs, files)
        os.chdir(path)
        for f in files:
            delete_flag = False
            if f != '.directory':
                file_time = os.path.getctime(f)
                rt = time.gmtime(file_time)
                filemonth = prefix_zero(str(rt.tm_mon))
                fileday = prefix_zero(str(rt.tm_mday))
                file_created_date = str(rt.tm_year) + filemonth + fileday

#                print(type(today),type(file_time))
                delete_flag = (today - file_time) > days * seconds_in_day
#                print(f, file_created_date, delete_flag)
                if delete_flag:
                    delete_files_dict[os.path.realpath(f)]=file_created_date
    return delete_files_dict

    
path, days = check_arguments(sys.argv[1],sys.argv[2])
#print(path, days, type(days))

old_files = get_old_files(path, days)

for k in old_files:
    print(k, old_files[k])



