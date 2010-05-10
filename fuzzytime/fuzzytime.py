#!/usr/bin/env python3.1
import time
while 1:
    tm = time.localtime()
    h = tm.tm_hour
    m = tm.tm_min
    s = tm.tm_sec

    min_sym = ''
    min_sym = '^' if m in range(0,5) else min_sym
    min_sym = '^+' if m in range(5,10)  else min_sym
    min_sym = '->' if m in range(10,15) else min_sym
    min_sym = '>' if m in range(15,20) else min_sym
    min_sym = '>+' if m in range(20,25) else  min_sym
    min_sym = '-v' if m in range(25,30) else  min_sym
    min_sym = 'v' if m in range(30,35) else min_sym 
    min_sym = 'v+' if m in range(35,40) else min_sym
    min_sym = '-<' if m in range(40,45) else min_sym
    min_sym = '<' if m in range(45,50) else min_sym 
    min_sym = '<+' if m in range(50,55) else min_sym
    min_sym = '-^' if m in range(55,60) else min_sym
    print (min_sym, h)
    time.sleep(60)
