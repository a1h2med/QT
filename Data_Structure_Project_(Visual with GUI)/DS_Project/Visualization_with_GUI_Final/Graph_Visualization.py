# In this project it's required to Visualize the Graph as an assignment project
# it was required to have a file as an input then calculate the centrality of it and visualize it with clearing the nodes which are highly centralized
# It was added some features on it to make it better
# I added GUI to it which enable the user to choose the method of calculating the centrality(closeness,betweeness,centrality), and choose the file required which has the data in it
# then shows the output of the calculation in a text label in the window and plot the Graph

# author => Ahmed Ashraf

# import matplotlib to be able to draw the graph
# import networkx as a lib important for graph operations
import json                 # its a library used to convert from dict. into string
import sys
import matplotlib.pyplot as plt
import networkx as nx
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QRadioButton , QFileDialog , QTextEdit
from PyQt5.QtCore import Qt

# glabal variables initialized to share its values

Degree = False
Betweeness = []
Closeness = []

class Window(QMainWindow):
    def __init__(self):                 # Class constructor
        super().__init__()
        self.titel = "Centrality Project"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.Init_window()              # Window function which have the parameters required


    def Init_window(self):

        # it's a Button created to open a file and choose it
        self.button = QPushButton("open File",self)
        self.button.setGeometry(100,75,100,50)

        #it's a function used to connect between the action performed on the button and what should happen
        self.button.clicked.connect(self.OpenFileDialog)

        # it's used to show the a text dialog in the window in which I'll show the output of the calculation
        self.textedit = QTextEdit(self)
        self.textedit.setGeometry(75,150,400,300)

        # it's a button created to submit the data received when the button is clicked
        self.Button_Submit = QPushButton("Submit", self)
        self.Button_Submit.move(500, 400)
        self.Button_Submit.clicked.connect(self.GetTheData)

        # here i made radio butttons to choose the type of calculation you want to perform
        RadioButton = QRadioButton("Degree_Centrality ", self)
        RadioButton.move(500, 250)
        RadioButton.toggled.connect(self.RadioButtonChanged)

        RadioButton1 = QRadioButton("Closeness_Centrality ", self)
        RadioButton1.move(500, 300)
        RadioButton1.toggled.connect(self.RadioButtonChanged1)

        RadioButton2 = QRadioButton("Betweeness_Centrality ", self)
        RadioButton2.move(500, 350)
        RadioButton2.toggled.connect(self.RadioButtonChanged2)

        # setting the window parameters
        self.setWindowTitle(self.titel)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()


    # the three upcoming functions was created to connect each button with its special function
    # in each function It will read the state of it and set one of the global variables
    def RadioButtonChanged(self):
        state = self.sender()
        if state.isChecked:
            global Degree
            Degree = True
            global Betweeness
            Betweeness = False
            global Closeness
            Closeness = False



    def RadioButtonChanged1(self):
        state1 = self.sender()
        if state1.isChecked:
            global Degree
            Degree = False
            global Betweeness
            Betweeness = False
            global Closeness
            Closeness = True


    def RadioButtonChanged2(self):
        state2 = self.sender()
        if state2.isChecked:
            global Degree
            Degree = False
            global Betweeness
            Betweeness = True
            global Closeness
            Closeness = False

    # in this function it's connected to (open file) button which when you press it it will call this function
    # here i will read the file which was choosen by the user

    def OpenFileDialog(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', '/home')
        if filename[0]:
            self.GetTheData(open(filename[0], "r"))


    # when the button(submit) is pressed I will check on the global variables to see which
    # algorithm was selected, then perform the calculation and plot the graph required
    # for sure the highly centralized nodes will be cleared in a different colors
    def GetTheData(self,f):
        if Degree == True:
            s = f.readline()  # I made those lines to read the first line in the file to get rid of it and keep reading from the next one
            x1 = s.split(" ")[0]
            x2 = s.split(" ")[1]
            G = nx.Graph()

            for x in f:  # That loop is made to read the nodes and what they are connected to
                First_node = x.split(" ")[0]
                Second_node = x.split(" ")[1]
                G.add_edges_from([(First_node, Second_node)])

            color_map = []

            degree = nx.degree_centrality(G)  # It's a variable made to calculate the degree centrality
            print(degree)
            c = json.dumps(degree)

            Max_value = max(degree.values())  # It's a variable made to calculate the Max value in the algorithm

            for node in G:  # this loop is simply checking on nodes of the graph and checks if it has the Max centrality or not
                if node in degree:
                    value = degree.get(node)
                    if Max_value == value:
                        color_map.append('red')
                    else:
                        color_map.append('blue')

            pos = nx.spring_layout(G)
            nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_color=color_map, node_size=500)
            nx.draw_networkx_labels(G, pos)
            nx.draw_networkx_edges(G, pos, arrows=False)
            plt.show()
            print(degree)
            self.textedit.setText(c)


        elif Betweeness == True:
            s = f.readline()  # I made those lines to read the first line in the file to get rid of it and keep reading from the next one
            x1 = s.split(" ")[0]
            x2 = s.split(" ")[1]
            G = nx.Graph()
            reading = ""

            for x in f:  # That loop is made to read the nodes and what they are connected to
                First_node = x.split(" ")[0]
                Second_node = x.split(" ")[1]
                weight = x.split(" ")[2]
                reading += weight
                G.add_edges_from([(First_node, Second_node)])

            color_map = []

            betweeness = nx.betweenness_centrality(G, int(x1), True, reading)

            c = json.dumps(betweeness)

            Max_value = max(betweeness.values())  # It's a variable made to calculate the Max value in the algorithm

            for node in G:  # this loop is simply checking on nodes of the graph and checks if it has the Max centrality or not
                if node in betweeness:
                    value = betweeness.get(node)
                    if Max_value == value:
                        color_map.append('red')
                    else:
                        color_map.append('blue')

            pos = nx.spring_layout(G)
            nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_color=color_map, node_size=500)
            nx.draw_networkx_labels(G, pos)
            nx.draw_networkx_edges(G, pos, arrows=False)
            plt.show()
            self.textedit.setText(c)


        elif Closeness == True:
            s = f.readline()  # I made those lines to read the first line in the file to get rid of it and keep reading from the next one
            x1 = s.split(" ")[0]
            x2 = s.split(" ")[1]
            G = nx.Graph()

            for x in f:  # That loop is made to read the nodes and what they are connected to
                First_node = x.split(" ")[0]
                Second_node = x.split(" ")[1]
                G.add_edges_from([(First_node, Second_node)])

            color_map = []

            closeness = nx.closeness_centrality(G)

            c = json.dumps(closeness)

            Max_value = max(closeness.values())  # It's a variable made to calculate the Max value in the algorithm

            for node in G:  # this loop is simply checking on nodes of the graph and checks if it has the Max centrality or not
                if node in closeness:
                    value = closeness.get(node)
                    if Max_value == value:
                        color_map.append('red')
                    else:
                        color_map.append('blue')

            pos = nx.spring_layout(G)
            nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_color=color_map, node_size=500)
            nx.draw_networkx_labels(G, pos)
            nx.draw_networkx_edges(G, pos, arrows=False)
            plt.show()
            self.textedit.setText(c)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())


