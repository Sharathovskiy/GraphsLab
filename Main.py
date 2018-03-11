from tkinter import *

from GraphService import GraphService
from views.SimpleFormAdd import AddGraphSimpleFormViewCreator

if __name__ == '__main__':
    root = Tk()

    AddGraphSimpleFormViewCreator(root)

    root.mainloop()