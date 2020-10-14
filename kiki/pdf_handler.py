from gtts import gTTS
from PyPDF2 import PdfFileReader
from typer import progressbar


def download(pdf):
    with progressbar(length=pdf.getNumPages(), label='Downloading') as progress:
        with open('asdf.mp3', 'wb') as f:
            for page in progress:
                text = pdf.getPage(page).extractText()
                if text:
                    tts = gTTS(text)
                    tts.write_to_fp(f)


def file_pdf(file_name):
    pdf = PdfFileReader(file_name, strict=False)
    download(pdf)


def url_pdf(url):
    # make PdfFileReader obj out of beautiful soup
    pass


file_pdf('/mnt/c/Users/Vijay/Downloads/CitationNeededBook-Sample.pdf')
