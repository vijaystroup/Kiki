# Kiki

Named after the Google voice actress Kiki Baessell.  
Kiki will transform your PDFs into audio files for you to listen to.

## Installation
### Dependencies
- Python 3
- Python 3 pip

```bash
$ pip install kiki
```

## Usage
```bash
$ kiki
Usage: kiki [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  get     get audio from pdf
  github  open github repo for Kiki
```

```bash
$ kiki get --help
Usage: kiki get [OPTIONS] PDF

  get audio from pdf

Arguments:
  PDF  url or file of pdf  [required]

Options:
  --filename TEXT  name of output file without extension  [default: kiki]
  --help           Show this message and exit.


$ kiki get http://www.africau.edu/images/default/sample.pdf
Downloading  [####################################]  100%          
Your audio file is now available at kiki.mp3
```
