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
    
    # initializing a Signal 
    sending = pyqtSignal()

    # initializing a Signal which will take (string) as an input
    reading = pyqtSignal(str)
    
    # init Function for the Signal class
    def __init__(self):
        # Initialize the PunchingBag as a QObject
        QObject.__init__(self)
    
    # defining a function to emit the signal 
    def punch(self):
        self.sending.emit()

#
#
############ end of Class ############
#
#

########## defining a Slot which takes (string) ##########
@pyqtSlot(str)
def reading(s):
    print(s)

# here I wanted to connect it with another Slot exists in a Widget Class
    b = Signal()
    b.reading.connect(Widget.save)
    b.reading.emit(s)


########## defining a Slot which just print(1) (I made it for testing ##########
@pyqtSlot()
def nn():
    print(1)

#
#
#
#
############ MainWindow Class in which Main window Parameters will be defined ############
#
#
#
#
class UI(QMainWindow):
    
    # init Function
    def __init__(self):
        super().__init__()
        self.intUI()

    def intUI(self):
        
        # setting the Geometry of the window and its title
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('micropython IDE')
        
        # defining a Push button and connecting it with save function
        self.btn = QPushButton("name", self)
        self.btn.clicked.connect(self.save)
        
        # defining a variable of type class(Signal)
        self.b = Signal()

        # defining a variable of type class(Widget) (if we want)
        A = Widget()
        
        # connecting the Signal reading with the function reading which we've written previously
        self.b.reading.connect(reading)
        self.show()


#    def Init(s):
#        print(s)
    
    # on pushing the button, this function will be executed
    # we will emit a string to our slot (reading Function defined previously)
    def save(self):
        self.b.reading.emit("name")
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UI()
#    ex = Widget()
    #    ex = Try()
    sys.exit(app.exec_())
