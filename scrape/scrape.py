import wget
import os


def wget_download_page(url, file_name):
    path = "tmp/"+file_name
    delete_file(path)
    response = wget.download(url, path)
    return path


def delete_file(file):
    os.remove(file)


def download_file(url: str,name):

    return