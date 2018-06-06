class PathFinder:
    def __init__(self, graph_service, starting_node):
        self.graph_service = graph_service
        self.starting_node = starting_node
        self.current_path = []
        self.paths = []
        self.shortest_paths_to_all_nodes = []
        print("starting node: " + str(starting_node))

    def get_shortest_path_to_all_nodes_using_weights(self):
        for node in self.graph_service.get_nodes():
            shortest_path = self.get_shortest_path_to_node_using_weights(node)
            if shortest_path is not None:
                shortest_path.append(node)
                self.shortest_paths_to_all_nodes.append(shortest_path)
        return self.shortest_paths_to_all_nodes

    def get_shortest_path_to_node_using_weights(self, to_node):
        self.get_paths_to_node(to_node)
        if not self.paths:
            return None
        shortest_path = self.paths[0]
        for path in self.paths:
            if self.get_path_weight(shortest_path, to_node) > self.get_path_weight(path, to_node):
                shortest_path = path
        self.paths = []
        return shortest_path

    def get_path_weight(self, path, to_node):
        # If list is empty it means starting node is connected directly with to_node
        if not path:
            return self.graph_service.get_edge_weight(self.starting_node, to_node)

        weight = self.graph_service.get_edge_weight(self.starting_node, path[0])

        for idx, node in enumerate(path):
            if len(path) > idx + 1:  # If next array element exist
                weight += self.graph_service.get_edge_weight(node, path[idx + 1])
            else:
                weight += self.graph_service.get_edge_weight(node, to_node)

        return weight

    def get_shortest_path_to_node(self, to_node):
        print('to node: ' + str(to_node))
        self.get_paths_to_node(to_node)
        if len(self.paths) <= 0:
            return None

        shortest_path = self.paths[0]
        for path in self.paths:
            if len(path) < len(shortest_path):
                shortest_path = path
        return shortest_path

    def get_paths_to_node(self, to_node, from_node=None):
        if from_node is None:
            from_node = self.starting_node
        if from_node is to_node:
            print('From node is to node')
            return

        neighbours = self.graph_service.graph.neighbors(from_node)
        for nbr in neighbours:
            nbr = int(nbr)
            if nbr in self.current_path or nbr is self.starting_node:
                continue
            if nbr is to_node:
                self.paths.append(list(self.current_path))
                continue

            self.current_path.append(nbr)
            self.get_paths_to_node(to_node, nbr)
            if nbr is not self.starting_node:
                self.current_path.remove(nbr)
