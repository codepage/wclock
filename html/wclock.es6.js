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
    ].join('\n');

    const cNames = ['I T \' S', 'A B O U T', 'A', 'Q U A R T E R', 'T W E N T Y', 'F I V E', 'F I V E', 'T E N',
                   'N I N E', 'O N E', 'S I X', 'T H R E E', 'F O U R', '*F I V E*',
                   'T W O', 'E I G H T', 'E L E V E N', 'S E V E N', 'T W E L V E',
                   'T E N', 'O C L O C K', 'P A S T', 'H A L F', 'T O'];

    const cPre = [[-1, -1], [-1, -1]];

    const cTimes = MINUTE < 35 ? [[15, 20], [15, 20], [20, 30], [25, 30, false], [5, 10], [10, 15],
                                  [9], [1], [6], [3], [4], [5], [2], [8], [11], [7], [12], [10]]
                                 :
                                 [[45, 50], [45, 50], [35, 45], [35, 40, false], [55, 61], [50, 55],
                                  [8], [12], [5], [2], [3], [4], [1], [7], [10], [6], [11], [9]];

    const cPost = [[0, 5], [5, 35], [30, 35], [35, 61]];

    if (!changed()) return null;

    // ---------------------------------------------------------------------  //
    // functions
    // ---------------------------------------------------------------------  //

    function minMatch(minFrom, minTo) { return minFrom <= MINUTE && MINUTE < minTo };

    function changed() {
        let item = cTimes.filter(function(val) {
            return val.length > 1 && minMatch(val[0],  val[1]);
        });
        let val = item[0].toString();
        let change = val !== timeVal;
        if (change) timeVal = val;
        return change;
    }

    function fmtFace(match, val, repl = true) {
        const src = `[${val}]`;
        const fmt_on = `<span class='light'>${val}</span>`;
        if (match) {
            face = face.replace(src, fmt_on);
        } else if (repl) {
            face = face.replace(src, val);
        }
    }

    function minFMT(txt, times) {
        const [nMinFrom, nMinTo, repl] = times;
        const match = minMatch(nMinFrom, nMinTo) || (nMinFrom == -1);
        fmtFace(match, txt, repl);
    }

    function hourFMT(txt, times) {
        const [nHour, repl] = times;
        const match = (nHour == HOUR) || (nHour == 0);
        fmtFace(match, txt, repl);
    }

    function fmtFaceLines() {
        const lines = face.split('\n');
        for (let i = 0; i < lines.length; i++) {
            lines[i] = `<div class='row'>${lines[i]}</div>`;
        }
        face = lines.join('\n');
        face = face.replace('*', '').replace('*', '');
    }

    // ---------------------------------------------------------------------  //
    // actions
    // ---------------------------------------------------------------------  //

    // a bit weird... iterate joined arrays
    [].concat(cPre, cTimes, cPost).map(function(val, i) {
            let isHour = (val.length == 1);
            let txt = cNames[i];
            isHour ? hourFMT(txt, val) : minFMT(txt, val);
    });

    fmtFaceLines();

    return face;
}

function run() {
    let val = getFace();
    if (val) document.getElementById('clock').innerHTML = val;
    setTimeout(run, 15000);
}

window.onload = function() {
    run();
}
