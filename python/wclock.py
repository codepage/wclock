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


def getFace():
    # -------------------------------------------------------------------- #
    # vars
    # -------------------------------------------------------------------- #
    class APP:
        face = '\n'.join([
            "[I T ' S] X [A B O U T] E",
            "[A] C [Q U A R T E R] D C",
            "[T W E N T Y] [F I V E] X",
            "[H A L F] B [T E N] F [T O]",
            "[P A S T] E R U [N I N E]",
            "[O N E] [S I X] [T H R E E]",
            "[F O U R] [*F I V E*] [T W O]",
            "[E I G H T] [E L E V E N]",
            "[S E V E N] [T W E L V E]",
            "[T E N] S E [O C L O C K]"
        ])

    fmt_on = ''
    fmt_off = ''

    t = datetime.datetime.now()
    HOUR = t.hour % 12 or 12
    MINUTE = t.minute

    CNames = ['I T \' S', 'A B O U T', 'A', 'Q U A R T E R', 'T W E N T Y', 'F I V E', 'F I V E', 'T E N',
              'N I N E', 'O N E', 'S I X', 'T H R E E', 'F O U R', '*F I V E*',
              'T W O', 'E I G H T', 'E L E V E N', 'S E V E N', 'T W E L V E',
              'T E N', 'O C L O C K', 'P A S T', 'H A L F', 'T O']

    CPre = [[-1, -1], [-1, -1]]

    CTimes = ([[15, 20], [15, 20], [20, 30], [25, 30, False], [5, 10], [10, 15],
               [9], [1], [6], [3], [4], [5], [2], [8], [11], [7], [12], [10]]
           if MINUTE < 35 else
              [[45, 50], [45, 50], [35, 45], [35, 40, False], [55, 61], [50, 55],
               [8], [12], [5], [2], [3], [4], [1], [7], [10], [6], [11], [9]])

    CPost = [[0, 5], [5, 35], [30, 35], [35, 61]]

    cTimeData = CPre + CTimes + CPost

    if (__name__ == '__main__'):
        if len(sys.argv) > 1 and sys.argv[1] == '-t':
            # terminal
            Color = '\033[38;5;10m'
            Color1 = '\033[38;5;6m'
            endColor = '\033[0m'

            fmt_on = endColor + Color + '{0}' + endColor + Color1
            fmt_off = '{0}'

            APP.face = Color1 + APP.face + endColor
        else:
            # conky
            fmt_on = '${{color}}{0}${{color1}}'
            fmt_off = '${{color1}}{0}${{color1}}'
    else:
        # terminal - curses
        fmt_on = '({0})'
        fmt_off = '{0}'

    # -------------------------------------------------------------------- #
    # functions
    # -------------------------------------------------------------------- #
    def fmtFace(match, val, repl):
        src = '[{0}]'.format(val)
        if match:
            APP.face = APP.face.replace(src, fmt_on.format(val), 1)
        elif repl:
            APP.face = APP.face.replace(src, fmt_off.format(val), 1)

    def minFMT(val, nMinFrom, nMinTo, repl = True):
        match = (nMinFrom <= MINUTE < nMinTo) or (nMinFrom == -1)
        fmtFace(match, val, repl)

    def hourFMT(val, nHour, repl = True):
        match = (nHour == HOUR) or (nHour == 0)
        fmtFace(match, val, repl)

    def fiveFMT():
        APP.face = APP.face.replace('*', '')

    # -------------------------------------------------------------------- #
    # actions
    # -------------------------------------------------------------------- #
    for i, val in enumerate(cTimeData):
        isHour = len(val) == 1
        txt = CNames[i]
        hourFMT(txt, *val) if isHour else minFMT(txt, *val)

    fiveFMT()

    return APP.face

def Face():
    return getFace()

if __name__ == '__main__':
    print(Face())