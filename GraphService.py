import networkx as nx
import matplotlib.pyplot as plt
from tkinter import *


class GraphService:
    def __init__(self, data=None):
        self.graph = nx.Graph(data)
        self.edges_visited= []

    def add_node(self, n, label=None):
        self.graph.add_node(n, label=label)

    def add_edge(self, u, v, weight=None):
        self.graph.add_edge(u, v, weight=weight)

    def draw_graph(self):
        pos = nx.spring_layout(self.graph)

        nx.draw_networkx_nodes(self.graph, pos=pos, node_size=700)

        self.hamilton()

        nx.draw_networkx_edges(self.graph, pos, edgelist=self.edges_visited, width=6)
        nx.draw_networkx_edges(self.graph, pos)

        if not self.are_all_weights_equal():
            edge_labels = self.get_edge_weights_dict()
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

    def hamilton(self):
        nodes = list(self.get_nodes(True))
        self.check_nbrs(None, nodes[0])
        print(nodes)
        print(self.edges_visited)

    def get_node_with_value(self, value):
        nodes = self.graph.nodes(data=True)
        for node in list(nodes):
            if node[0] == value:
                return node
        return None

    def check_nbrs(self, parent_node, child_node):
        child_node_data = child_node[1]
        if 'visited' in child_node_data:
            if child_node_data['visited'] is True:
                return

        child_node_data['visited'] = True
        if parent_node is not None:
            self.edges_visited.append((parent_node[0],child_node[0]))
        for nbr in self.graph.neighbors(child_node[0]):
            new_child = self.get_node_with_value(nbr)
            self.check_nbrs(child_node, new_child)
        return

    def do_edges_have_weight(self):
        for u, v, d in self.get_edges(True):
            if 'weight' not in d:
                return False
        return True

    def get_edge_weights_dict(self):
        edge_labels = {}
        if self.do_edges_have_weight():
            for (u, v, d) in self.get_edges(True):
                edge_labels[(u, v)] = d['weight']
        return edge_labels

    def get_nodes(self, with_data = False):
        return self.graph.nodes(with_data)

    def get_edges(self, with_data=False):
        return self.graph.edges(data=with_data)

    def remove_graph(self):
        self.graph = nx.Graph()
        self.edges_visited = []

    def get_node_label(self, n):
        return self.graph.node[n]['label']

    def get_edge_weight(self, u, v):
        return self.graph[u][v]['weight']
