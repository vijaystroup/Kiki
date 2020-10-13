from PyPDF2 import PdfFileReader
from typer import progressbar
from gtts import gTTS


def file_pdf(file_name: str):
    pdf = PdfFileReader(file_name, strict=False)

    with progressbar(length=pdf.getNumPages(), label='Downloading') as progress:
        with open('asdf.mp3', 'wb') as f:
            for page in progress:
                text = pdf.getPage(page).extractText()
                if text:
                    tts = gTTS(text)
                    tts.write_to_fp(f)


file_pdf('/mnt/c/Users/Vijay/Downloads/CitationNeededBook-Sample.pdf')
