from gtts import gTTS
from PyPDF2 import PdfFileReader
from typer import progressbar
import requests
from utils import error_message


def download(pdf):
    """function that takes a pdf object and converts it to an audio file"""

    with progressbar(length=pdf.getNumPages(), label='Downloading') as progress:
        with open('asdf.mp3', 'wb') as f:
            for page in progress:
                text = pdf.getPage(page).extractText()
                if text:
                    tts = gTTS(text)
                    tts.write_to_fp(f)


def file_pdf(file_name):
    """create pdf object from file and download audio"""

    pdf = PdfFileReader(file_name, strict=False)
    download(pdf)


def url_pdf(url):
    """make pdf object from beautifulsoup and download audio"""

    filename = 'kiki_temp.pdf'

    try:
        r = requests.get(url, timeout=3)
        if r.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(r.content)
        else:
            error_message(f'{url} is invalid.')
    except TimeoutError as e:
        error_message(f'Request for {url} timed out.')
        raise Exit()


# file_pdf('/mnt/c/Users/Vijay/Downloads/CitationNeededBook-Sample.pdf')
url_pdf('http://www.pdf995.com/samples/pdfs.pdf')
