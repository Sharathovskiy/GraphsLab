class Hamilton:
    def __init__(self, graph_service):
        self.current_starting_node = None
        self.graph_service = graph_service
        self.edges_visited = []
        self.parent_nodes = []

    def check(self):
        self.clear_edges_visited()
        nodes = list(self.graph_service.get_nodes(with_data=True))

        for node in nodes:
            self.current_starting_node = node
            print('current_starting_node: ' + str(node[0]))
            self.check_neighbours(None, node)

            nodes_visited = self.are_all_nodes_visited()
            if not nodes_visited:
                self.clear_visited_from_nodes()
                self.clear_edges_visited()
            else:
                print(self.edges_visited)
                self.order_edges_visited()
                return True

        return False

    def check_neighbours(self, parent_node, child_node):
        child_node_data = child_node[1]
        if 'visited' in child_node_data:
            if child_node_data['visited'] is True:
                return

        child_node_data['visited'] = True
        if parent_node is not None:
            self.edges_visited.append((parent_node[0],child_node[0]))

        neighbours = self.graph_service.graph.neighbors(child_node[0])
        for nbr in neighbours:
            if parent_node is not None:
                if parent_node[0] == nbr: # continue if node to check is parent node
                    continue

            if self.is_visited(nbr):
                continue

            self.parent_nodes.append(child_node[0])

            new_child = self.graph_service.get_node_with_value(nbr)
            self.check_neighbours(child_node, new_child)

            # We want to check each path only once, so when it "comes back" after nested
            # neighbours are checked it means either that it found hamilton path or not.
            if child_node[0] in self.parent_nodes:
                return
        return

    def is_visited(self, node_value):
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

    def clear_visited_from_nodes(self):
        for node in self.graph_service.get_nodes(with_data=True):
            if 'visited' in node[1]:
                node[1]['visited'] = False
        return

    def order_edges_visited(self):
        for idx, (u,v) in enumerate(self.edges_visited):
            self.graph_service.graph[u][v]['placement'] = idx + 1

    def clear_edges_visited(self):
        self.edges_visited = []