class Hamilton:
    def __init__(self, graph_service):
        self.current_starting_node = None
        self.graph_service = graph_service
        self.visited_edges = []
        self.hamilton_cycle_found = False

    def is_hamilton_cycle(self):
        return self.is_hamilton(self.look_for_hamilton_cycle)

    def is_hamilton_path(self):
        return self.is_hamilton(self.look_for_hamilton_path)

    def is_hamilton(self, hamilton_function):
        self.clear_visited_edges()
        self.make_all_nodes_unvisited()
        nodes = list(self.graph_service.get_nodes(with_data=True))

        for node in nodes:
            self.current_starting_node = node
            hamilton_function(None, node)

            nodes_visited = self.are_all_nodes_visited()
            if nodes_visited:
                self.set_visited_edges_order()
                return True
            else:
                self.make_all_nodes_unvisited()
                self.clear_visited_edges()

        return False

    def look_for_hamilton_cycle(self, parent_node, child_node):
        child_node_data = child_node[1]
        if 'visited' in child_node_data:
            if child_node_data['visited'] is True:
                return

        child_node_data['visited'] = True
        if parent_node is not None:
            self.visited_edges.append((parent_node[0], child_node[0]))
            print('adding path: ' + str((parent_node[0], child_node[0])) + 'for starting node: ' + str( self.current_starting_node[0]))

        starting_node_value = self.current_starting_node[0]

        neighbours = self.graph_service.graph.neighbors(child_node[0])
        for nbr in neighbours:
            if self.hamilton_cycle_found:
                return

            if parent_node is None:
                self.make_all_nodes_unvisited()
                child_node_data['visited'] = True
                self.clear_visited_edges()
            else:
                if nbr == parent_node[0]: # continue if node to check is parent node
                    continue

            if self.is_node_visited(nbr) and nbr != starting_node_value:
                continue

            new_child = self.graph_service.get_node_with_value(nbr)
            self.look_for_hamilton_cycle(child_node, new_child)

            # if neighbour is starting node and all nodes are visited
            # it means that we found hamilton cycle
            if nbr == starting_node_value:
                if self.are_all_nodes_visited():
                    self.visited_edges.append((nbr, child_node[0]))
                    self.hamilton_cycle_found = True
                    return

            if not self.hamilton_cycle_found:
                self.unset_visited_edge(child_node[0], new_child[0])
                self.make_node_unvisited(new_child)
                print('unvisit: ' + str(new_child))

        return

    def look_for_hamilton_path(self, parent_node, child_node):
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
            self.look_for_hamilton_path(child_node, new_child)

            # We want to check each path only once, so when it "comes back" after nested
            # neighbours are checked it means either that it found hamilton path or not.
            if self.is_node_visited(child_node[0]):
                return
        return

    def unset_visited_edge(self, u, v):
        if (u,v) in self.visited_edges:
            self.visited_edges.remove((u,v))

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

    def make_all_nodes_unvisited(self):
        for node in self.graph_service.get_nodes(with_data=True):
            self.make_node_unvisited(node)
        return

    def make_node_unvisited(self, node):
        if 'visited' in node[1]:
            node[1]['visited'] = False

    def set_visited_edges_order(self):
        for idx, (u,v) in enumerate(self.visited_edges):
            self.graph_service.graph[u][v]['placement'] = idx + 1

    def clear_visited_edges(self):
        self.visited_edges = []