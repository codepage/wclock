/* -----------------------------------------------------------------------------

DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
        Version 2, December 2004

Copyright (C) 2016 xDaks <http://xdaks.deviantart.com/>

Everyone is permitted to copy and distribute verbatim or modified
copies of this license document, and changing it is allowed as long
as the name is changed.

DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

0. You just DO WHAT THE FUCK YOU WANT TO.

----------------------------------------------------------------------------- */

var timeVal = '';

function getFace() {

    // ---------------------------------------------------------------------  //
    // vars
    // ---------------------------------------------------------------------  //

    const t = new Date();

    const HOUR = t.getHours() % 12 || 12;

    const MINUTE = t.getMinutes();

    // ---------------------------------------------------------------------  //
    // functions
    // ---------------------------------------------------------------------  //

    function minMatch(minFrom, minTo) { return minFrom <= MINUTE && MINUTE < minTo };

    function fmtFace(row, match, val, repl = true) {
        const src = `(${val})`;
        const fmt_on = `<span class='light'>${val}</span>`;
        if (match) {
            return row.replace(src, fmt_on);
        } else if (repl) {
            return row.replace(src, val);
        }
        return row
    }

    function minFMT(row, txt, times) {
        const [nMinFrom, nMinTo, repl] = times;
        const match = minMatch(nMinFrom, nMinTo) || (nMinFrom == -1);
        return fmtFace(row, match, txt, repl);
    }

    function hourFMT(row, txt, times) {
        const [nHour, repl] = times;
        const match = (nHour == HOUR) || (nHour == 0);
        return fmtFace(row, match, txt, repl);
    }

    function fmtFaceLines(rows) {
        const lines = rows.map(item => `<div class='row'>${item}</div>`);
        return lines.join('\n');
    }

    function getText(row) {
        b = row.indexOf('(');
        e = row.indexOf(')');
        return (b == -1 || e == -1) ? '' : row.substring(b + 1, e);
    }

    function R(row, t1, t2) {
        let t = MINUTE <= 35 ? t1 : t2;
        t.forEach(val => {
            let isHour = (val.length == 1);
            let txt = getText(row);
            if (txt != '') {
                row = isHour ? hourFMT(row, txt, val) : minFMT(row, txt, val);
            }
        });
        return row
    }

    // ---------------------------------------------------------------------  //
    // actions
    // ---------------------------------------------------------------------  //

    let rows = [
            R("(I T ' S) X (A B O U T) E",    [[-1, -1], [-1, -1]],                   [[-1, -1], [-1, -1]]),
            R("(A) C (Q U A R T E R) D C",    [[15, 20], [15, 20]],                   [[45, 50], [45, 50]]),
            R("(T W E N T Y) (F I V E) X",    [[20, 30], [25, 30, false], [5, 10]],   [[35, 45], [35, 40, false], [55, 61]]),
            R("(H A L F) B (T E N) F (T O)",  [[30, 35], [10, 15], [35, 61]],         [[30, 35], [50, 55], [35, 61]]),
            R("(P A S T) E R U (N I N E)",    [[5, 35], [9]],                         [[5, 35], [8]]),
            R("(O N E) (S I X) (T H R E E)",  [[1], [6], [3]],                        [[12], [5], [2]]),
            R("(F O U R) (F I V E) (T W O)",  [[4], [5], [2]],                        [[3], [4], [1]]),
            R("(E I G H T) (E L E V E N)",    [[8], [11]],                            [[7], [10]]),
            R("(S E V E N) (T W E L V E)",    [[7], [12]],                            [[6], [11]]),
            R("(T E N) S E (O C L O C K)",    [[10], [0, 5]],                         [[9], [0, 5]])
    ];

    return fmtFaceLines(rows);
}

function run() {
    let val = getFace();
    if (val && timeVal !== val) {
        document.getElementById('clock').innerHTML = val;
        timeVal = val;
    }
    setTimeout(run, 15000);
}

window.addEventListener('load', run);