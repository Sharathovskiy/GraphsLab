import networkx as nx
import matplotlib.pyplot as plt
from tkinter import *

from Hamilton import Hamilton


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

        hamilton = Hamilton(self)
        is_hamilton = hamilton.check()

        if is_hamilton:
            nx.draw_networkx_edges(self.graph, pos, edgelist=hamilton.edges_visited, width=6)
            edge_labels = self.get_edge_dict_with_property('placement')
            nx.draw_networkx_edge_labels(self.graph, pos=pos, edge_labels=edge_labels)

        nx.draw_networkx_edges(self.graph, pos)

        if not self.are_all_weights_equal():
            edge_labels = self.get_edge_dict_with_property('weight')
            nx.draw_networkx_edge_labels(self.graph, pos=pos, edge_labels=edge_labels)

        nx.draw_networkx_labels(self.graph, pos)

        plt.axis('off')
        plt.show()

    def draw_graph_from_adjacency_matrix(self, adjacency_matrix):
        self.graph = nx.from_numpy_matrix(adjacency_matrix)
        self.draw_graph()

    def draw_graph_from_adjacency_list(self, adjacency_list):
        self.graph = nx.parse_adjlist(adjacency_list, nodetype=int)
        self.draw_graph()

    def are_all_weights_equal(self):
        if not self.do_edges_have_weight():
            return True
        edges = list(self.get_edges(True))
        if len(edges) > 0:
            first_edge_data = edges[0][2]
            comparing_edge_weight = first_edge_data['weight']
        else:
            return True
        for u, v, d in edges:
            if d['weight'] != comparing_edge_weight:
                return False
        return True

    def get_node_with_value(self, value):
        nodes = self.get_nodes(with_data=True)
        for node in list(nodes):
            if node[0] == value:
                return node
        return None

    def do_edges_have_weight(self):
        for u, v, d in self.get_edges(True):
            if 'weight' not in d:
                return False
        return True

    def get_edge_dict_with_property(self, property):
        edge_labels = {}
        for (u, v, d) in self.get_edges(True):
            if property in d:
                edge_labels[(u, v)] = d[property]
        return edge_labels

    def get_nodes(self, with_data = False):
        return self.graph.nodes(with_data)

    def get_edges(self, with_data=False):
        return self.graph.edges(data=with_data)

    def remove_graph(self):
        self.graph = nx.Graph()

    def get_node_label(self, n):
        return self.graph.node[n]['label']

    def get_edge_weight(self, u, v):
        return self.graph[u][v]['weight']
