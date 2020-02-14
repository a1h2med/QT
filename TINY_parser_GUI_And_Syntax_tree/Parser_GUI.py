import PyQt5
from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit ,QAction,  QWidget , QVBoxLayout, QInputDialog, QGridLayout, QFileDialog, QMessageBox
from PyQt5 import uic
import sys
import Tree
import yarab
from os import stat
class UI(QMainWindow):
    portNo = ""
    def __init__(self):
        super().__init__()
        self.intUI()

    def intUI(self):
        menu = self.menuBar()
        filemenu = menu.addMenu('File')
        Run = menu.addMenu('Run')
        Close_Action = QAction("Close", self)
        Close_Action.triggered.connect(self.close)

        Open_Action = QAction("Open", self)
        Open_Action.triggered.connect(self.Open)

        RunAction = QAction("Run", self)
        RunAction.triggered.connect(self.Run)
        Run.addAction(RunAction)

        filemenu.addAction(Close_Action)
        filemenu.addAction(Open_Action)

        ################           Code For AutoSizing           ################
        self.text = QTextEdit()
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.text, 1, 0)

        self.setGeometry(300, 150, 500, 500)
        self.setWindowTitle('Parser GUI')
        widget = QWidget()
        widget.setLayout(grid)
        self.setCentralWidget(widget)

        self.show()
        ################      end of code           ########################


    ###########################        Start OF the Functions          ##################
    def Run(self):
        with open("test.txt", "w") as f:
            mytext = self.text.toPlainText()
            f.write(mytext)
#        f.close()
#        Tree.process()

        self.Read()

    def Read(self):
        # yarab.program()
        # print(yarab.token_type)
        # print(yarab.token_value)
        # print(yarab.error_type)
        # print(yarab.error_type)
        # if yarab.error_type != "":
        #     Tree.process(token_value,token_type)
        # else:
        #     print('error')
        token_value = []
        string_t_value = ''

        token_type = []
        string_t_type = ''
        bool_colon_found = 0
        j = 0
        token_len = 0
        set = stat('test.txt').st_size == 0

        if set != True:
            with open('test.txt') as fp:
                for cnt, line in enumerate(fp):
                    print(line)

                    for i in line:
                        if i == ' ':
                            pass;
                        elif i == ',':
                            bool_colon_found = 1

                        elif bool_colon_found == 0:
                            string_t_value += i
                        elif (bool_colon_found == 1) and (i != '\n'):
                            string_t_type += i
                    token_value.append(string_t_value)
                    token_type.append(string_t_type)
                    token_len = len(token_type)
                    bool_colon_found = 0
                    string_t_value = ''
                    string_t_type = ''
            # print(token_value)
            # print(token_type)
            yarab.token_value = token_value
            yarab.token_type = token_type
            yarab.token_len = token_len
            yarab.program()
            if yarab.error_type == "":
                Tree.process(token_value,token_type)
            else:
                QMessageBox.about(self, "error Messsage", yarab.error_type)
                print(yarab.error_type)
                # //give me the msg box for error_type
        else:
            error_type = "the file is empty"
            QMessageBox.about(self, "error Messsage", error_type)
            print(error_type)
            # error msg here

#        return token_value,token_type

    def Open(self):
        filename = QFileDialog.getOpenFileName(self,'Open File')
        if filename[0]:
            f = open(filename[0], 'r')

            with f:
                data = f.read()
                self.text.setText(data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UI()
    sys.exit(app.exec_())