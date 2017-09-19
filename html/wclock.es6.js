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

let timeVal = '';

function getFace() {

    // ---------------------------------------------------------------------  //
    // vars
    // ---------------------------------------------------------------------  //

    const t = new Date();

    const HOUR = t.getHours() % 12 || 12;

    const MINUTE = t.getMinutes();

    let face = [
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

    const cTimes = MINUTE < 35 ? [
        [[-1, -1], [-1, -1]],
        [[15, 20], [15, 20]],
        [[20, 30], [25, 30, false], [5, 10]],
        [[30, 35], [10, 15], [35, 61]],
        [[5, 35], [9]],
        [[1], [6], [3]],
        [[4], [5], [2]],
        [[8], [11]],
        [[7], [12]],
        [[10], [0, 5]]
     ]
     :
     [
        [[-1, -1], [-1, -1]],
        [[45, 50], [45, 50]],
        [[35, 45], [35, 40, false], [55, 61]],
        [[30, 35], [50, 55], [35, 61]],
        [[5, 35], [8]],
        [[12], [5], [2]],
        [[3], [4], [1]],
        [[7], [10]],
        [[6], [11]],
        [[9], [0, 5]]
     ];


    if (!changed()) return null;

    // ---------------------------------------------------------------------  //
    // functions
    // ---------------------------------------------------------------------  //

    function minMatch(minFrom, minTo) { return minFrom <= MINUTE && MINUTE < minTo };

    function changed() {
        let item;
        for (let row of cTimes) {
            item = row.filter(val => val.length > 1 && minMatch(val[0],  val[1]));
            if (item.length > 0) break;
        };
        const val = item.toString();
        const change = val !== timeVal;
        if (change) timeVal = val;
        return change;
    }

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

    // ---------------------------------------------------------------------  //
    // actions
    // ---------------------------------------------------------------------  //

    let rows = face.map((row, i) => {
        cTimes[i].forEach(val => {
            let isHour = (val.length == 1);
            let txt = getText(row);
            if (txt != '') {
                row = isHour ? hourFMT(row, txt, val) : minFMT(row, txt, val);
            }
        });
        return row;
    });

    return fmtFaceLines(rows);
}

function run() {
    let val = getFace();
    if (val) document.getElementById('clock').innerHTML = val;
    setTimeout(run, 15000);
}

window.addEventListener('load', run);
