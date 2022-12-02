# -*- coding: utf-8 -*-

from shutil import copy
import os

def fichierOffline(filePATH,FinalPATH):
    """Renvoie le fichier PDF en OFFLINE"""

    try : #On a le path au complet
        copy(filePATH, FinalPATH + "/temp.pdf")
    except FileNotFoundError:
        try : #On a juste le nom du fichier, il faut donc rajouter le chemin jusqu'a la racine 
            copy(os.getcwd() + filePATH, FinalPATH + "/temp.pdf")
        except FileNotFoundError:
            print("Error - Le fichier n'a pas été trouvé")
            return 1

    print("File correctly copied !")
    return FinalPATH + "/temp.pdf"