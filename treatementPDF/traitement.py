# -*- coding: utf-8 -*-

def prepaFilePath(FilePath): 
    """Ajoute l'extension .pdf sur le nom de fichier si besoin"""
    if FilePath[-4:] != ".pdf":
        FilePath += ".pdf"
    return FilePath