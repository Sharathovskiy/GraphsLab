from tkinter import *
from GraphService import GraphService


# TODO: Handle Enter hit
class AddGraphSimpleFormViewCreator:
    def __init__(self, master):
        self.graphService = GraphService()

        # NODE COLUMN
        self.add_node_label = Label(master, text="Node")
        self.current_nodes_label = Label(master, text="Current nodes: ")
        self.current_nodes_info = Label(master)
        self.node_label = Label(master, text="Node label")
        self.add_node_button = Button(master, text="+", command=self.add_node)

        self.add_node_entry = Entry(master)
        self.node_label_entry = Entry(master)

        # EDGE COLUMN
        self.add_edge_label = Label(master, text="Edge")
        self.edge_weight_label = Label(master, text="Edge weight")
        self.current_edges_label = Label(master, text="Current edges: ")
        self.current_edges_info = Label(master)
        self.add_edge_button = Button(master, text="+", command=self.add_edge)

        self.add_edge_entry = Entry(master)
        self.edge_weight = Entry(master)

        # DRAW / REMOVE BUTTONS
        self.draw_graph_button = Button(master, text="Draw graph", command=self.draw_graph)
        self.remove_graph_button = Button(master, text="Remove graph", command=self.remove_graph)

        # NODE COLUMN GRID

        # LABELS
        self.add_node_label.grid(row=0, sticky=E)
        self.node_label.grid(row=1, sticky=E)
        self.add_node_button.grid(row=2, columnspan=3)
        self.current_nodes_label.grid(row=3)
        self.current_nodes_info.grid(row=3, column=1, sticky=W)

        # ENTRIES
        self.add_node_entry.grid(row=0, column=1)
        self.node_label_entry.grid(row=1, column=1)

        # EDGE COLUMN GRID

        # LABELS
        self.add_edge_label.grid(row=0, column=2, sticky=E)
        self.edge_weight_label.grid(row=1, column=2, sticky=E)
        self.add_edge_button.grid(row=2, column=3, columnspan=3)
        self.current_edges_label.grid(row=3, column=2)
        self.current_edges_info.grid(row=3, column=3, sticky=W)

        # ENTRIES
        self.add_edge_entry.grid(row=0, column=3)
        self.edge_weight.grid(row=1, column=3)

        # DRAW / REMOVE BUTTONS

        self.draw_graph_button.grid(row=6, columnspan=2)
        self.remove_graph_button.grid(row=6, column=2, columnspan=2)

    def draw_graph(self):
        self.graphService.draw_graph()

    def remove_graph(self):
        self.graphService.remove_graph()
        self.update_info()

    def add_node(self):
        node = self.add_node_entry.get()
        label = self.node_label_entry.get()

        self.graphService.add_node(node, label=label)

        self.erase_entry(self.add_node_entry)
        self.erase_entry(self.node_label_entry)
        self.update_info()

    def add_edge(self):
        data = self.add_edge_entry.get().split(' ')
        # TODO: handle indexes
        u = data[0]
        v = data[1]
        # TODO: handle non numeric weight strings
        weight = float(self.edge_weight.get())
        self.graphService.add_edge(u, v, weight=weight)

        self.erase_entry(self.add_edge_entry)
        self.erase_entry(self.edge_weight)
        self.update_info()

    def update_info(self):
        self.update_nodes_info()
        self.update_edges_info()

    def update_nodes_info(self):
        self.current_nodes_info['text'] = list(self.graphService.get_nodes())

    def update_edges_info(self):
        self.current_edges_info['text'] = list(self.graphService.get_edges())

    def erase_entry(self, entry):
        entry.delete(0, 'end')
