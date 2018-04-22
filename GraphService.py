import copy

import matplotlib.pyplot as plt
import networkx as nx

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
            nx.draw_networkx_edges(self.graph, pos, edgelist=hamilton.visited_edges, width=6)
            edge_labels = self.get_edge_dict_with_property('placement')
            nx.draw_networkx_edge_labels(self.graph, pos=pos, edge_labels=edge_labels)

        nx.draw_networkx_edges(self.graph, pos)

        if not self.are_all_weights_equal():
            edge_labels = self.get_edge_dict_with_property('weight')
            nx.draw_networkx_edge_labels(self.graph, pos=pos, edge_labels=edge_labels)

        nx.draw_networkx_labels(self.graph, pos)

        if self.is_eulerian_circuit():
            plt.suptitle('Is an Euler\'s circuit.', color='green')
        else:
            plt.suptitle('Is not an Euler\'s circuit.', color='red')

        self.eulerian_circuit(0)
        plt.axis('off')
        plt.show()

    def is_eulerian_circuit(self):
        for v, d in self.graph.degree():
            if d % 2 != 0:
                return False
        return True


    # 0 1 0 0 0 1 0 1 1;
    # 1 0 1 0 0 0 0 1 0;
    # 0 1 0 1 0 0 0 0 0;
    # 0 1 1 0 0 0 0 0 0;
    # 0 0 0 0 0 0 1 1 0;
    # 1 0 0 0 0 0 0 0 1;
    # 0 0 0 0 1 0 1 0 0;
    # 1 1 0 0 1 0 1 0 0;
    # 1 0 0 0 0 1 0 0 0
    def eulerian_circuit(self, start=0):
        G = copy.deepcopy(self.graph)
        degree = G.degree
        edges = G.edges

        vertex_stack = [start]
        last_vertex = None
        while vertex_stack:
            current_vertex = vertex_stack[-1]
            if degree(current_vertex) == 0:
                if last_vertex is not None:
                    print('(',last_vertex,'-', current_vertex, ')')
                last_vertex = current_vertex
                vertex_stack.pop()
            else:
                from networkx.utils import arbitrary_element
                next_vertex = arbitrary_element(edges(current_vertex))[-1]
                vertex_stack.append(next_vertex)
                G.remove_edge(current_vertex, next_vertex)

    # Example Adjacency List: 0 1 3; 1 2 4; 3 5 6; 5 7
    def dfs(self, start):
        G = self.graph.adj
        stack, path = [start], []

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
