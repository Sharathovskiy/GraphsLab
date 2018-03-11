from tkinter import *

class AddGraphSimpleFormViewCreator:
    def __init__(self, master):
        # GUI ELEMENTS
        self.add_edge_label = Label(master, text="Add edge")
        self.add_node_label = Label(master, text="Add node")

        self.add_edge_entry = Entry(master)
        self.add_node_entry = Entry(master)

        self.current_edges_label = Label(master, text="Current edges: ")
        self.current_nodes_label = Label(master, text="Current nodes: ")

        self.add_edge_button = Button(master, text="+", command=self.add_edge)
        self.add_node_button = Button(master, text="+", command=self.add_node)

        self.draw_graph_button = Button(master, text="Draw graph", command=self.draw_graph)

        # GRID
        self.add_edge_label.grid(row=0, sticky=E)
        self.add_node_label.grid(row=1, sticky=E)

        self.add_edge_entry.grid(row=0, column=1)
        self.add_node_entry.grid(row=1, column=1)

        self.current_edges_label.grid(row=0, column=3)
        self.current_nodes_label.grid(row=1, column=3)

        self.add_edge_button.grid(row=0, column=2)
        self.add_node_button.grid(row=1, column=2)

        self.draw_graph_button.grid(row=2, columnspan=4)

    def draw_graph(self):
        print("draw placeholder")

    def add_edge(self):
        print("add edge placeholder")

    def add_node(self):
        print("add node placeholder")