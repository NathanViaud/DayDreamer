# Créé par heyda, le 21/03/2016 en Python 3.2

import os
global listeCollision, listeCollisionAction
global n, n2
global fichierNiveau, fichierNiveau2
listeCollisionAction = []
listeCollision = []     #définition et globalisation des variables nécessaires au programme


def charger(niveau): #fonction qui va permettre de définir l'adresse et le nom du fichier à charger
    global adresse, adresse2
    if niveau == 0:
        adresse = "data/coordonnees/mort.txt"
        adresse2 = "data/coordonnees/mortA.txt"
        print("mort")
    if niveau == 1:
        adresse = "data/coordonnees/niveau1.txt"
        adresse2 = "data/coordonnees/niveau1A.txt"
        print("maison chargée")
    elif niveau == 2:
        adresse = "data/coordonnees/niveau2.txt"
        adresse2 = "data/coordonnees/niveau2A.txt"
        print("allée chargée")
    elif niveau == 3:
        adresse = "data/coordonnees/niveau3.txt"
        adresse2 = "data/coordonnees/niveau3A.txt"
    elif niveau == 4:
        adresse = "data/coordonnees/niveau4.txt"
        adresse2 = "data/coordonnees/niveau4A.txt"
    elif niveau == 5:
        adresse = "data/coordonnees/niveau5.txt"
        adresse2 = "data/coordonnees/niveau5A.txt"
    obtentionligne()
    init()
def obtentionligne(): #fonction qui va permettre d'obtenir le nombre de ligne présentent dans le fichier txt
    global n, n2
    fichierNiveau = open(adresse,"r")
    fichierNiveau2 = open(adresse2,"r")
    n=0
    n2 = 0
    for line in fichierNiveau:
        n=n+1
    for line in fichierNiveau2:
        n2=n2+1

def init(): #fonction qui va lancer l'aquisition des valeurs de chaque lignes du fichier
    obtentionligne()
    fichierNiveau = open(adresse,"r")
    fichierNiveau2 = open(adresse2, "r")
    listeCollision[:] = []
    listeCollisionAction[:] = []

    for i in range(n): #fonction qui va répeter l'acquisition en fonction du nombre de ligne
        listeCollision.append( int((fichierNiveau.readline()))) #aquisition de la valeur de la ligne et insertion dans une liste
        print (listeCollision)

    for i in range(n2):
        listeCollisionAction.append( int((fichierNiveau2.readline())))
        print (listeCollisionAction)