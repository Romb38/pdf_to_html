# -*- coding: utf-8 -*-

import requests as rq

def fichierOnline(FinalPATH,URL = ""):
    """Copie le fichier PDF présent dans l'URL dans le fichier FinalPath"""
    if not(URL):
        print("Error - URL missing to fetch online pdf")
        return 1

    try :
        response = rq.get(URL) #Récupération du fichier ONLINE
    except rq.exceptions.ConnectTimeout or rq.exceptions.ConnectionError:
        print("Error - Timeout")
        return 1
    except rq.exceptions.MissingSchema:
        print("Error - Invalid URL")
        return 1
    except :
        print("Error - Résaux insable")
        return 1

    try:
        with open(FinalPATH + '/temp.pdf', 'wb') as f: #Copie du fichier dans le fichier FinalPATH
            f.write(response.content)
    except FileNotFoundError:
        print("Error - Invalide Final PATH")
        return 1
    
    print("Success : PDF file correctly copied !")
    return FinalPATH + "/temp.pdf"



