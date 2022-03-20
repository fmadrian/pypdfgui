import os
from PyPDF2 import PdfFileWriter, PdfFileReader


# Splits a single page pdf into several pages.
def pdf_splitter(path, parts):
    # file name.
    fname = os.path.splitext(os.path.basename(path))[0]
    pdf_writer = PdfFileWriter()
    page = get_base_page(path)
    dim = get_dim(page)
    # print(dim)
    upper_right = dim["upperRight"]
    scale = upper_right[1] / parts
    pages = []

    # Generates pages.
    for part in range(0, parts):
        page = get_base_page(path)
        page.cropBox.upperLeft = (0, part * scale)
        page.cropBox.lowerLeft = (0, (part + 1) * scale)
        pages.append(page)

    # Adds the pages to the new pdf in the right order.
    for split_page in range(len(pages)):
        pdf_writer.addPage(pages.pop())

    # Writes new pdf
    output_filename = '{}_{}.pdf'.format(fname, "split")
    with open(output_filename, 'wb') as out:
        pdf_writer.write(out)


# returns first page.
def get_base_page(path):
    pdf = PdfFileReader(path)
    return pdf.getPage(0)


# returns page dimensions.
def get_dim(page):
    return {
        "lowerLeft": page.cropBox.getLowerLeft(),
        "lowerRight" : page.cropBox.getLowerRight(),
        "upperLeft" : page.cropBox.getUpperLeft(),
        "upperRight" : page.cropBox.getUpperRight()
    }

