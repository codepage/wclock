#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  This file is part of Word Clock
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                    Version 2, December 2004
#
# Copyright (C) 2016 xDaks <http://xdaks.deviantart.com/>
#
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
#  0. You just DO WHAT THE FUCK YOU WANT TO.
#

import curses
import sys
import os
import time
import wclock

os.environ["TERM"] = "xterm-256color"

def main(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()

    for i in range(0, curses.COLORS):
        curses.init_pair(i, i, -1);

    color0 = curses.color_pair(243)
    color1 = curses.color_pair(85)
    color = color0

    try:
        while True:
            #stdscr.clear()
            stdscr.erase()
            face = wclock.Face()
            for ch in face:
                if ch in ['[', ']']:
                    color = color1 if ch == '[' else color0
                    continue
                stdscr.addstr(ch, color)
            stdscr.refresh()
            time.sleep(15)
    except:
        pass

curses.wrapper(main)
os.system('clear')