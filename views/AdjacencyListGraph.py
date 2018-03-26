from tkinter import *
from tkinter import messagebox
import numpy

from GraphService import GraphService


class AdjacencyListGraph:

    def __init__(self, master):
        self.graph_service = GraphService()

        # GUI ELEMENTS
        self.adjacency_list_entry = Entry(master)
        self.draw_graph_button = Button(master, text="Draw graph", command=self.draw_graph)

        # GRID
        self.adjacency_list_entry.grid(row=0, column=1)
        self.draw_graph_button.grid(row=1, column=1)

    def draw_graph(self):
        adjacency_list = self.adjacency_list_entry.get().split(";")
        self.graph_service.draw_graph_from_adjacency_list(adjacency_list)
