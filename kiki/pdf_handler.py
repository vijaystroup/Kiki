from PyPDF2 import PdfFileReader


def file_pdf(file_name: str):
    pdf = PdfFileReader(file_name)

    for page in range(pdf.getNumPages()):
        print(pdf.getPage(page).extractText())
        print()


file_pdf('/mnt/d/sample.pdf')
