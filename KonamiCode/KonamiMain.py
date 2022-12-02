# -*- coding: utf-8 -*-

# 3 - = 1 case
# Jeu [0,6]

from random import randint

LARGEUR_PLATEAU = 7
HAUTEUR_PLATEAU = 6

def rules():
    """Affichage des règles"""
    print("============================")
    print("Welcome in our Space Invaders - Konami Code Edition")
    print("Your goal is simple : Destroy all your ennemis")
    print("You can move :")
    print("- l/g for left and rigth")
    print("- a/b to shoot")
    print("- u/d for up and down. That teleports you to the side of the game")
    print("- q to quit (So sad...)")
    print("Edge are wall ! Be careful !")
    print("============================\n\n ")


def showGame(jeu,x):
    """Affiche le jeu actuel"""
    for i in range(0,HAUTEUR_PLATEAU):
            print("".join(jeu[i]))

    print("\n")
    
    chn = ""
    for i in range(0,LARGEUR_PLATEAU):
        if i == x:
            chn += "-A-"
        else:
            chn += "---"
    print(chn)


def initJeu(jeu):
    """Initialise le jeu en début de partie"""
    for i in range(0,HAUTEUR_PLATEAU//2  ):
        for j in range(0,LARGEUR_PLATEAU):
            jeu[i][j] = " X "

def move(c,x):
    """Déplace le joueur vers la gauche ou la droite"""
    deplacement = 0
    if c == 'r' and x < HAUTEUR_PLATEAU:
        deplacement = 1
    elif c == 'l' and x > 0:
        deplacement = -1
    elif c == "u":
        deplacement = HAUTEUR_PLATEAU - x
    elif c == "d":
        deplacement = -x
    return x + deplacement

def shoot(jeu,x):
    """Génère le tir du vaisseau"""
    flag = False
    i = HAUTEUR_PLATEAU -1
    while i!= -1 and not(flag):
        if jeu[i][x] == " X ":
            jeu[i][x] = "   "
            flag = True
        i-=1
    return 0

def victory(jeu):
    """Renvoie True si il n'y a plus d'ennemis sur le terrain"""
    win = True
    i = 0
    while i !=HAUTEUR_PLATEAU and win:
        j = 0
        while j != LARGEUR_PLATEAU and win:
            win = (jeu[i][j] != " X ")
            j += 1
        i+= 1
    return win

def inputMove():
    """Gestion de l'erreur de l'entrée des mouvements"""
    try :
        movement = input("Move (l/r/a/b/u/d/q): ")
        if not(movement in ['l','r','a','b','u','d','q']):
            raise ValueError
    except :
        print("Bad key ! You lost a chance ...")
        movement = ""

    return movement


def down(jeu,hauteurActuelle):
    """Fait descendre le jeu de temps en temps et dit si on a perdu ou non"""
    if hauteurActuelle + 1 >= HAUTEUR_PLATEAU:
        return True,hauteurActuelle
    else :
        hauteurActuelle = hauteurActuelle + 1
        for i in range(hauteurActuelle,-1,-1):
            jeu[i] = jeu[i-1]
        jeu[0] = [" X " for k in range(0,LARGEUR_PLATEAU)]
        return False, hauteurActuelle

def konamiHandle(saveInput,m):
    """Handle the list of input"""
    if len(saveInput)<10:
        saveInput.append(m)
    
    for i in range(len(saveInput)-1,0,-1):
        saveInput[i] = saveInput[i-1]
    saveInput[0] = m
    

def main():
    #Affichage des règles
    rules()

    #Variables de jeu
    jeu = [[" " for i in range (LARGEUR_PLATEAU)] for j in range(HAUTEUR_PLATEAU)]
    posJoueur = 3 #Position de départ
    saveInput = []
    KonamiInput = ["u","u","d","d","l","r","l","r","b","a"]
    konamiFlag = False
    compt = 0
    chute = randint(4,6)
    hauteurActuelle = 3
    perdu = False

    #Initialisation
    initJeu(jeu)
    showGame(jeu,posJoueur)

    movement = inputMove()

    while movement != 'q' and not(victory(jeu)) and not(konamiFlag) and not(perdu):
        
        #Gestion du code Konami
        if movement != "":
            konamiHandle(saveInput,movement)
        
        if saveInput == KonamiInput[::-1]:
            konamiFlag = True

        #Descente des vaisseaux
        if compt == chute:
            perdu,hauteurActuelle = down(jeu,hauteurActuelle)
            chute = randint(4,6)
            compt = 0

        #Gestion des mouvements
        if movement in ['l','r','u','d'] :
            posJoueur = move(movement,posJoueur)
        elif movement:
            shoot(jeu,posJoueur)

        #Affichage du jeu
        showGame(jeu,posJoueur)

        #Tour suivant en cas de non victoire
        if not(victory(jeu)) and not(konamiFlag):
            compt += 1
            movement = inputMove()

    #Victoire !
    if konamiFlag : 
        print("Booom, you have destroyed the game and create a KONAMICEPTION")
    elif victory(jeu):
        print("Good game, you win !")
    elif perdu:
        print("Sad, you lose ...")
    else :
        print("Goodbye !")

    return 1



if __name__ == "__main__":
    main()
