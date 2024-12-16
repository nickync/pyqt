from __future__ import unicode_literals, print_function

from atom.api import Atom, Str, List, Tuple, Int
import enaml
import sys, os
from enaml.qt.qt_application import QtApplication
from enaml.widgets.api import Label

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

class Notebook(Atom):
    tabs = List( Int() )



def main():
    with enaml.imports():
        from notebook_flow import NotebookFlow

    notebook = Notebook( tabs= [1,2,3] )

    app = QtApplication()
    view = NotebookFlow(notebook)

    view.show()
    app.start()

if __name__ == '__main__':
    main()