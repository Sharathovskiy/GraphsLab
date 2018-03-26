from tkinter import *
from tkinter.ttk import Notebook

from views.AdjacencyListGraph import AdjacencyListGraph
from views.SimpleFormAdd import AddGraphSimpleFormViewCreator
from views.AdjacencyMatrixGraph import AdjacencyMatrixGraph
from views.IncidenceMatrixGraph import IncidenceMatrixGraph

if __name__ == '__main__':
    root = Tk()
    notebook = Notebook(root)

    frame1 = Frame(notebook)
    frame2 = Frame(notebook)
    frame3 = Frame(notebook)
    frame4 = Frame(notebook)

    notebook.add(frame1, text='Simple form')
    notebook.add(frame2, text='Adjacency Matrix Graph')
    notebook.add(frame3, text='Incidence Matrix Graph')
    notebook.add(frame4, text='Adjacency List Graph')
    notebook.pack()

    AddGraphSimpleFormViewCreator(frame1)
    AdjacencyMatrixGraph(frame2)
    IncidenceMatrixGraph(frame3)
    AdjacencyListGraph(frame4)

    root.mainloop()
