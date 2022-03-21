from PyQt5.QtWidgets import QMessageBox, QFileDialog
from src.appstate import AppState
import src.split as functions
class Ui_Split_Controller:

    def __init__(self, ui):
        self.btn_loadfile = ui.btn_loadfile
        self.btn_split = ui.btn_split
        self.lbl_filename = ui.lbl_filename
        self.box_pieces = ui.box_pieces
        self.btn_back = ui.btn_back

        self.btn_loadfile.clicked.connect(self.loadFile)
        self.btn_split.clicked.connect(self.split)
        self.btn_back.clicked.connect(self.back)
        self.filename = ""

        self.update()

    def loadFile(self):
        self.filename = QFileDialog.getOpenFileName(caption="PDF", filter="PDF (*.pdf)")[0]
        self.update()

    def split(self):
        try:
            pieces = self.box_pieces.value()
            if(pieces > 1):
                functions.pdf_splitter(self.filename, pieces)
                QMessageBox(QMessageBox.Information, "Información", "Listo.", QMessageBox.Ok).exec()
        except Exception as e:
            QMessageBox(QMessageBox.Critical, "Error", str(e), QMessageBox.Ok).exec()

    def update(self):
        if self.filename != "":
            self.btn_split.setEnabled(True)
            self.lbl_filename.setText(self.filename)
        else:
            self.btn_split.setEnabled(False)
            self.lbl_filename.setText("")

    def back(self):
        AppState.open("main")