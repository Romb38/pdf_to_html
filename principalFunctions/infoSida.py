# -*- coding: utf-8 -*-

import requests as rq

#Url du logo de sida info service
URL_SIDA = "https://stockagehelloassoprod.blob.core.windows.net/images/logos/sida-info-service-sis-19d0bf28197647d5abee605f02de7595.png"

def recuperationImageSidaInfoService(ImagePath):
    """Récupère les images a propos du sida sur internet et l'ajoute dans le fichier image"""

    #Téléchargement de l'image
    try :
        response = rq.get(URL_SIDA) #Récupération du fichier ONLINE
    except rq.exceptions.ConnectTimeout or rq.exceptions.ConnectionError:
        print("Error - Timeout")
        return 1
    except rq.exceptions.MissingSchema:
        print("Error - Invalid URL")
        return 1
    except :
        print("Error - Résaux insable")
        return 1

    #Import de l'image dans le fichier images_tmp
    try:
        with open(ImagePath + '-1_sidaInfo.png', 'wb') as f: #Copie du fichier dans le fichier FinalPATH
            f.write(response.content)
    except FileNotFoundError:
        print("Error - Invalide Final PATH")
        return 1
    return 0
