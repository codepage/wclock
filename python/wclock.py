#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
#  This file is part of Word Clock
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                    Version 2, December 2004
#
# Copyright (C) 2017 xDaks <http://xdaks.deviantart.com/>
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

import sys
import datetime
import re

def getFace():
    # -------------------------------------------------------------------- #
    # vars
    # -------------------------------------------------------------------- #
    face = ([
        "(I T ' S) X (A B O U T) E",
        "(A) C (Q U A R T E R) D C",
        "(T W E N T Y) (F I V E) X",
        "(H A L F) B (T E N) F (T O)",
        "(P A S T) E R U (N I N E)",
        "(O N E) (S I X) (T H R E E)",
        "(F O U R) (F I V E) (T W O)",
        "(E I G H T) (E L E V E N)",
        "(S E V E N) (T W E L V E)",
        "(T E N) S E (O C L O C K)"
    ])

    startColor = ''
    endColor = ''

    fmt_on = ''
    fmt_off = ''

    rex = re.compile(r'\((.*?)\)')

    t = datetime.datetime.now()
    HOUR = t.hour % 12 or 12
    MINUTE = t.minute

    cTimes = (
        [
            [[-1, -1], [-1, -1]],
            [[15, 20], [15, 20]],
            [[20, 30], [25, 30, False], [5, 10]],
            [[30, 35], [10, 15], [35, 61]],
            [[5, 35], [9]],
            [[1], [6], [3]],
            [[4], [5], [2]],
            [[8], [11]],
            [[7], [12]],
            [[10], [0, 5]]
        ]
            if MINUTE < 35 else
        [
            [[-1, -1], [-1, -1]],
            [[45, 50], [45, 50]],
            [[35, 45], [35, 40, False], [55, 61]],
            [[30, 35], [50, 55], [35, 61]],
            [[5, 35], [8]],
            [[12], [5], [2]],
            [[3], [4], [1]],
            [[7], [10]],
            [[6], [11]],
            [[9], [0, 5]]
        ]
    )

    if (__name__ == '__main__'):
        if len(sys.argv) > 1 and sys.argv[1] == '-t':
            # terminal
            Color = '\033[38;5;43m'
            Color1 = '\033[38;5;66m'
            endColor = '\033[0m'

            fmt_on = endColor + Color + '{0}' + endColor + Color1
            fmt_off = '{0}'

            startColor = Color1
            endColor = endColor
        else:
            # conky
            fmt_on = '${{color}}{0}${{color1}}'
            fmt_off = '${{color1}}{0}${{color1}}'
    else:
        # terminal - curses
        fmt_on = '[{0}]'
        fmt_off = '{0}'

    # -------------------------------------------------------------------- #
    # functions
    # -------------------------------------------------------------------- #
    def fmtFace(row, match, val, repl):
        src = '({0})'.format(val)
        if match:
            return row.replace(src, fmt_on.format(val), 1)
        elif repl:
            return row.replace(src, fmt_off.format(val), 1)
        return row

    def minFMT(row, val, nMinFrom, nMinTo, repl = True):
        match = (nMinFrom <= MINUTE < nMinTo) or (nMinFrom == -1)
        return fmtFace(row, match, val, repl)

    def hourFMT(row, val, nHour, repl = True):
        match = (nHour == HOUR) or (nHour == 0)
        return fmtFace(row, match, val, repl)

    def getText(row):
        sr = rex.search(row)
        return sr.group(1) if sr else ''

    def getClockFace():
        return startColor + '\n'.join(face) + endColor

    # -------------------------------------------------------------------- #
    # actions
    # -------------------------------------------------------------------- #
    for i, row in enumerate(face):
        for val in cTimes[i]:
            isHour = len(val) == 1
            txt = getText(row)
            if txt != '':
                row = hourFMT(row, txt, *val) if isHour else minFMT(row, txt, *val)
        face[i] = row

    return getClockFace()

def Face():
    return getFace()

if __name__ == '__main__':
    print(Face())