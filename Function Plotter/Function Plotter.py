# ToDo add documentation.
# ToDo increase font size.
# ToDo support ^.
import numpy as np
from PySide2.QtWidgets import *
from PySide2 import QtWidgets, QtCore
from matplotlib.backends.backend_qt5agg import (
    NavigationToolbar2QT as NavigationToolbar)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import sys
from PySide2.QtWidgets import (QTextEdit, QPushButton, QApplication,
                               QVBoxLayout, QDialog, QGridLayout)

user_input_eqn = ''
user_input_min = 0
user_input_max = 0

def symbol_checking(symbol, function):
    if symbol < len(function) - 1:
        return True
    else:
        return False


def Error_Handling(error_code_number):
    switch = {
        1: 'variable error, please enter exactly one variable',
        2: 'unsupported operator, please recheck the function',
        3: 'Expected an operator',
        4: 'Expected a digit or a variable',
        5: 'Expected a variable',
        6: 'Make sure that Min/Max is a valid integer number'
    }
    # ToDo: make it appears in an error dialog
    print(switch.get(error_code_number))


def Lexical_Analyzer(function):
    list_of_operators = []
    list_of_digits = []
    variable = ''
    flag = 0
    for symbol in range(len(function)):
        current_char = function[symbol]
        if current_char == '+' or current_char == '-' or current_char == '*' or current_char == '/':
            list_of_operators.append(current_char)
        elif current_char.isalpha():
            if flag == 0:
                variable = current_char
                flag = 1
            else:
                if current_char == variable:
                    pass
                else:
                    Error_Handling(1)
                    return False
        elif current_char.isdigit():
            list_of_digits.append(int(current_char))
        else:
            Error_Handling(2)
            return False
    if variable == '':
        Error_Handling(5)
        return False
    out = Parser_Analyzer(function, list_of_digits, list_of_operators, variable, 0)
    return out


def Parser_Analyzer(function, list_of_digits, list_of_operators, variable, starting_flag):
    """

    :param function: original input by the user.
    :param list_of_digits: list of digits exists in the user input.
    :param list_of_operators: list of operators exists in the user input.
    :param variable: the variable exists in the function being entered.
    :param starting_flag: this is the flag to handle whether it's the first call or not.
    :return: true if the output was correct, else it will raise an error.

    valid rules:
        1- ([digit]+ ^ [operator]+ ^ [variable* | digit*]+)*
        2- ([variable]+ ^ [operator]+ ^ [variable* | digit*]+)*
        3- [variable]+
    """
    for symbol in range(len(function)):
        current_symbol = function[symbol]
        if current_symbol == variable:
            out = symbol_checking(symbol, function)
            symbol += 1
            if out:
                current_symbol = function[symbol]
                if current_symbol in list_of_operators:
                    out = symbol_checking(symbol, function)
                    symbol += 1
                    if out:
                        current_symbol = function[symbol]
                        if current_symbol == variable:
                            if symbol == len(function) - 1:
                                return True
                            else:
                                function = function[symbol + 1:]
                                output = Parser_Analyzer(function, list_of_digits, list_of_operators, variable, 1)
                                return output
                        elif ord(current_symbol[0]) - 48 in range(0, 9):
                            if int(current_symbol) in list_of_digits:
                                if symbol == len(function) - 1:
                                    return True
                                else:
                                    function = function[symbol + 1:]
                                    output = Parser_Analyzer(function, list_of_digits, list_of_operators, variable, 1)
                                    return output
                        else:
                            Error_Handling(4)
                            return False
                    else:
                        Error_Handling(4)
                        return out
                else:
                    Error_Handling(3)
                    return False
            else:
                Error_Handling(3)
                return out
        elif starting_flag != 0:
            if current_symbol in list_of_operators:
                out = symbol_checking(symbol, function)
                symbol += 1
                if out:
                    current_symbol = function[symbol]
                    if current_symbol == variable:
                        if symbol == len(function) - 1:
                            return True
                        else:
                            function = function[symbol + 1:]
                            output = Parser_Analyzer(function, list_of_digits, list_of_operators, variable, 1)
                            return output
                    elif ord(current_symbol[0]) - 48 in range(0, 9):
                        if int(current_symbol) in list_of_digits:
                            if symbol == len(function) - 1:
                                return True
                            else:
                                function = function[symbol + 1:]
                                output = Parser_Analyzer(function, list_of_digits, list_of_operators, variable, 1)
                                return output
                    else:
                        Error_Handling(4)
                        return False
                else:
                    if current_symbol == variable:
                        function = function[symbol + 1:]
                        return True
                    elif ord(current_symbol[0]) - 48 in range(0, 9):
                        if ord(current_symbol[0]) - 48 in range(0, 9):
                            if int(current_symbol) in list_of_digits:
                                function = function[symbol + 1:]
                                return True
                    else:
                        Error_Handling(4)
                        return out
            else:
                return True
        elif ord(current_symbol[0]) - 48 in range(0, 9):
            if int(current_symbol) in list_of_digits:
                out = symbol_checking(symbol, function)
                symbol += 1
                if out:
                    current_symbol = function[symbol]
                    if current_symbol in list_of_operators:
                        out = symbol_checking(symbol, function)
                        symbol += 1
                        if out:
                            current_symbol = function[symbol]
                            if current_symbol == variable:
                                if symbol == len(function) - 1:
                                    return True
                                else:
                                    function = function[symbol + 1:]
                                    output = Parser_Analyzer(function, list_of_digits, list_of_operators, variable, 1)
                                    return output
                            elif ord(current_symbol[0]) - 48 in range(0, 9):
                                if int(current_symbol) in list_of_digits:
                                    if symbol == len(function) - 1:
                                        return True
                                    else:
                                        function = function[symbol + 1:]
                                        output = Parser_Analyzer(function, list_of_digits, list_of_operators, variable,
                                                                 1)
                                        return output
                            else:
                                Error_Handling(4)
                                return False
                        else:
                            Error_Handling(4)
                            return out
                    else:
                        Error_Handling(3)
                        return False
                else:
                    Error_Handling(3)
                    return out
        else:
            Error_Handling(4)
            return False
    if len(function) == 0:
        return True


def Input_Checker(function, minimum_value, maximum_value):
    out = Lexical_Analyzer(function)
    input_min = MinMaxChecking(minimum_value)
    input_max = MinMaxChecking(maximum_value)
    return out, input_min, input_max

def MinMaxChecking(input_string):
    for i in range(len(input_string)):
        if ord(input_string[i]) - 48 in range(0, 9):
            continue
        else:
            Error_Handling(6)
    return int(input_string)

class FunctionPlotter(QDialog):

    def __init__(self, parent=None):
        super(FunctionPlotter, self).__init__(parent)
        self.mainwindow()

    # Greets the user
    def mainwindow(self):

        self.setWindowTitle("Function Plotter")
        grid = QGridLayout()
        self.setLayout(grid)

        eqn_title = QLabel("Please Insert Your Equation Here")
        min_title = QLabel("Please Insert Min Value")
        max_title = QLabel("Please Insert Max Value")

        eqn_title.setAlignment(QtCore.Qt.AlignHCenter)
        min_title.setAlignment(QtCore.Qt.AlignHCenter)
        max_title.setAlignment(QtCore.Qt.AlignHCenter)

        self.eqn_text_edit = QTextEdit()
        self.min_text_edit = QTextEdit()
        self.max_text_edit = QTextEdit()

        submit = QtWidgets.QPushButton("submit", self)

        grid.setSpacing(10)
        grid.addWidget(eqn_title, 0, 0, 1, 1)
        grid.addWidget(self.eqn_text_edit, 1, 0, 1, 1)
        grid.addWidget(min_title, 0, 1, 1, 1)
        grid.addWidget(self.min_text_edit, 1, 1, 1, 1)
        grid.addWidget(max_title, 0, 2, 1, 1)
        grid.addWidget(self.max_text_edit, 1, 2, 1, 1)
        grid.addWidget(submit, 2, 0, 1, 1)

        submit.clicked.connect(self.connector)
        self.show()

    def connector(self):
        global user_input_eqn
        global user_input_min
        global user_input_max
        user_input_eqn = self.eqn_text_edit.toPlainText()
        user_input_min = self.min_text_edit.toPlainText()
        user_input_max = self.max_text_edit.toPlainText()

        out, user_input_min, user_input_max = Input_Checker(user_input_eqn, user_input_min, user_input_max)
        if out:
            self.w = Window()
            self.w.show()
            self.hide()
        else:
            print(2)

class Window(QDialog):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        self.setWindowTitle('Plot')
        self.plot()

    def plot(self):
        global user_input_eqn
        global user_input_min
        global user_input_max
        self.figure.clear()
        x = np.array(range(user_input_min, user_input_max))
        y = eval(user_input_eqn)
        ax = self.figure.add_subplot(111)
        ax.plot(x, y, '*-')
        self.canvas.draw()


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    Plotter = FunctionPlotter()
#    Plotter.show()
    # Run the main Qt loop
    sys.exit(app.exec_())
