from tkinter import *

from GraphService import GraphService
from tkinter.ttk import Notebook

from views.SimpleFormAdd import AddGraphSimpleFormViewCreator
from views.AdjacencyMatrixGraph import AdjacencyMatrixGraph

if __name__ == '__main__':
    root = Tk()
    notebook = Notebook(root)

    frame1 = Frame(notebook)
    frame2 = Frame(notebook)

    notebook.add(frame1, text='Frame One')
    notebook.add(frame2, text='Frame Two')
    notebook.pack()

    AddGraphSimpleFormViewCreator(frame1)
    AdjacencyMatrixGraph(frame2)

    root.mainloop()
