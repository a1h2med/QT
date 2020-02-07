import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

#
#
#
#
############ Signal Class ############
#
#
#
#
class Signal(QObject):

    # initializing a Signal which will take (string) as an input
    reading = pyqtSignal(str)

    # init Function for the Signal class
    def __init__(self):
        QObject.__init__(self)

#
#
############ end of Class ############
#
#

# Making text editor as A global variable (to solve the issue of being local to (self) in widget class)
text = QTextEdit

#
#
#
#
############ Widget Class ############
#
#
#
#
class Widget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        global text
        text = QTextEdit()

        # second editor in which the error messeges and succeeded connections will be shown
        self.text2 = QTextEdit()
        self.text2.setReadOnly(True)
        # defining a Treeview variable to use it in showing the directory included files
        self.treeview = QTreeView()

        # making a variable (path) and setting it to the root path (surely we can set it to whatever the root we want, not the default)
        path = QDir.rootPath()

        # making a Filesystem variable, setting its root path and applying somefilters we need on it
        self.dirModel = QFileSystemModel()
        self.dirModel.setRootPath(QDir.rootPath())

        # NoDotAndDotDot => Do not list the special entries "." and "..".
        # AllDirs =>List all directories; i.e. don't apply the filters to directory names.
        # Files => List files.
        self.dirModel.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs | QDir.Files)
        self.treeview.setModel(self.dirModel)
        self.treeview.setRootIndex(self.dirModel.index(path))

        vbox = QVBoxLayout()
        Left_hbox = QHBoxLayout()
        Right_hbox = QHBoxLayout()

        # after defining variables of type QVBox and QHBox
        # I will Assign treevies variable to the left one and the first text editor in which the code will be written to the right one
        Left_hbox.addWidget(self.treeview)
        Right_hbox.addWidget(text)

        # defining another variable of type Qwidget to set its layout as an QHBoxLayout
        # we will do the same with the right one
        Left_hbox_Layout = QWidget()
        Left_hbox_Layout.setLayout(Left_hbox)

        Right_hbox_Layout = QWidget()
        Right_hbox_Layout.setLayout(Right_hbox)

        # I defined a splitter to seperate the two variables (left, right) and make it more easily to change the space between them
        H_splitter = QSplitter(Qt.Horizontal)
        H_splitter.addWidget(Left_hbox_Layout)
        H_splitter.addWidget(Right_hbox_Layout)
        H_splitter.setStretchFactor(1, 1)

        # we defined a new splitter to seperate between the upper and lower sides of the window
        V_splitter = QSplitter(Qt.Vertical)
        V_splitter.addWidget(H_splitter)
        V_splitter.addWidget(self.text2)

        Final_Layout = QHBoxLayout(self)
        Final_Layout.addWidget(V_splitter)

        self.setLayout(Final_Layout)

    # defining a new Slot (takes string) to save the text inside the first text editor
    @pyqtSlot(str)
    def Saving(s):
        with open('somefile.txt', 'w') as f:
            TEXT = text.toPlainText()
            f.write(TEXT)

#
#
############ end of Class ############
#
#

# defining a new Slot (takes string)
# Actually I could connect the (mainwindow) class directly to the (widget class) but I've made this function in between for futuer use
# All what it do is to take the (input string) and establish a connection with the widget class, send the string to it
@pyqtSlot(str)
def reading(s):
    b = Signal()
    b.reading.connect(Widget.Saving)
    b.reading.emit(s)


#
#
#
#
############ MainWindow Class ############
#
#
#
#
class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.intUI()

    def intUI(self):

        self.b = Signal()

        # connecting (self.b) with reading function
        self.b.reading.connect(reading)

        # creating menu items
        menu = self.menuBar()

        # we have three menu items
        filemenu = menu.addMenu('File')
        Port = menu.addMenu('Port')
        Run = menu.addMenu('Run')

        # Making and adding actions for Port item
        Port_Action = QAction("Port", self)
        Port_Action.triggered.connect(self.Port)
        Port.addAction(Port_Action)

        # Making and adding Run Actions
        RunAction = QAction("Run", self)
        RunAction.triggered.connect(self.Run)
        Run.addAction(RunAction)

        # Making and adding File Features
        Save_Action = QAction("Save", self)
        Save_Action.triggered.connect(self.save)
        Save_Action.setShortcut("Ctrl+S")
        Close_Action = QAction("Close", self)
        Close_Action.setShortcut("Alt+c")
        Close_Action.triggered.connect(self.close)

        filemenu.addAction(Save_Action)
        filemenu.addAction(Close_Action)

        # Seting the window Geometry
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('micropython IDE')

        widget = Widget()

        self.setCentralWidget(widget)
        self.show()

    ###########################        Start OF the Functions          ##################
    def Run(self):
        if self.port_flag == 0:
            self.text2.append("Your code was uploaded successfully.")
        else:
            self.text2.append("Please Select Your Port Number First")

    def Port(self):
        Port_Number, Entered = QInputDialog.getText(self, 'Input Dialog', 'PLease_Enter_Your_Port_Number:')
        self.port_flag = 0

    def save(self):
        self.b.reading.emit("name")


#
#
############ end of Class ############
#
#

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UI()
    # ex = Widget()
    sys.exit(app.exec_())

