#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import sys
import subprocess
import random
import wclock
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt, QUrl
from PyQt4.QtGui import QApplication, QPalette

# ------------------------------------------------------------------ #
#                                                                    #
# http://doc.qt.io/qt-5/stylesheet-reference.html                    #
#                                                                    #
# http://doc.qt.io/qt-5/richtext-html-subset.html                    #
#                                                                    #
# ------------------------------------------------------------------ #

scriptPath = os.path.dirname(os.path.abspath(__file__))

def style():
    return(
        """
            QLabel {
                font-size: 20px;
                font-family: monospace;
                color: #BFBFBF;
            }
            QMainWindow {
                background: #2B2B2B;
            }
        """
    )

def styleHighlight():
    return 'color: {}; font-weight: bold;'.format('#00FFD7')

class ClockWindow(QtGui.QMainWindow):

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def keyPressEvent(self, e):
        key = e.key()
        if key == Qt.Key_Escape:
            QApplication.quit()

    def clockFace(self):
        result = ''
        face = wclock.Face()
        if self.face == face:
            return ''
        self.face = face

        face = face.split('\n')

        b = '<span style="{}">'.format(styleHighlight())
        e = '</span>'
        for row in face:
            result += '<div>{}</div>'.format(row).replace('[', b).replace(']', e)

        return result

    def updateFace(self):
        face = self.clockFace()
        if face == '': return
        self.label.setText(face)

    def __init__(self):
        super(ClockWindow, self).__init__()

        self.face = ''
        self.setWindowTitle('Word Clock')

        self.label = QtGui.QLabel()
        self.label.setTextFormat(Qt.RichText)
        self.setStyleSheet(style())
        self.updateFace()
        self.setCentralWidget(self.label)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateFace)
        self.timer.start(10000)

        self.setContentsMargins(80, 80, 80, 80)
        self.setFixedSize(0, 0)
        self.adjustSize()
        self.center()
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    win = ClockWindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
