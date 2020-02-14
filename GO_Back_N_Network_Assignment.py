import sys
import sender2
import server2
from PyQt5.QtWidgets import QMainWindow,QPushButton, QApplication , QDialog , QLabel , QInputDialog , QTextEdit
from PyQt5.QtCore import QSize, Qt, QLine, QPoint
from PyQt5.QtGui import QPainter, QPen
from PyQt5 import QtCore
from PyQt5 import QtGui
import _thread
from threading import Thread
import socket
import time
from random import randrange

flag = 0

    #######      GUI Class       ########

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "GO_BACK_N_PROTOCOL"
        self.top = 600
        self.left = 700
        self.width = 700
        self.hight = 600

        self.InitWindow()


    #######       Initialization Window       ######

    def InitWindow(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.hight)

        self.button = QPushButton('Next', self)
        self.button.setFont(QtGui.QFont("Sanserif", 15))
        self.button.clicked.connect(self.Second_Window)
        self.button.resize(70, 40)
        self.button.move(600, 520)

        label = QLabel(self)
        label.setText("WELCOME!!")

        label2 = QLabel(self)
        label2.setText("Go_Back_N_ Protocol_Explanation")

        label3 = QLabel(self)
        label3.setText("Go-Back-N ARQ is a specific instance of the automatic repeat request (ARQ) protocol, \n in which the sending process continues to send a number of frames specified by a window \n size even without receiving an acknowledgement (ACK) packet from the receiver. \n It is a special case of the general sliding window protocol with the transmit window size of N \n and receive window size of 1. It can transmit N frames to the peer before requiring an ACK. \nThe receiver process keeps track of the sequence number of the next frame it expects \n to receive, and sends that number with every ACK it sends. The receiver will discard \n any frame that does not have the exact sequence number it expects (either a duplicate \n frame it already acknowledged, or an out-of-order frame it expects to receive later) and \n will resend an ACK for the last correct in-order frame.Once the sender has sent \n all of the frames in its window, it will detect that all of the frames since the first lost frame \nare outstanding, and will go back to the sequence number of the last ACK it received from \nthe receiver process and fill its window starting with that frame and continue the process over\n again.Go-Back-N ARQ is a more efficient use of a connection than Stop-and-wait ARQ,\n since unlike waiting for an acknowledgement for each packet, the connection is still being \nutilized as packets are being sent. In other words, during the time that would otherwise \nbe spent waiting, more packets are being sent. However, this method also results in sending \n frames multiple times – if any frame was lost or damaged, or the ACK acknowledging them\n was lost or damaged, then that frame and all following frames in the window \n (even if they were received without error) will be re-sent.\n To avoid this, Selective Repeat ARQ can be used.")

        label.setFont(QtGui.QFont("Sanserif", 20))
        label.adjustSize()

        label2.setFont(QtGui.QFont("Sanserif", 15))
        label2.adjustSize()
        label2.move(0, 40)

        label3.setFont(QtGui.QFont("Sanserif", 13))
        label3.adjustSize()
        label3.move(0, 80)
        self.show()


    def Second_Window(self):
        mydialog = QDialog(self)
        mydialog.setWindowTitle(self.title)
        mydialog.setGeometry(self.top,self.left,800,self.hight+60)
#        mydialog.show()

        self.hide()

        No_OF_FRAMES,Entered = QInputDialog.getText(mydialog, 'Input Dialog', 'PLease_Enter_Number_Of_Frames:')
        mydialog.text_edit = QTextEdit(mydialog)
        mydialog.text_edit.setGeometry(self.top-100,self.left-50, 800-500,self.hight-150)
        mydialog.text_edit.move(50,100)
        #self.text_edit.setText(x)

        mydialog.text_edit1 = QTextEdit(mydialog)
        mydialog.text_edit1.setGeometry(self.top - 100, self.left - 50, 800 - 500, self.hight - 150)
        mydialog.text_edit1.move(430, 100)

        mydialog.label7 = QLabel(mydialog)
        mydialog.label7.setText("Sender")

        mydialog.label8 = QLabel(mydialog)
        mydialog.label8.setText("Server")

        mydialog.label7.setFont(QtGui.QFont("Sanserif", 20))
        mydialog.label7.adjustSize()

        mydialog.label8.setFont(QtGui.QFont("Sanserif", 20))
        mydialog.label8.adjustSize()

        mydialog.label7.move(110,40)
        mydialog.label8.move(490,40)

        mydialog.button = QPushButton('Quit', mydialog)
        mydialog.button.setFont(QtGui.QFont("Sanserif", 15))
        mydialog.button.clicked.connect(mydialog.close)
        mydialog.button.resize(70, 40)
        mydialog.button.move(600, 600)


        mydialog.button2 = QPushButton('Transmit_Again', mydialog)
        mydialog.button2.setFont(QtGui.QFont("Sanserif", 15))
        mydialog.button2.clicked.connect(self.Second_Window)

        mydialog.button2.resize(180, 40)
        mydialog.button2.move(280, 600)


        mydialog.show()
        if Entered:
            print(int(No_OF_FRAMES))
            Sender_Output, Server_Output = self.Protocol_Implementation(int(No_OF_FRAMES))

            for i in range(len(Sender_Output)):
                mydialog.text_edit.append(Sender_Output[i])

            for i in range(len(Server_Output)):
                mydialog.text_edit1.append(Server_Output[i])


        mydialog.update()
        #mydialog.hide()


    #######    Protocol Calling Function      ########

    def Protocol_Implementation(self,No_OF_FRAMES):
        thread_1 = [None]
        result_1 = [None]

        thread_2 = [None]
        result_2 = [None]

        thread_1 = Thread(target=server2.mainfunc, args=(No_OF_FRAMES, result_1, 0))
        thread_1.start()

        thread_2 = Thread(target=sender2.main, args=(No_OF_FRAMES, result_2, 0))
        thread_2.start()

        thread_1.join()
        thread_2.join()

        #print(" ".join(result_1))
        return (" ".join(result_2)), (" ".join(result_1))


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())