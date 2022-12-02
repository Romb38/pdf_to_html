# -*- coding: utf-8 -*-

import treatementPDF.getPDF as gPDF
import zipFile.ZipFile as zip
import principalFunctions.infoSida as iS

import os
import principalFunctions.HtmlFunc as HTMLf

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



   


def create_html_file(outputName,FileName,PDFPath,ImagePath):
    """Fonction de création du HTML, elle utilise tout les fonction présente au dessus"""

    #Constante de bases (représente le début et la fin du doc html)
    HTML_BASE_START = "<!DOCTYPE html>\n<html lang=\"fr\">\n\t<head>\n\t\t<meta charset=\"utf-8\" />\n\t\t<title>"+ FileName[:-5] +"</title>\n\t</head>\n\t<body>\n"
    HTML_BASE_END = "\n\t</body>\n</html>"

    #Ouverture du fichier html
    f = open(outputName, "w", encoding="utf-8")
    NoAbsoluteImagePATH = "./images_tmp/" #PATH des images dans le html
    f.write(HTML_BASE_START)
    f.write("\n<img src='"+ NoAbsoluteImagePATH + "-1_sidaInfo.png' width=10% heigth=10%/><br>Numero Sida Infos Service : 0 800 84 800<br>Site : <a href =https://www.sida-info-service.org>https://www.sida-info-service.org</a><br>Nuit de l'info 2022<br><br><br>===========PDF===========<br><br><br><br>")


    pages = HTMLf.get_pages(PDFPath) #Liste des pages du documents PDF

    for i,page in enumerate(pages): #Pour chaque page
        
        
        #Création des fichier pour les images contenus sur la page
        HTMLf.create_image(page,ImagePath,i)
        images = HTMLf.get_imageName(ImagePath)



        #Placement des images dans le html
        for image in images:
            if HTMLf.get_index(image) == i:
                f.write("\n<img src='"+ NoAbsoluteImagePATH + image + "'/><br>")
    

        #Récupération du contenu textuel du PDF
        content = HTMLf.get_content(page)
        content = HTMLf.traitementContent(content)

        #Placement du contenu
        f.write(content)

    #Fin de l'HTML
    f.write(HTML_BASE_END)
    f.close()

def pdfToHtml(argv):
    """Mise en lien du fichier PDF et de la création de l'HTML"""

    pdfInfo = gPDF.fetchPDF(argv) #récupère les infos du PDF (online/offline)
    if type(pdfInfo) != int:
        PDFPath = pdfInfo[0] #PATH du pdf, existe forcément
        FinalPATH = pdfInfo[1] #PATH du fichier de sauvegarde (+ /temp pour obtenir les fichier de sauvegarde locale)
        FinalFileName = pdfInfo[2] #Nom du fichier HTML de sortie
        TempPath = FinalPATH + "/temp" #PATH vers le fichier temp
        ImagePath = TempPath + "/images_tmp/" #PATH vers le fichier des images
        
        os.mkdir(ImagePath) #Création du fichier contenant les images

        iS.recuperationImageSidaInfoService(ImagePath)

        create_html_file(TempPath+"/"+ FinalFileName,FinalFileName,PDFPath,ImagePath)
        
        zip.createFile(FinalPATH,FinalFileName) #Crée l'archive finale
        gPDF.suppTempFile(FinalPATH) #Enleve les fichier temporaire créé durant l'algo
    return 0