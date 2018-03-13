from tkinter import *
from tkinter.ttk import Notebook

from views.SimpleFormAdd import AddGraphSimpleFormViewCreator
from views.AdjacencyMatrixGraph import AdjacencyMatrixGraph
from views.AdjacencyListGraph import AdjacencyListGraph

if __name__ == '__main__':
    root = Tk()
    notebook = Notebook(root)

    frame1 = Frame(notebook)
    frame2 = Frame(notebook)
    frame3 = Frame(notebook)

    notebook.add(frame1, text='Frame One')
    notebook.add(frame2, text='Frame Two')
    notebook.add(frame3, text='Adjacency List')
    notebook.pack()

    AddGraphSimpleFormViewCreator(frame1)
    AdjacencyMatrixGraph(frame2)
    AdjacencyListGraph(frame3)

    root.mainloop()
