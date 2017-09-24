//
//
//    This file is part of Word Clock
//
//              DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
//                      Version 2, December 2004
//
//   Copyright (C) 2017 xDaks <http://xdaks.deviantart.com/>
//
//   Everyone is permitted to copy and distribute verbatim or modified
//   copies of this license document, and changing it is allowed as long
//   as the name is changed.
//
//              DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
//     TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
//
//    0. You just DO WHAT THE FUCK YOU WANT TO.
//
//

import std.stdio;
import std.datetime;
import std.format;
import std.array;
import std.string;

struct TimeRangeStruct {
    int From,  To;
    bool Repl, IsHour;
}

alias trs = TimeRangeStruct;

trs rs(int f, int t, bool r = true) {return trs(f, t, r);}
trs rs(int f) {return trs(f, 0, true, true);}

int HOUR;
int MINUTE;
string[] face;
string fmt_on;
string fmt_off;
string Color1;
string EndColor;

void init(string[] args) {
    SysTime currentTime = Clock.currTime();

    HOUR = currentTime.hour % 12 == 0 ? 12 : currentTime.hour % 12;
    MINUTE = currentTime.minute;

    if (args.length > 1 && args[1] == "-t") {
        string Color = "\033[38;5;43m";
        Color1 = "\033[38;5;66m";
        EndColor = "\033[0m";

        fmt_on = EndColor ~ Color ~ "%s" ~ EndColor ~ Color1;
        fmt_off = "%s";
    } else {
        fmt_on = "${{color}}%s${{color1}}";
        fmt_off = "${{color1}}%s${{color1}}";
    }
}

string fmtFace(string row, bool match, string val, bool repl) {
    string src = format("(%s)", val);
    if (match) {
        return replaceFirst(row, src, format(fmt_on, val));
    } else if (repl) {
        return replaceFirst(row, src, format(fmt_off, val));
    }
    return row;
}

string rowFmt(string row, string val, trs t) {
    bool match = t.IsHour ?
                (t.From == HOUR) || (t.From == 0) :
                (t.From <= MINUTE && MINUTE < t.To) || (t.From == -1);
    return fmtFace(row, match, val, t.Repl);
}

string get_text(string row) {
    long b = indexOf(row, "(");
    long e = indexOf(row, ")");
    return (b == -1 || e == -1) ? "" : row[b + 1..e];
}

string R(string row, trs[] t1, trs[] t2) {
    auto t = (MINUTE < 35) ? t1 : t2;
    string txt;

    foreach (i, trs val; t) {
        txt = get_text(row);
        if (txt != "") row = rowFmt(row, txt, val);
    }
    return row;
}

string get_face(string[] rows) {
    return Color1 ~ rows.join("\n") ~ EndColor;
}

void main(string[] args) {
    init(args);

    auto rows = [
        R("(I T ' S) X (A B O U T) E",      [rs(-1, -1), rs(-1, -1)],                     [rs(-1, -1), rs(-1, -1)]),
        R("(A) C (Q U A R T E R) D C",      [rs(15, 20), rs(15, 20)],                     [rs(45, 50), rs(45, 50)]),
        R("(T W E N T Y) (F I V E) X",      [rs(20, 30), rs(25, 30, false), rs(5, 10)],   [rs(35, 45), rs(35, 40, false), rs(55, 61)]),
        R("(H A L F) B (T E N) F (T O)",    [rs(30, 35), rs(10, 15), rs(35, 61)],         [rs(30, 35), rs(50, 55), rs(35, 61)]),
        R("(P A S T) E R U (N I N E)",      [rs(5, 35), rs(9)],                           [rs(5, 35), rs(8)]),
        R("(O N E) (S I X) (T H R E E)",    [rs(1), rs(6), rs(3)],                        [rs(12), rs(5), rs(2)]),
        R("(F O U R) (F I V E) (T W O)",    [rs(4), rs(5), rs(2)],                        [rs(3), rs(4), rs(1)]),
        R("(E I G H T) (E L E V E N)",      [rs(8), rs(11)],                              [rs(7), rs(10)]),
        R("(S E V E N) (T W E L V E)",      [rs(7), rs(12)],                              [rs(6), rs(11)]),
        R("(T E N) S E (O C L O C K)",      [rs(10), rs(0, 5)],                           [rs(9), rs(0, 5)])
    ];

    writeln(get_face(rows));
}