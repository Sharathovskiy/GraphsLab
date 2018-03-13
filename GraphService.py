import networkx as nx
import matplotlib.pyplot as plt


class GraphService:
    def __init__(self, data=None):
        self.graph = nx.Graph(data)

    def add_node(self, n, weight=None):
        self.graph.add_node(n, weight=weight)

    def add_edge(self, u, v, weight=None):
        self.graph.add_edge(u, v, weight=weight)

    def draw_graph(self):
        nx.draw(self.graph, with_labels=True)
        plt.show()

    def draw_graph_from_adjacency_matrix(self, adjacency_matrix):
        self.graph = nx.from_numpy_matrix(adjacency_matrix)
        self.draw_graph()

    def get_nodes(self):
        return self.graph.nodes

    def get_edges(self):
        return self.graph.edges

    def remove_graph(self):
        self.graph = nx.Graph()
