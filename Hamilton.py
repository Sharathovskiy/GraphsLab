class Hamilton:
    def __init__(self, graph_service):
        self.current_starting_node = None
        self.graph_service = graph_service
        self.visited_edges = []
        self.parent_nodes = []

    def check(self):
        self.clear_visited_edges()
        nodes = list(self.graph_service.get_nodes(with_data=True))

        for node in nodes:
            self.current_starting_node = node
            self.check_neighbours(None, node)

            nodes_visited = self.are_all_nodes_visited()
            if nodes_visited:
                self.set_visited_edges_order()
                return True
            else:
                self.make_nodes_unvisited()
                self.clear_visited_edges()

        return False

    def check_neighbours(self, parent_node, child_node):
        child_node_data = child_node[1]
        if 'visited' in child_node_data:
            if child_node_data['visited'] is True:
                return

        child_node_data['visited'] = True
        if parent_node is not None:
            self.visited_edges.append((parent_node[0], child_node[0]))

        neighbours = self.graph_service.graph.neighbors(child_node[0])
        for nbr in neighbours:
            if parent_node is not None:
                if parent_node[0] == nbr: # continue if node to check is parent node
                    continue

            if self.is_node_visited(nbr):
                continue

            new_child = self.graph_service.get_node_with_value(nbr)
            self.check_neighbours(child_node, new_child)

            # We want to check each path only once, so when it "comes back" after nested
            # neighbours are checked it means either that it found hamilton path or not.
            if self.is_node_visited(child_node[0]):
                return
        return

    def is_node_visited(self, node_value):
        node = self.graph_service.graph.node[node_value]
        if 'visited' in node:
            if node['visited'] is True:
                return True
        return False

    def are_all_nodes_visited(self):
        for node in self.graph_service.get_nodes(with_data=True):
            if 'visited' not in node[1]:
                return False
            if node[1]['visited'] is False:
                return False
        return True

    def make_nodes_unvisited(self):
        for node in self.graph_service.get_nodes(with_data=True):
            if 'visited' in node[1]:
                node[1]['visited'] = False
        return

    def set_visited_edges_order(self):
        for idx, (u,v) in enumerate(self.visited_edges):
            self.graph_service.graph[u][v]['placement'] = idx + 1

    def clear_visited_edges(self):
        self.visited_edges = []