from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit ,QAction,  QWidget , QInputDialog, QGridLayout
import sys

#
#
#
#
###############   Main Class   ################
#
#
#
#

class UI(QMainWindow):

    #
    #
    #
    ###############   Init Function   ################
    #
    #
    #
    def __init__(self):
        super().__init__()
        self.intUI()


    def intUI(self):
        self.port_flag = 1

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


#        Syntax = menu.addMenu('Syntax_Check')
#        Syntax_Action = QAction("Check", self)
#        Syntax_Action.triggered.connect(self.Check)
#        Syntax.addAction(Syntax_Action)


        # Making and adding File Features
        Save_Action = QAction("Save", self)
        Save_Action.triggered.connect(self.save)
        Save_Action.setShortcut("Ctrl+S")
        Close_Action = QAction("Close", self)
        Close_Action.setShortcut("Alt+c")
        Close_Action.triggered.connect(self.close)

        filemenu.addAction(Save_Action)
        filemenu.addAction(Close_Action)

        ################           Grid Layout           ################
        
        # First text editor in which the code will be written
        self.text = QTextEdit()
        
        # second editor in which the error messeges and succeeded connections will be shown
        self.text2 = QTextEdit()
        
        grid = QGridLayout()
        
        # setting the space between the two text editors
        grid.setSpacing(10)

        # setting a fixed hight for the second text editor so when the window is maximized it won't take half of the screen
        self.text2.setFixedHeight(70)
        
        # making it read only so the user can't insert anything in it(Although whether he put anything or not it won't make any difference)
        self.text2.setReadOnly(True)
        
        # setting the position for the two text editors
        grid.addWidget(self.text, 1, 0)
        grid.addWidget(self.text2, 2, 0)
        
        # Seting the window Geometry
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('micropython IDE')
        widget = QWidget()
        
        # setting layout widget and making it central widget for Qmainwindow
        widget.setLayout(grid)
        self.setCentralWidget(widget)

        self.show()
        ################      end of code           ########################





    ###########################        Start OF the Functions          ##################
    def Run(self):
        if self.port_flag == 0:
            self.text2.append("Your code was uploaded successfully.")
        else:
            self.text2.append("Please Select Your Port Number First.")

#   def Check(self):
#       print(1)

    
    # Making an input dialog to enter the number of its port on which the microcontroller is connected to
    def Port(self):
        Port_Number, Entered = QInputDialog.getText(self, 'Input Dialog', 'PLease_Enter_Your_Port_Number:')
        self.port_flag = 0
    
    # Saving the Code
    def save(self):
        with open('somefile.txt', 'w') as f:
            mytext = self.text.toPlainText()
            f.write(mytext)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UI()
    sys.exit(app.exec_())

