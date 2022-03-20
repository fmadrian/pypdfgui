import sys
from src.text import MSG_ERROR, MSG_SUCCESS, ERROR_NO_NAME, ERROR_NO_FILES, WINDOW_TITLE, MSG_ABOUT
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from src.merge import PdfMerger


class Ui_Merge_Controller:

    def __init__(self, window):
        self.btn_merge = window.btn_merge
        self.btn_add = window.btn_add
        self.lbl_name = window.lbl_name
        self.btn_up = window.btn_up
        self.btn_down = window.btn_down
        self.btn_delete = window.btn_delete
        self.txt_name = window.txt_name
        self.lst_pdf = window.lst_pdf

        self.action_exit = window.action_exit
        self.action_about = window.action_about

        self.btn_merge.clicked.connect(self.merge)
        self.action_exit.triggered.connect(self.exit)
        self.action_about.triggered.connect(self.about)
        self.btn_add.clicked.connect(self.add)
        self.btn_up.clicked.connect(self.moveUp)
        self.btn_down.clicked.connect(self.moveDown)
        self.btn_delete.clicked.connect(self.delete)

        self.merger = PdfMerger()

    # adds one or several items to the list.
    def add(self):
        files = QFileDialog.getOpenFileNames(
            caption=WINDOW_TITLE, filter="PDF (*.pdf)")
        # file[0] = filepath / files[0] = filepaths
        # reverse the list because it comes in reverse order.
        # files[0].reverse()
        for file in files[0]:
            if file.endswith('pdf'):
                # inserta al inicio.
                self.merger.pdfs.append(file)
        self.show_list()

    # deletes the selected item.
    def delete(self):
        try:
            item = self.lst_pdf.currentRow()
            if item >= 0:
                self.merger.pdfs.pop(item)
        except Exception as e:
            QMessageBox(QMessageBox.Critical, MSG_ERROR,
                        str(e), QMessageBox.Ok).exec()
        finally:
            self.show_list()

    # shows selected pdfs.
    def show_list(self):
        # get selected item
        item_selected = self.lst_pdf.currentRow()
        self.lst_pdf.clear()
        for pdf in self.merger.pdfs:
            self.lst_pdf.addItem(pdf)
        # return the focus to the selected item. (if selected)
        if(item_selected > -1):
            self.lst_pdf.setCurrentRow(item_selected)

    # merges selected pdfs.
    def merge(self):
        try:
            if(len(self.merger.pdfs) > 0):
                if(self.txt_name.text().strip() is None or self.txt_name.text().strip() != ""):
                    self.merger.normal_merge(self.txt_name.text())
                    QMessageBox(QMessageBox.Information, WINDOW_TITLE,
                                MSG_SUCCESS, QMessageBox.Ok).exec()
                else:
                    raise Exception(ERROR_NO_NAME)
            else:
                raise Exception(ERROR_NO_FILES)
        except Exception as e:
            QMessageBox(QMessageBox.Critical, MSG_ERROR,
                        str(e), QMessageBox.Ok).exec()

    def exit(self):
        sys.exit()

    # moves an item up in the list
    def moveUp(self):
        try:
            itemIndex = self.lst_pdf.currentRow()
            if itemIndex > 0:
                # move the selected item one position up.
                item = self.merger.pdfs.pop(itemIndex)
                self.merger.pdfs.insert(itemIndex-1, item)
                self.lst_pdf.setCurrentRow(itemIndex-1)
        except Exception as e:
            QMessageBox(QMessageBox.Critical, MSG_ERROR,
                        str(e), QMessageBox.Ok).exec()
        finally:
            self.show_list()

    # moves an item down in the list
    def moveDown(self):
        try:
            itemIndex = self.lst_pdf.currentRow()
            if itemIndex < len(self.merger.pdfs)-1:
                # move the selected item one position up.
                item = self.merger.pdfs.pop(itemIndex)
                self.merger.pdfs.insert(itemIndex+1, item)
                self.lst_pdf.setCurrentRow(itemIndex+1)
        except Exception as e:
            QMessageBox(QMessageBox.Critical, MSG_ERROR,
                        str(e), QMessageBox.Ok).exec()
        finally:
            self.show_list()

    def about(self):
        QMessageBox(QMessageBox.Information, WINDOW_TITLE,
                    MSG_ABOUT, QMessageBox.Ok).exec()
