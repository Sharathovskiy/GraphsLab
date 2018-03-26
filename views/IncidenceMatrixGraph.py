from tkinter import *
from tkinter import messagebox
import numpy

from GraphService import GraphService


class IncidenceMatrixGraph:

    def __init__(self, master):
        self.graph_service = GraphService()

        # GUI ELEMENTS
        self.incidence_matrix_entry = Entry(master)
        self.draw_graph_button = Button(master, text="Draw graph", command=self.draw_graph)

        # GRID
        self.incidence_matrix_entry.grid(row=0, column=1)
        self.draw_graph_button.grid(row=1, column=1)

    def draw_graph(self):
        try:
            incidence_matrix = numpy.matrix(self.incidence_matrix_entry.get())
            # convert incidence matrix to adjacency matrix
            adjacency_matrix = (numpy.dot(incidence_matrix, incidence_matrix.T) > 0).astype(int)
            self.graph_service.draw_graph_from_adjacency_matrix(adjacency_matrix)
        except Exception as err:
            messagebox.showerror('Exception', err)
