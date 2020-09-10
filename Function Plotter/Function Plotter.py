"""
    This project intends to plot any function user enters.
    this project is separated into multiple parts, the first two parts behaves as a compiler,
    it  1- checks the syntax provided by the user, saves it,
        2- checks the grammar provided.
    third part is GUI which consists of:
        1- labels           2- text editor           3- button
        4- plot
    fourth and final part is the part where it calculates the function and plot it.

    features:
        1- checks syntax entered by the user.
        2- displays error messages if any.
        3- takes min, max range for the function.
        4- checks on the input range.
        5- supports negative range.  
        6- plot entered equation using matplotlib, which is embedded in PySide2 GUI.
        7- simple design.

    limitations:
        1- it can draw equations which has only one variable.
        2- as this application is still under development, so it supports only (+, -, *, ^, /), for now.
        3- it can't handle (,{,[, which will be considered during future thoughts.

"""
# call required libraries
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

# global variables made to save entered equation, min, max values, and error message.
user_input_eqn = ''
user_input_min = 0
user_input_max = 0
errorMessage = ''
var = ''
# this function is made to check whether I've nearly reached the end of the equation or not.
def symbol_checking(symbol, function):
    """

    :param symbol: current index number of a certain equation
    :param function: passed equation
    :return: true when the index number less than length of equation by one, else it will return false
    """
    if symbol < len(function) - 1:
        return True
    else:
        return False


# A function to hold all types of errors I got.
def Error_Handling(error_code_number):
    """

    :param error_code_number: error code.
    :return: corresponding error message.
    """
    global errorMessage
    switch = {
        1: 'variable error, please enter exactly one variable',
        2: 'unsupported operator, please recheck the function',
        3: 'Expected an operator',
        4: 'Expected a digit or a variable',
        5: 'Expected a variable',
        6: 'Make sure that Min/Max is a valid integer number',
        7: 'Please recheck Max/Min values',
        8: 'Expected to end with a variable or a digit'
    }
    errorMessage = switch.get(error_code_number)

# this function mainly gets all the digit, as I'm looping char by char,
# so if there's an integer it will be parsed like: 1,0,0
# while 100 is a number, so I've to get the whole integer.
def getDigit(function, current_char, symbol):
    temp = ''
    while current_char.isdigit():
        temp += current_char
        if symbol < len(function) - 1:
            symbol += 1
        else:
            symbol += 1
            break
        current_char = function[symbol]
    return int(temp), symbol

# checking syntax of the equation provided by the user.
# here I'll check on certain things,
# 1- operators entered      2- variables        3- integers.
def Lexical_Analyzer(function):
    """

    :param function: equation entered by the user.
    :return: false, whenever there's an error, else it will call parser, passing operators found,
    digits, and variables, then returns whatever it returns.
    """
    global var
    list_of_operators = []
    list_of_digits = []
    variable = ''
    # this flag is made to check on whether I already have a variable stored or not.
    flag = 0
    # what I'm doing here is very simple
    # 1- loop over the string
    # 2- get current char and check on it to know what it is.
    # 3- if not found raise an error, else store it.
    symbol = 0
    while symbol in range(len(function)):
        current_char = function[symbol]
        if current_char == '+' or current_char == '-' or current_char == '*' or current_char == '/' \
                or current_char == '^':
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
            temp, symbol = getDigit(function, current_char, symbol)
            list_of_digits.append(int(temp))
            continue
        else:
            Error_Handling(2)
            return False
        symbol += 1
    if variable == '':
        Error_Handling(5)
        return False
    # if there was no error call parser, and return whatever it returns.
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

        # get the current char, and check on it, whether it's a variable or integer, if nothing raise an error.
        # it's clearly that it's the same steps, but I've made to steps before performing recursion (explained down)
        # as I've seen that it was the best thing to separate the equation into three parts, if I have an equation
        # like: x+2+3+4, then it was easier to cut it like x+2, then pass whatever comes again to the function
        # which should be an operator followed by an equation or a digit, like in the above example, which
        # in my case will be: +3, +4.
        current_symbol = function[symbol]
        if current_symbol == variable:
            # if it's a variable, check on the string provided, then raise the current symbol to get
            # the next char.
            out = symbol_checking(symbol, function)
            symbol += 1
            # if symbol is not at its end, then proceed
            if out:
                # get the current char, and check whether it's in the list of operators
                # provided by the lexical analyzer or not, if not check on the digits list
                # if not raise an error.
                current_symbol = function[symbol]
                if current_symbol in list_of_operators:
                    out = symbol_checking(symbol, function)
                    symbol += 1
                    if out:
                        # get the current char, check whether it's a variable or digit or raise an error.
                        # check on the length, if it's the last, return true,
                        # else call the parser again, passing to it the new function,
                        # list of digits, operators, variable, and flag which indicates whether it's the
                        # first call or not, as it's not so I need it to get into the (operator part).
                        current_symbol = function[symbol]
                        if current_symbol == variable:
                            if symbol == len(function) - 1:
                                return True
                            else:

                                # pass unchecked part of the equation.
                                function = function[symbol + 1:]
                                output = Parser_Analyzer(function, list_of_digits, list_of_operators, variable, 1)
                                return output
                        elif ord(current_symbol[0]) - 48 in range(0, 9):
                            # get the whole digit.
                            temp, symbol = getDigit(function, current_symbol, symbol)
                            # decrease the symbol value by 1, to get the previous char, and proceed.
                            # in case you have (1) so entered symbol is x, out is x+2, so I need to decrease it,
                            # I can't decrease it in the function itself as I need it somewhere else
                            symbol -= 1
                            if temp in list_of_digits:
                                if symbol == len(function) - 1:
                                    return True
                                else:
                                    function = function[symbol + 1:]
                                    output = Parser_Analyzer(function, list_of_digits, list_of_operators, variable, 1)
                                    return output
                        else:
                            # if it's not a variable or a digit raise an error
                            Error_Handling(4)
                            return False
                    else:
                        Error_Handling(4)
                        return out
                else:
                    # if it's not an operator raise an error, as variable should has operator after it.
                    Error_Handling(3)
                    return False
            else:
                return True
            # operator part
        elif starting_flag != 0:
            # check on symbol.
            # check on length.
            # get next char.
            # check on its type.
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
                        temp, symbol = getDigit(function, current_symbol, symbol)
                        symbol -= 1
                        if temp in list_of_digits:
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
                            temp, symbol = getDigit(function, current_symbol, symbol)
                            symbol -= 1
                            if temp in list_of_digits:
                                function = function[symbol + 1:]
                                return True
                    else:
                        Error_Handling(4)
                        return out
            else:
                return True

            # digit part, same as variable part
        elif ord(current_symbol[0]) - 48 in range(0, 9):
            temp, symbol = getDigit(function, current_symbol, symbol)
            symbol -= 1
            if temp in list_of_digits:
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
                                temp, symbol = getDigit(function, current_symbol, symbol)
                                symbol -= 1
                                if temp in list_of_digits:
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

# check on min max values provided by the user.
def MinMaxChecking(input_string):
    """

    :param input_string: min/max value
    :return: int value of min/max, or empty string
    """

    """
        1- it will loop on provided string.
        2- checks on the ASCII code of each char of it
        3- raise an error if there were any, else check if it's a (-) sign or not else return int of string 
    """
    flag = 1
    for i in range(len(input_string)):
        if ord(input_string[i]) - 48 in range(0, 9):
            continue
        elif (i == 0) and (input_string[i] == '-'):
            continue
        else:
            flag = 0
            Error_Handling(6)
    if flag:
        return int(input_string)
    else:
        return ''

# checks on the inputs provided by the user.
def Input_Checker(function, minimum_value, maximum_value):
    """

    :param function: input equation
    :param minimum_value: input min
    :param maximum_value: input max
    :return: out => output of compiler, which is true if the equation syntax and grammar was correct,
     else otherwise.
     input_min => checked min value integer.
     input_max => checked max value integer.
    """
    out = Lexical_Analyzer(function)
    input_min = MinMaxChecking(minimum_value)
    input_max = MinMaxChecking(maximum_value)
    return out, input_min, input_max

# this class which holds main GUI.
# it's consists of multiple widgets lays in grid layout which puts them just as needed.
class FunctionPlotter(QDialog):

    def __init__(self, parent=None):
        super(FunctionPlotter, self).__init__(parent)
        self.mainwindow()

    # main window GUI
    def mainwindow(self):

        # setting window title, and setting layout of GUI to be in shape of grid.
        self.setWindowTitle("Function Plotter")
        grid = QGridLayout()
        self.setLayout(grid)

        # made three labels to let the user know which goes where.
        eqn_title = QLabel("Please Insert Your Equation Here")
        min_title = QLabel("Please Insert Min Value")
        max_title = QLabel("Please Insert Max Value")

        eqn_title.setAlignment(QtCore.Qt.AlignHCenter)
        min_title.setAlignment(QtCore.Qt.AlignHCenter)
        max_title.setAlignment(QtCore.Qt.AlignHCenter)

        # three text editors, and I've set font size to 20, to make it clearer.
        self.eqn_text_edit = QTextEdit()
        self.min_text_edit = QTextEdit()
        self.max_text_edit = QTextEdit()

        self.eqn_text_edit.setFontPointSize(20)
        self.min_text_edit.setFontPointSize(20)
        self.max_text_edit.setFontPointSize(20)

        # push button made to let the user submit his/her inputs.
        submit = QtWidgets.QPushButton("submit", self)

        # adding previous widgets to grid, where everything should goes just where I need it.
        grid.setSpacing(10)
        grid.addWidget(eqn_title, 0, 0, 1, 1)
        grid.addWidget(self.eqn_text_edit, 1, 0, 1, 1)
        grid.addWidget(min_title, 0, 1, 1, 1)
        grid.addWidget(self.min_text_edit, 1, 1, 1, 1)
        grid.addWidget(max_title, 0, 2, 1, 1)
        grid.addWidget(self.max_text_edit, 1, 2, 1, 1)
        grid.addWidget(submit, 2, 0, 1, 1)

        # on clicking the button, call this function.
        submit.clicked.connect(self.connector)
        self.show()

    def connector(self):
        # save all the entered text, pass them to input checker to check on the values, get new values.
        global user_input_eqn
        global user_input_min
        global user_input_max
        user_input_eqn = self.eqn_text_edit.toPlainText()
        user_input_min = self.min_text_edit.toPlainText()
        user_input_max = self.max_text_edit.toPlainText()

        out, user_input_min, user_input_max = Input_Checker(user_input_eqn, user_input_min, user_input_max)

        # check on the outputs of input checker, if there's anything wrong, just display an error message.
        # if nothing wrong, call other class, where the calculation lays in.
        if out and (user_input_min != '') and (user_input_max != '') and (user_input_max > user_input_min):
            self.w = Window()
            self.w.show()
            self.hide()
        else:
            global errorMessage
            if (user_input_min != '') and (user_input_max != ''):
                if user_input_max <= user_input_min:
                    Error_Handling(7)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText(errorMessage)
            msg.setWindowTitle("Error")
            msg.exec_()
            msg.hide()

class Window(QDialog):

    # making a plot.
    # first, I've made a figure, then called Figure canvas, passed this figure to it.
    # then made navigation tool bar, passed created canvas to it.
    # added all of that to the layout, which is Vbox.
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
        global var
        self.figure.clear()

        # before plotting, replace every ^ with **, to server the correct function.
        user_input_eqn = user_input_eqn.replace("^", "**")
#        eqn.replace("xx", "x")
        x = np.array(range(user_input_min, user_input_max))
        y = eval(user_input_eqn)
        ax = self.figure.add_subplot(111)
        ax.plot(x, y, '*-')
        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Plotter = FunctionPlotter()
    sys.exit(app.exec_())
