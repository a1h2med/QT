# import matplotlib to be able to draw the graph
# import networkx as a lib important for graph operations

import json
import sys
import matplotlib.pyplot as plt
import networkx as nx
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton, QRadioButton , QFileDialog , QTextEdit
from PyQt5.QtCore import Qt

Degree = False
Betweeness = []
Closeness = []
read = []


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.titel = "Centrality Project"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.Init_window()


    def Init_window(self):
        self.button = QPushButton("open File",self)
        self.button.setGeometry(100,75,100,50)
        self.button.clicked.connect(self.OpenFileDialog)

        self.textedit = QTextEdit(self)
        self.textedit.setGeometry(75,150,400,300)

        button = QPushButton("Submit", self)
        button.move(500, 400)

        RadioButton = QRadioButton("Degree_Centrality ", self)
        RadioButton.move(500, 250)
        RadioButton.toggled.connect(self.RadioButtonChanged)

        RadioButton1 = QRadioButton("Closeness_Centrality ", self)
        RadioButton1.move(500, 300)
        RadioButton1.toggled.connect(self.RadioButtonChanged1)

        RadioButton2 = QRadioButton("Betweeness_Centrality ", self)
        RadioButton2.move(500, 350)
        RadioButton2.toggled.connect(self.RadioButtonChanged2)

        self.setWindowTitle(self.titel)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()


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

    def OpenFileDialog(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', '/home')
        if filename[0]:
            f = open(filename[0], "r")


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

                for x in f:  # That loop is made to read the nodes and what they are connected to
                    First_node = x.split(" ")[0]
                    Second_node = x.split(" ")[1]
                    G.add_edges_from([(First_node, Second_node)])

                color_map = []

                betweeness = nx.betweenness_centrality(G)

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


