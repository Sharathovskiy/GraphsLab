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
        split_edges = self.split_edges_by_weights(3, 5)

        pos = nx.spring_layout(self.graph)

        nx.draw_networkx_nodes(self.graph, pos=pos, node_size=700)

        line_width = 2
        for key, value in split_edges.items():
            nx.draw_networkx_edges(self.graph, pos, edgelist=value, width=line_width)
            line_width += 2

        nx.draw_networkx_edge_labels(self.graph, pos=pos, edge_labels=self.get_edge_weights_dict())
        nx.draw_networkx_labels(self.graph, pos)

        plt.axis('off')
        plt.show()

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

    def get_edge_weights_dict(self):
        edge_labels = {}
        for (u, v, d) in self.get_edges(True):
            edge_labels[(u, v)] = d['weight']

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
