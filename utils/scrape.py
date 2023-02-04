import wget
import os
from PyPDF2 import PdfReader


def wget_download_page(url, file_name):
    path = "tmp/"+file_name
    delete_file(path)
    wget.download(url, path)
    return path


def convert_pdf(file):
    # creating a pdf reader object
    reader = PdfReader(file)

    # printing number of pages in pdf file
    print(len(reader.pages))

    # getting a specific page from the pdf file
    page = reader.pages[0]

    # extracting text from page
    text = page.extract_text()
    print(text)
    return text


def save_txt(textfile, text):
    filepath = "tmp/"+textfile
    delete_file(filepath)
    savefile = open(filepath, "w")
    savefile.write(text)
    savefile.close()


def delete_file(file):
    if os.path.isfile(file):
        os.remove(file)



def download_file(url: str,name):

    return