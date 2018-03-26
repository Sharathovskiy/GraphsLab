from tkinter import *
from tkinter.ttk import Notebook

from views.SimpleFormAdd import AddGraphSimpleFormViewCreator
from views.AdjacencyMatrixGraph import AdjacencyMatrixGraph

if __name__ == '__main__':
    root = Tk()
    notebook = Notebook(root)

    frame1 = Frame(notebook)
    frame2 = Frame(notebook)
    frame3 = Frame(notebook)

    notebook.add(frame1, text='Simple form')
    notebook.add(frame2, text='Adjacency matrix')
    notebook.add(frame3, text='Adjacency list')
    notebook.pack()

    AddGraphSimpleFormViewCreator(frame1)
    AdjacencyMatrixGraph(frame2)

    root.mainloop()
