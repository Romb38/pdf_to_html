# -*- coding: utf-8 -*-

import treatementPDF.getPDF as gPDF
import zipFile.ZipFile as zip

from PyPDF2 import PdfReader
import re
import os


#Fonction de création du HTML

"""
Fonctionnement :
On créer la base du fichier HTML avec la borne haute et la borne basse

Pour chaque page du PDF
On récupère les images et on les stockes dans un fichier 'images_temp'
On récupère le contenu
On ajoute le tout sur le HTML

/!\ les images sont placés dans l'ordre au dessus de tout le texte /!\ 
"""

def get_page(path):
    """Renvoie la première page d'un PDF"""
    reader = PdfReader(path)
    return reader.pages[0]

def get_pages(path):
    """Renvoie la première page d'un PDF"""
    reader = PdfReader(path)
    return reader.pages

def get_nb_page(path):
    reader = PdfReader(path)
    return len(reader.pages)

def get_content(path,page):
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

def get_imageName(ImagePath):
    """Renvoie la liste des fichier présents dans PATH"""
    return os.listdir(ImagePath) #path corresspond au fichier des images
   
def traitementContent(content):
    content = replace_skipline(content)
    content = replace_url(content)
    content = replace_namedurl(content)
    return content



def create_html_file(content,images,outputName,index,FileName):
    """Fonction de création du HTML, elle utilise tout les fonction présente au dessus"""

    #Constante de bases (représente le début et la fin du doc html)
    HTML_BASE_START = "<!DOCTYPE html>\n<html lang=\"fr\">\n\t<head>\n\t\t<meta charset=\"utf-8\" />\n\t\t<title>"+ FileName[:-5] +"</title>\n\t</head>\n\t<body>\n"
    HTML_BASE_END = "\n\t</body>\n</html>"

    #Ouverture du fichier html
    f = open(outputName, "w", encoding="utf-8")
    NoAbsoluteImagePATH = "./images_tmp/" #PATH des images dans le html
    f.write(HTML_BASE_START)

    #Placement des images
    for image in images:
        f.write("\n<img src='"+ NoAbsoluteImagePATH + image + "'/><br>")
    
    #Placement du contenu
    f.write(content)

    #Fin de l'HTML
    f.write(HTML_BASE_END)
    f.close()

def pdfToHtml(argv):
    """Mise en lien du fichier PDF et de la création de l'HTML"""

    pdfInfo = gPDF.fetchPDF(argv) #récupère les infos du PDF (online/offline)
    if type(pdfInfo) != int:
        pdfPath = pdfInfo[0] #PATH du pdf, existe forcément
        FinalPATH = pdfInfo[1] #PATH du fichier de sauvegarde (+ /temp pour obtenir les fichier de sauvegarde locale)
        FinalFileName = pdfInfo[2] #Nom du fichier HTML de sortie
        TempPath = FinalPATH + "/temp" #PATH vers le fichier temp
        ImagePath = TempPath + "/images_tmp/" #PATH vers le fichier des images
        
        os.mkdir(ImagePath) #Création du fichier contenant les images

        
        pages = get_pages(pdfPath) #Liste des pages du documents PDF

        for i,page in enumerate(pages): #Pour chaque page
            
            #Mise en place du contenu dans la page HTML
            content = get_content(pdfPath,page)
            content = traitementContent(content)

            create_image(page,ImagePath,i)
            images = get_imageName(ImagePath)
            create_html_file(content,images,TempPath+"/"+ FinalFileName,i,FinalFileName)
        
        zip.createFile(FinalPATH,FinalFileName) #Crée l'archive finale
        gPDF.suppTempFile(FinalPATH) #Enleve les fichier temporaire créé durant l'algo
    return 0