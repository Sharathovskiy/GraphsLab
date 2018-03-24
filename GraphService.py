import networkx as nx
import matplotlib.pyplot as plt


class GraphService:
    def __init__(self, data=None):
        self.graph = nx.Graph(data)

    def add_node(self, n, label=None):
        self.graph.add_node(n, label=label)

    def add_edge(self, u, v, weight=None):
        self.graph.add_edge(u, v, weight=weight)


    def draw_graph(self):
        nx.draw_networkx_edge_labels(self.graph, pos=nx.spring_layout(self.graph), edge_labels=self.get_weights_as_edge_labels())
        nx.draw(self.graph, with_labels=True)
        plt.show()

    def get_weights_as_edge_labels(self):
        edge_labels = {}
        for (u,v, d) in self.get_edges(True):
            edge_labels[(u,v)] = d['weight']

        return edge_labels

    def get_nodes(self):
        return self.graph.nodes

    def get_edges(self, data=False):
        return self.graph.edges(data=data)

    def remove_graph(self):
        self.graph = nx.Graph()

    def get_node_label(self, n):
        return self.graph.node[n]['label']

    def get_edge_weight(self, u, v):
        return self.graph[u][v]['weight']
