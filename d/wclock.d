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
// import std.regex;

struct TRS {
    int From;
    int To;
    bool Repl;
    bool IsHr = false;
}

// auto re = regex(`\((.*?)\)`);

auto mir = (int f, int t, bool r = true) => TRS(f, t, r);
auto hr  = (int f) => TRS(f, 0, true, true);

string[] face = [
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
];


int HOUR;
int MINUTE;

string startColor = "";
string endColor = "";

string fmt_on = "";
string fmt_off = "";

string fmtFace(string row, bool match, string val, bool repl) {
    string src = format("(%s)", val);
    if (match) {
        return replaceFirst(row, src, format(fmt_on, val));
    } else if (repl) {
        return replaceFirst(row, src, format(fmt_off, val));
    }
    return row;
}

string minFMT(string row, string val, TRS trs) {
    bool match = (trs.From <= MINUTE && MINUTE < trs.To) || (trs.From == -1);
    return fmtFace(row, match, val, trs.Repl);
}

string hourFMT(string row, string val, TRS trs) {
    bool match = (trs.From == HOUR) || (trs.From == 0);
    return fmtFace(row, match, val, trs.Repl);
}

string getText(string row) {
    long b = indexOf(row, "(");
    long e = indexOf(row, ")");
    return (b == -1 || e == -1) ? "" : row[b + 1..e];
}

string getClockFace() {
    return startColor ~ face.join('\n') ~ endColor;
}

/*
string get_text() {
    auto c = matchFirst(face, re);
    return (!c.empty) && (c.length > 1) ? c[1] : "";
}
*/

void getFace() {

    TRS[][] CTimes;
    if (MINUTE < 35) {
        CTimes = [
            [mir(-1, -1), mir(-1, -1)],
            [mir(15, 20), mir(15, 20)],
            [mir(20, 30), mir(25, 30, false), mir(5, 10)],
            [mir(30, 35), mir(10, 15), mir(35, 61)],
            [mir(5, 35), hr(9)],
            [hr(1), hr(6), hr(3)],
            [hr(4), hr(5), hr(2)],
            [hr(8), hr(11)],
            [hr(7), hr(12)],
            [hr(10), mir(0, 5)]
            ];
    } else {
        CTimes = [
            [mir(-1, -1), mir(-1, -1)],
            [mir(45, 50), mir(45, 50)],
            [mir(35, 45), mir(35, 40, false), mir(55, 61)],
            [mir(30, 35), mir(50, 55), mir(35, 61)],
            [mir(5, 35), hr(8)],
            [hr(12), hr(5), hr(2)],
            [hr(3), hr(4), hr(1)],
            [hr(7), hr(10)],
            [hr(6), hr(11)],
            [hr(9), mir(0, 5)]
        ];
    }

    string txt;
    foreach (i, string row; face) {
        foreach (TRS val; CTimes[i]) {
            txt = getText(row);
            if (txt != "") {
                row = val.IsHr ? hourFMT(row, txt, val) : minFMT(row, txt, val);
            }
        }
        face[i] = row;
    }
    writeln(getClockFace());
}

void init(string[] args) {

    SysTime currentTime = Clock.currTime();
    HOUR = currentTime.hour % 12 == 0 ? 12 : currentTime.hour % 12;
    MINUTE = currentTime.minute;

    if (args.length > 1 && args[1] == "-t") {

        string Color = "\033[38;5;43m";
        string Color1 = "\033[38;5;66m";
        string endColor = "\033[0m";

        fmt_on = endColor ~ Color ~ "%s" ~ endColor ~ Color1;
        fmt_off = "%s";

        startColor = Color1;
        endColor = endColor;
    } else {

        fmt_on = "${{color}}%s${{color1}}";
        fmt_off = "${{color1}}%s${{color1}}";
    }
}

void main(string[] args) {
    init(args);
    getFace();
}