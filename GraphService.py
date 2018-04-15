from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.widgets import Button

class GraphService:
    def __init__(self, data=None):
        self.graph = nx.Graph(data)

    def add_node(self, n, label=None):
        self.graph.add_node(n, label=label)

    def add_edge(self, u, v, weight=None):
        self.graph.add_edge(u, v, weight=weight)

    def draw_graph(self):
        pos = nx.spring_layout(self.graph)

        nx.draw_networkx_nodes(self.graph, pos=pos, node_size=700)

        nx.draw_networkx_edges(self.graph, pos)
        # if self.are_all_weights_equal():
        #     nx.draw_networkx_edges(self.graph, pos)
        # else: # Draw weights as edge labels and change edge width according to weight
        #     edge_labels = self.get_edge_weights_dict()
        #     split_edges = self.split_edges_by_weights(3, 5)
        #
        #     line_width = 2
        #     for key, value in split_edges.items():
        #         nx.draw_networkx_edges(self.graph, pos, edgelist=value, width=line_width)
        #         line_width += 2
        #     nx.draw_networkx_edge_labels(self.graph, pos=pos, edge_labels=edge_labels)

        nx.draw_networkx_labels(self.graph, pos)

        def euler(event):
            # Jeżeli wszystkie wierzchołki grafu nieskierowanego mają stopień parzysty, to znaczy, że da się skonstruować zamkniętą ścieżkę Eulera nazywaną cyklem Eulera.
            for v,d in self.graph.degree():
                if d % 2 != 0:
                    messagebox.showinfo("Euler", "false")
                    return
                messagebox.showinfo("Euler", "true")
                return



        def hamilton(event):
                print(self.graph[1])

        axEuler = plt.axes([0.0, 0.00, 0.1, 0.075])
        axHamilton = plt.axes([0.2, 0.00, 0.1, 0.075])
        beuler = Button(axEuler, 'Euler')
        beuler.on_clicked(euler)
        bhamilton = Button(axHamilton, 'Hamilton')
        bhamilton.on_clicked(hamilton)

        plt.show()

    def draw_graph_from_adjacency_matrix(self, adjacency_matrix):
        self.graph = nx.from_numpy_matrix(adjacency_matrix)
        self.draw_graph()

    def draw_graph_from_adjacency_list(self, adjacency_list):
        self.graph = nx.parse_adjlist(adjacency_list, nodetype=int)
        self.draw_graph()

    def split_edges_by_weights(self, chunks, weight_interval):
        split_edges = {}
        for i in range(chunks):
            split_edges[i] = []

        for i in range(chunks):
            for j, (u, v, d) in enumerate(self.get_edges(True)):
                w = d['weight']

                if w > chunks * weight_interval:
                    split_edges[chunks-1].append((u, v))
                    continue

                if w < weight_interval:
                    split_edges[0].append((u, v))
                    continue

                if w > i * weight_interval and w <= (i + 1) * weight_interval:
                    split_edges[i].append((u, v))
        return split_edges

    def are_all_weights_equal(self):
        edges = list(self.get_edges())
        if (len(edges) > 0):
            first_edge = edges[0]
            u = first_edge[0]
            v = first_edge[1]
            comparing_edge_weight = self.graph[u][v]['weight']
        for u, v in edges:
            if self.graph[u][v]['weight'] != comparing_edge_weight:
                return False
        return True

    def get_edge_weights_dict(self):
        edge_labels = {}
        for (u, v, d) in self.get_edges(True):
            edge_labels[(u, v)] = d['weight']

        return edge_labels

    def get_nodes(self):
        return self.graph.nodes(data='weight', default='')

    def get_edges(self, data=False):
        return self.graph.edges(data=data)

    def remove_graph(self):
        self.graph = nx.Graph()

    def get_node_label(self, n):
        return self.graph.node[n]['label']

    def get_edge_weight(self, u, v):
        return self.graph[u][v]['weight']
