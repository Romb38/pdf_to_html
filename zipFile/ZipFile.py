# -*- coding: utf-8 -*-

import os
import shutil


def createFile(FinalPATH,FinalFileName):
    """Copie le fichier HTML ainsi que les images correspondantes dans un fichier puis le compresse et renvoie le PATH vers l'archive"""
    FinalFile = FinalPATH + "/" + FinalFileName[:-5] + "/"

    #Création de l'archive
    os.mkdir(FinalFile)

    #Copie des fichiers
    shutil.move(FinalPATH + "/temp/" + FinalFileName, FinalFile)
    shutil.move(FinalPATH + "/temp/images_tmp",FinalFile)
    shutil.move(FinalPATH + "/temp/temp.pdf", FinalFile + FinalFileName[:-5] + ".pdf")

    #Compression du fichier obtenu
    shutil.make_archive(FinalPATH + "/" + FinalFileName[:-5],"zip",FinalFile)

    #Suppression fichier temporaire
    shutil.rmtree(FinalFile[:-1])