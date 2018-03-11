from tkinter import *
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt
import numpy


class AdjacencyMatrixGraph:

    def __init__(self, master):
        # GUI ELEMENTS
        self.adjacency_matrix_entry = Entry(master)
        self.draw_graph_button = Button(master, text="Draw graph", command=self.draw_graph)

        # GRID
        self.adjacency_matrix_entry.grid(row=0, column=1)
        self.draw_graph_button.grid(row=1, column=1)

    def draw_graph(self):
        try:
            adjacency_matrix = numpy.matrix(self.adjacency_matrix_entry.get())
            graph = nx.from_numpy_matrix(adjacency_matrix)
            nx.draw(graph)
            plt.show()
        except Exception as err:
            self.show_error(self, err)


def show_error(self, *args):
    messagebox.showerror('Exception', args[1])
