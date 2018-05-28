import itertools
import random

import matplotlib.pyplot as plt
import networkx as nx

from Eulerian import Eulerian
from Hamilton import Hamilton


class GraphService:
    def __init__(self, graph = None):
        self.graph = graph
        self.color_map = []

    def add_node(self, n, label=None):
        self.graph.add_node(n, label=label)

    def add_edge(self, u, v, weight=None):
        self.graph.add_edge(u, v, weight=weight)

    def draw_graph(self):
        pos = nx.spring_layout(self.graph)

        print(self.color_graph())
        print(self.get_nodes(True))

        nx.draw_networkx_nodes(self.graph, node_color= self.color_map, pos=pos, node_size=700)

        hamilton = Hamilton(self)
        is_hamilton_cycle = hamilton.is_hamilton_cycle()

        if is_hamilton_cycle:
            nx.draw_networkx_edges(self.graph, pos, edgelist=hamilton.visited_edges, width=6)
            edge_labels = self.get_edge_dict_with_property('placement')
            nx.draw_networkx_edge_labels(self.graph, pos=pos, edge_labels=edge_labels)

        nx.draw_networkx_edges(self.graph, pos)

        if not self.are_all_weights_equal():
            edge_labels = self.get_edge_dict_with_property('weight')
            nx.draw_networkx_edge_labels(self.graph, pos=pos, edge_labels=edge_labels)

        nx.draw_networkx_labels(self.graph, pos)

        eulerian = Eulerian(self.graph)

        if eulerian.is_eulerian_circuit():
            plt.suptitle('Is an Euler\'s circuit.', color='green')
        else:
            plt.suptitle('Is not an Euler\'s circuit.', color='red')

        eulerian.eulerian_circuit(0)
        print('Critical edges: ' + str(self.get_critical_edges()))
        plt.axis('off')
        plt.show()

    # Example Adjacency List: 0 1 3; 1 2 4; 3 5 6; 5 7
    def get_dfs_path(self):
        G = self.graph.adj
        nodes = list(self.graph.nodes())

        if len(nodes) > 0:
            starting_vertex = nodes[0]
        else:
            return

        stack, path = [starting_vertex], []

        while stack:
            vertex = stack.pop()
            if vertex in path:
                continue
            path.append(vertex)
            for neighbor in G[vertex]:
                stack.append(neighbor)

        return path

    def draw_graph_from_adjacency_matrix(self, adjacency_matrix):
        self.graph = nx.from_numpy_matrix(adjacency_matrix)
        self.draw_graph()

    def draw_graph_from_adjacency_list(self, adjacency_list):
        self.graph = nx.parse_adjlist(adjacency_list, nodetype=int)
        self.draw_graph()

    def get_critical_edges(self):
        edges = list(self.get_edges())
        critical_edges = []
        for edge in edges:
            self.graph.remove_edge(*edge)
            if not self.is_graph_connected():
                critical_edges.append(edge)
            self.graph.add_edge(*edge)
        return critical_edges

    def is_graph_connected(self):
        dfs_path = self.get_dfs_path()
        nodes = self.get_nodes()
        for node in nodes:
            if node not in dfs_path:
                return False
        return True

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

    def color_graph(self):
        self.color_map = []
        colors = {}
        #nodes = self.descent_colouring()
        #nodes = self.random_colouring()
        nodes = self.normal_colouring()
        for u in nodes:
            neighbour_colors = {colors[v] for v in self.graph[u] if v in colors}
            dupa = ['blue','red','green','orange','yellow','purple']
            for color in dupa:
                if color not in neighbour_colors:
                    break
            colors[u] = color

        for node in list(self.graph):
            self.color_map.append(colors[node])

        return colors

    def descent_colouring(self):
        return sorted(self.graph, key=self.graph.degree, reverse=True)

    def random_colouring(self):
        nodes = list(self.graph)
        random.shuffle(nodes)
        return nodes

    def normal_colouring(self):
        return list(self.graph)
