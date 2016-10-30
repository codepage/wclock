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

    def minFMT(nMinFrom, nMinTo, val, repl = True):
        match = (nMinFrom <= MINUTE < nMinTo) or (nMinFrom == -1)
        fmtFace(match, val, repl)

    def hourFMT(nHour, val, repl = True):
        match = (nHour == HOUR) or (nHour == 0)
        fmtFace(match, val, repl)

    def fiveFMT():
        APP.face = APP.face.replace('*', '')

    # -------------------------------------------------------------------- #
    # actions
    # -------------------------------------------------------------------- #

    def buidFace():
        minFMT(-1, -1, "I T ' S")
        minFMT(-1, -1, 'A B O U T')

        if MINUTE < 35:
            [minFMT(*mi) for mi in [
                (15, 20, 'A'),
                (15, 20, 'Q U A R T E R'),
                (20, 30, 'T W E N T Y'),
                (25, 30, 'F I V E', False),
                (5, 10, 'F I V E'),
                (10, 15, 'T E N')
            ]]

            [hourFMT(*hour) for hour in [
                (9, 'N I N E'),    (1, 'O N E'),         (6, 'S I X'),
                (3, 'T H R E E'),  (4, 'F O U R'),       (5, '*F I V E*'),
                (2, 'T W O'),      (8, 'E I G H T'),     (11, 'E L E V E N'),
                (7, 'S E V E N'),  (12, 'T W E L V E'),  (10, 'T E N')
            ]]
        else:
            [minFMT(*mi) for mi in [
                (45, 50, 'A'),
                (45, 50, 'Q U A R T E R'),
                (35, 45, 'T W E N T Y'),
                (35, 40, 'F I V E', False),
                (55, 61, 'F I V E'),
                (50, 55, 'T E N')
            ]]

            [hourFMT(*hour) for hour in [
                (8, 'N I N E'),    (12, 'O N E'),        (5, 'S I X'),
                (2, 'T H R E E'),  (3, 'F O U R'),       (4, '*F I V E*'),
                (1, 'T W O'),      (7, 'E I G H T'),     (10, 'E L E V E N'),
                (6, 'S E V E N'),  (11, 'T W E L V E'),  (9, 'T E N')
            ]]

        [minFMT(*mi) for mi in [
            (0, 5, 'O C L O C K'),
            (5, 35, 'P A S T'),
            (30, 35, 'H A L F'),
            (35, 61, 'T O')
        ]]

        fiveFMT()

    buidFace()
    return APP.face

def Face():
    return getFace()

if __name__ == '__main__':
    print(Face())