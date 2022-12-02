# -*- coding: utf-8 -*-

#Bibliothèque système (récupération d'arguments)
import os
from shutil import rmtree

import treatementPDF.getInfo as gtI
import treatementPDF.pdfOnline as pdfOn
import treatementPDF.pdfOffline as pdfOff
import treatementPDF.traitement as t
import KonamiCode.KonamiMain as kon

def fetchPDF(argv):
    """Retourne le fichier pdf récuperée online/offline grâce aux arguements de la fonction"""

    if "UpUpDownDownLeftRigthLeftRigthBA" in argv or "HautHautBasBasGaucheDroiteGaucheDroiteBA" in argv:
        kon.main()

    pdf = None #Cette variable contiendra le fichier pdf récupéré en sortie
    FinalPATH = os.getcwd()
    typeFetch = 0 #On a bien les bons arguments dans la commande
    FinalFileName = "pdfToHTML_Result.html" #Nom final du fichier html (valeur par défaut)

    if not('-o') in argv and not('-f') in argv and not('-h') in argv:
        print("Error - Indicate fetch file methode (-f/-o) - See README for more informations")
        return 1

    for i in range(len(argv)):
        val = argv[i]
        if val == '-f' and not(typeFetch): #Le ficher est présent sur la machine
        
            FilePath = gtI.getInfoPdfOffline(argv,i)

            if FilePath == 1: #Gestion de l'erreur
                return 1

            typeFetch = 1

        elif val == '-o' and not(typeFetch): #On récupère le fichier en ligne
            
            URL = gtI.getInfoPdfOnline(argv,i)

            if URL == 1: #Gestion de l'erreur
                return 1
        
            typeFetch = 2
            
        elif val == '-p': #On récupère le PATH final de stockage
            FinalPATH = gtI.getFinalPath(argv,i)
            if FinalPATH == 1:
                return 1
        
        elif val == '-n': #On récupère le nom du fichier final
            FinalFileName = gtI.getName(argv,i)
            if FinalFileName == 1:
                return 1
        
        elif val == '-h': #Affiche le READ.Me
            RM = open("README.md")
            print(RM.read())
            return -1

    tempFilePath = FinalPATH + "/temp" #Chemin du fichier temporaire

    try :
        os.mkdir(tempFilePath)
    except FileExistsError:
        print("Error - name 'temp' is already taken by a folder")
        return 1


    if typeFetch == 1 and type(FinalPATH)!= int and type(FinalFileName)!=int:
        pdf = pdfOff.fichierOffline(t.prepaFilePath(FilePath),tempFilePath)
    elif typeFetch == 2 and type(FinalPATH)!= int and type(FinalFileName)!=int:
        pdf = pdfOn.fichierOnline(tempFilePath,URL)

    
    if not(typeFetch) :
        print ("Error - Specify PDF file with -f or -o")
        return 1,1
    return [pdf,FinalPATH,FinalFileName]


def suppTempFile(FinalPath):
    fileTempPath = FinalPath + "/temp"
    rmtree(fileTempPath)
    print("Success : temp file remove")
    return 0