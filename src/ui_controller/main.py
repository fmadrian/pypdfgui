from src.appstate import AppState
from PyQt5.QtWidgets import QMessageBox
from src.text import WINDOW_TITLE, MSG_ABOUT

class Ui_Main_Controller:
    def __init__(self, ui):
        self.btn_merge = ui.btn_merge
        self.btn_split = ui.btn_split
        self.btn_about = ui.btn_about
        self.btn_exit = ui.btn_exit

        self.btn_merge.clicked.connect(self.openMerge)
        self.btn_split.clicked.connect(self.openSplit)
        self.btn_about.clicked.connect(self.about)
        self.btn_exit.clicked.connect(self.exit)

    def openMerge(self):
        AppState.open("merge")    
    def openSplit(self):
        AppState.open("split")    
    def about(self):
        QMessageBox(QMessageBox.Information, WINDOW_TITLE, MSG_ABOUT, QMessageBox.Ok).exec()
    def exit(self):
        AppState.exit()
