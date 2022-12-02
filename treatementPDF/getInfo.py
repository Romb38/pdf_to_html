# -*- coding: utf-8 -*-
from os.path import isdir

def getInfoPdfOnline(argv,i):
    """Récupère les informations du PDF pour la version online"""
    URL = ""
    try :
        if argv[i+1][0] != "-": #On récuoère le nom du fichier pdf (format <NameFile>.pdf) (si disponible)
            URL = argv[i+1]
        else:
            raise IndexError
    except IndexError:
        print("Error - pdf file URL is missing")
        return 1

    return URL


def getInfoPdfOffline(argv,i):
    """Récupère les infos concernant le pdf en mode OFFLINE"""
    PathFile = "/"
    try :
        if argv[i+1][0] != "-": #On récuoère le nom du fichier pdf (format <NameFile>.pdf) (si disponible)
            PathFile = argv[i+1]
    except IndexError:
        print("Error - PDF file is missing")
        return 1
    
    return PathFile


def getFinalPath(argv,i):
    """Renvoie le PATH dans lequel l'archive finale est stockée"""
    FinalPATH = "/"
    try :
        if argv[i+1][0] != "-": #On récuoère le nom du fichier pdf (format <NameFile>.pdf) (si disponible)
            FinalPATH = argv[i+1]
        else :
            raise IndexError
        
        if not(isdir(FinalPATH)):
            print("Error - Final PATH is not pointing on a valid directory")
            return 1

    except IndexError:
        print("Error - Final PATH is missing")
        return 1

    return FinalPATH

def getName(argv,i):
    """Renvoie le nom du fichier HTML"""
    FinalFileName = ""
    try:
        if argv[i+1][0] != "-":
            FinalFileName = argv[i+1]
        else:
            raise IndexError
        
        if FinalFileName[-4:] != ".html": #On vérifie que le name contient l'extention html
            FinalFileName += ".html" #Sinon on la rajoute
    except IndexError:
        print("Error - Enter a valid file name")
        return 1
    return FinalFileName