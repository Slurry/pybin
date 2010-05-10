#!/usr/bin/env python3.1

import curses
import curses.wrapper
import curses.textpad
import time


def testing(stdscr):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    stdscr.box()
    stdscr.addstr(10, 0, "has color" + str(curses.has_colors()),\
                      curses.color_pair(1))
    stdscr.refresh()
    statusx = 0; statusy = 20; height = 1; width = 30
    win = curses.newwin(height, width, statusy, statusx)
    win.addstr(0, 0, "this is the first line")
    win.refresh()
    time.sleep(3)
    win.addstr(0, 0, "this is line two blink",curses.A_BLINK)
    win.refresh()
    time.sleep(3)

#stdscr = curses.initscr()
curses.wrapper(testing)
