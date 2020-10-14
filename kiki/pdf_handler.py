from os import remove
from gtts import gTTS
from PyPDF2 import PdfFileReader
from typer import progressbar
import requests
from .utils import error_message


def download(pdf, file_out):
    """function that takes a pdf object and converts it to an audio file"""

    with progressbar(length=pdf.getNumPages(), label='Downloading') as progress:
        with open(f'{file_out}.mp3', 'wb') as f:
            for page in progress:
                text = pdf.getPage(page).extractText()
                if text:
                    tts = gTTS(text)
                    tts.write_to_fp(f)


def file_pdf(file_name, file_out):
    """create pdf object from file and download audio"""

    pdf = PdfFileReader(file_name, strict=False)
    download(pdf, file_out)


def url_pdf(url, file_out):
    """make pdf object from beautifulsoup and download audio"""

    file_name = 'kiki_temp.pdf'

    try:
        r = requests.get(url, timeout=3)
        if r.status_code == 200:
            with open(file_name, 'wb') as f:
                f.write(r.content)
            pdf = PdfFileReader(file_name, strict=False)
            download(pdf, file_out)
            remove(file_name)
        else:
            error_message(f'{url} is invalid.')
    except requests.exceptions.Timeout:
        error_message(f'Request for {url} timed out.')
    except requests.exceptions.RequestException as e:
        error_message(f'Request for {url} is invalid.')
