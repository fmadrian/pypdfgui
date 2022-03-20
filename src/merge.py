import os

from PyPDF2 import PdfFileMerger
from .text import ERROR_INVALID_PDF


class PdfMerger:

    pdfs = []

    def __init__(self):
        pass

    # merges all the pdf in the order defined.
    def normal_merge(self, filename):
        try:
            filename = "{}{}".format(filename, ".pdf")
            merger = PdfFileMerger()
            # joins each pdf in the list.
            for item in self.pdfs:
                if item.endswith('pdf'):
                    merger.append(item)
            merger.write(filename)  # write document
            merger.close()
        except Exception:
            if item is None:
                item = 'No file.'
            raise Exception(ERROR_INVALID_PDF.format(item))

    # merges every pdf located in the same folder as the script.
    def current_dir_merge(self, filename):
        source_dir = os.getcwd()  # get current directory
        merger = PdfFileMerger()

        # joins each pdf in the list.
        for item in os.listdir(source_dir):
            if item.endswith('pdf'):
                merger.append(item)

        merger.write(filename)  # write document
        merger.close()

    def dir_merge(self, other_dir, filename):
        merger = PdfFileMerger()

        # joins each pdf in the list.
        for item in os.listdir(other_dir):
            if item.endswith('pdf'):
                merger.append(item)

        merger.write(filename)  # write document
        merger.close()
