import sys
import os
from PyQt6.QtPdf import QPdfDocument
from PyQt6.QtPdfWidgets import QPdfView
from PyQt6.QtWidgets import QApplication

class PDFViewerExample(QApplication):

    def __init__(self, path):
        super().__init__(sys.argv)

        self.file_path = path

        self.document = QPdfDocument(None)

        self.view = QPdfView(None)
        self.view.setGeometry(400, 200, 800, 600)


    def setup_ui(self):
        self.document.load(self.file_path)
         
        self.view.setPageMode(QPdfView.PageMode.MultiPage)
        
        self.view.setDocument(self.document)

        self.view.show()

        self.exec()

path = 'test.pdf'
app = PDFViewerExample(path)
app.setup_ui()