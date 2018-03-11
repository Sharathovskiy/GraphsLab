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

    def get_nodes(self):
        return self.graph.nodes

    def get_edges(self):
        return self.graph.edges