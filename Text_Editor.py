import sys
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QColor, QTextCharFormat, QFont, QSyntaxHighlighter
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.intUI()
    def intUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        highlight = PythonHighlighter(self.textEdit)
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('micropython IDE')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UI()
    #ex = Widget()
    sys.exit(app.exec_())

