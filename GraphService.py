import networkx as nx
import matplotlib.pyplot as plt


class GraphService:
    def __init__(self, data=None):
        self.graph = nx.Graph(data)

    def add_node(self, n, label=None, weight=None):
        self.graph.add_node(n, weight=weight)
        self.graph.node[n]['label'] = label

    def add_edge(self, u, v, label=None, weight=None):
        self.graph.add_edge(u, v, weight=weight)
        self.graph[u][v]['label'] = label

    def draw_graph(self):
        nx.draw(self.graph, with_labels=True)
        plt.show()

    def get_nodes(self):
        return self.graph.nodes

    def get_edges(self):
        return self.graph.edges

    def remove_graph(self):
        self.graph = nx.Graph()

    def get_edge_label(self, u, v):
        return self.graph[u][v]['label']

    def get_node_label(self, n):
        return self.graph.node[n]['label']
