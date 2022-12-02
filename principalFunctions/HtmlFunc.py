# -*- coding: utf-8 -*-

from PyPDF2 import PdfReader
import re
import os


def get_imageName(ImagePath):
    """Renvoie la liste des fichier présents dans PATH"""
    return os.listdir(ImagePath) #path corresspond au fichier des images

def get_pages(path):
    """Renvoie la première page d'un PDF"""
    reader = PdfReader(path)
    return reader.pages

def get_nb_page(path):
    reader = PdfReader(path)
    return len(reader.pages)

def get_content(page):
    """Renvoie le texte d'une page PDF"""
    return page.extract_text()

def replace_skipline(line):
    """Renmplace les \n par des <br>"""
    return re.sub('\n', "<br>", line)

def replace_url(line):
    """Modifie les URLS par des les balises HTML correspondante"""
    return re.sub(r'((http|https|ftp)://[a-zA-Z0-9\./]+)', r'<a href="\1">\1</a>', line)

def replace_namedurl(line):
    """Remplace les URLs du PDF par des hyperlien"""
    return re.sub("\[(.*) (.*)\]", "<a href='\\2'>\\1</a>", line)

def create_image(page,ImagePath,indexPage):
    """Crée les images venue du PDF dans le file /temp/images_tmp"""
    count=0
    for image_file_object in page.images:
        with open(ImagePath + str(indexPage) + "_" + str(count) + image_file_object.name, "wb") as fp:
            fp.write(image_file_object.data)
            count += 1

def traitementContent(content):
    """Renvoie le contenu textuel d'une page"""
    content = replace_skipline(content)
    content = replace_url(content)
    content = replace_namedurl(content)
    return content


def get_index(image):
    """Récupère l'index dans un nom de fichier au format <index>_<fileName>"""
    i = 0
    while image[i] != "_":
        i += 1
    return int(image[:i])