import copy

class Eulerian:
    def __init__(self, graph):
        self.graph = graph

    def is_eulerian_circuit(self):
        for v, d in self.graph.degree():
            if d % 2 != 0:
                return False
        return True

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
                    print('(', last_vertex, '-', current_vertex, ')')
                last_vertex = current_vertex
                vertex_stack.pop()
            else:
                from networkx.utils import arbitrary_element
                next_vertex = arbitrary_element(edges(current_vertex))[-1]
                vertex_stack.append(next_vertex)
                G.remove_edge(current_vertex, next_vertex)