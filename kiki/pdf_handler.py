from PyPDF2 import PdfFileReader
from typer import progressbar


def file_pdf(file_name: str):
    pdf = PdfFileReader(file_name, strict=False)

    with progressbar(length=pdf.getNumPages(), label='Downloading') as progress:
        for page in progress:
            text = pdf.getPage(page).extractText()


file_pdf('/mnt/c/Users/Vijay/Downloads/thermalphysics-2ed-Blundell.pdf')
