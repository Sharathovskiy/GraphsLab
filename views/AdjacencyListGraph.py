from tkinter import *
from tkinter import messagebox
import numpy

from GraphService import GraphService


class AdjacencyListGraph:

    def __init__(self, master):
        self.graph_service = GraphService()

        # GUI ELEMENTS
        self.adjacency_list_entry = Entry(master)
        self.draw_graph_button = Button(master, text="Draw graph", command=self.draw_graph)
        self.nodes_listbox = Listbox(master)
        self.edges_listbox = Listbox(master)

        self.nodes_label = Label(master, text="Nodes List: ")
        self.edges_label = Label(master, text="Edges List: ")

        self.nodes_entry = Entry(master)
        self.set_node_weight_button = Button(master, text="Set weight")

        self.edges_entry = Entry(master)
        self.set_edge_label_button = Button(master, text="Set Label")

        # GRID
        self.adjacency_list_entry.grid(row=0, column=1)
        self.draw_graph_button.grid(row=1, column=1)

        self.nodes_label.grid(row=0, column=2)
        self.nodes_listbox.grid(row=1, column=2)

        self.edges_label.grid(row=0, column=3)
        self.edges_listbox.grid(row=1, column=3)

        self.nodes_entry.grid(row=0, column=4)
        self.set_node_weight_button.grid(row=1, column=4)

        self.edges_entry.grid(row=2, column=4)
        self.set_edge_label_button.grid(row=3, column=4)

        def on_edge_select(evt):
            w = evt.widget
            index = int(w.curselection()[0])
            value = w.get(index)[1]
            self.nodes_entry.delete(0, END)
            self.nodes_entry.insert(0, value)

        def on_node_select(evt):
            w = evt.widget
            index = int(w.curselection()[0])
            value = w.get(index)[2]
            self.nodes_entry.delete(0, END)
            self.nodes_entry.insert(0, value)

        self.edges_listbox.bind('<<ListboxSelect>>', on_edge_select)
        self.nodes_listbox.bind('<<ListboxSelect>>', on_node_select)

    def draw_graph(self):
        try:
            adjacency_list = self.adjacency_list_entry.get().split(";")
            self.graph_service.draw_graph_from_adjacency_list(adjacency_list, self.nodes_listbox, self.edges_listbox)
        except Exception as err:
            messagebox.showerror('Exception', err)
