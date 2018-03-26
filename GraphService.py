import networkx as nx
import matplotlib.pyplot as plt
from tkinter import *


class GraphService:
    def __init__(self, data=None):
        self.graph = nx.Graph(data)

    def add_node(self, n, weight=None):
        self.graph.add_node(n, weight=weight)

    def add_edge(self, u, v, weight=None):
        self.graph.add_edge(u, v, weight=weight)

    def draw_graph(self, nodes_listbox=None, edges_listbox=None):
        if nodes_listbox and edges_listbox:
            nodes_listbox.delete(0, END)
            edges_listbox.delete(0, END)
            for node in self.get_nodes():
                nodes_listbox.insert(END, node)
            for edge in self.get_edges():
                edges_listbox.insert(END, edge)
        nx.draw(self.graph, with_labels=True)
        plt.show()

    def draw_graph_from_adjacency_matrix(self, adjacency_matrix):
        self.graph = nx.from_numpy_matrix(adjacency_matrix)
        self.draw_graph()

    def draw_graph_from_adjacency_list(self, adjacency_list, nodes_listbox, edges_listbox):
        self.graph = nx.parse_adjlist(adjacency_list, nodetype=int)
        self.draw_graph(nodes_listbox, edges_listbox)

    def get_nodes(self):
        return self.graph.nodes(data='weight', default='')

    def get_edges(self):
        return self.graph.edges(data='label', default='')

    def remove_graph(self):
        self.graph = nx.Graph()
