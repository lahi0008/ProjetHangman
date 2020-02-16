# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 11:37:26 2020

@author: Abdoulahi MBENGUE
"""
from random import *

def lettre_dans_mot(lettre,mot_a_trouver):
    positions=[]
    position_actuelle=0
    for lettre_mot in mot_a_trouver:
        if lettre_mot==lettre:
            positions.append(position_actuelle)
        position_actuelle+=1
        
    return positions

def affiche_lettres_trouvees(positions,mot_a_trouver):
    
    mot_a_afficher=" "
    
    position_actuelle=0
    
    for lettre_mot in mot_a_trouver:
        if position_actuelle in positions :
            mot_a_afficher+=lettre_mot
        else:
            mot_a_afficher+='-'
        position_actuelle+=1
    return mot_a_afficher

def choisir_mot(nom_fichier):
    liste_de_mots=[]
    fichier=open(nom_fichier,"r")
    for ligne in fichier:
        ligne=ligne.strip("\n")
        liste_de_mots.append(ligne)
    shuffle(liste_de_mots)
    mot_a_trouver=liste_de_mots[0]
    
    
    return mot_a_trouver
    

print("BIENVENUE DANS LE JEU DU HANGMAN")
niveau=int(input("Veuillez choisir un niveau (entre 1 et 3) pour commencer " ))
while niveau <1 or niveau >3:
    niveau=int(input("Veuillez choisir un niveau (entre 1 et 3 )!"))
if niveau==1:
    print("Vous avez choisi le Niveau 1")
    print("Je pense à un mot de 5 lettres au maximum, à vous de deviner.")
    mot_a_trouver=choisir_mot("mots5.txt")
    a=len(mot_a_trouver)
    b=0
    positions_tout=[]
    print(mot_a_trouver)
    essais=0
    lettres_trouvees=[]
    pendaison=['''
        +---+
        |   |
            |
            |
            |
            |
    ===========''','''
        +---+
        |   |
        O   |
            |
            |
            |
    ===========''' , '''
        +---+
        |   |
        O   |
       /    |
            |
            |
    ===========
    ''',
    '''
        +---+
        |   |
        O   |
       /|   |
            |
            |
    ===========
    ''',
    '''
        +---+
        |   |
        O   |
       /|\  |
            |
            |
    ===========
    ''',
    '''
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
    ===========
    ''',
    '''
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
    ===========
    ''']
    if a!=b:
        while essais<6:
        
            lettre_joueur=input( "Entrer une lettre: " )
            while lettre_joueur in lettres_trouvees:
                lettre_joueur=input( " Vous avez deja fait ce choix. Entrer une lettre à nouveau: " )
            lettres_trouvees.append(lettre_joueur)
            positions_actuelle=lettre_dans_mot(lettre_joueur,mot_a_trouver)
            if positions_actuelle==[]:
                essais+=1
                """ print(essais)""" 
            positions_tout+=positions_actuelle
            mot_a_afficher=affiche_lettres_trouvees(positions_tout,mot_a_trouver)
            b=len(mot_a_afficher)
            print(mot_a_afficher)
            print(pendaison[essais])
        
        if essais==6:
            print( "VOUS ETES PENDU !" )
            print("voici le MOT SECRET "+ str(mot_a_trouver))
            a==b
            
if niveau==2:
    print("Vous avez choisi le Niveau 2")
    print("Je pense à un mot de 8 lettres au maximum, à vous de deviner.")
    mot_a_trouver=choisir_mot("mots8.txt")
    positions_tout=[]
    print(mot_a_trouver)
    essais=0
    lettres_trouvees=[]
    pendaison=['''
        +---+
        |   |
            |
            |
            |
            |
    ===========''','''
        +---+
        |   |
        O   |
            |
            |
            |
    ===========''' , '''
        +---+
        |   |
        O   |
       /    |
            |
            |
    ===========
    ''',
    '''
        +---+
        |   |
        O   |
       /|   |
            |
            |
    ===========
    ''',
    '''
        +---+
        |   |
        O   |
       /|\  |
            |
            |
    ===========
    ''',
    '''
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
    ===========
    ''',
    '''
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
    ===========
    ''']

    while essais<6:
        lettre_joueur=input( "Entrer une lettre: " )
        while lettre_joueur in lettres_trouvees:
            lettre_joueur=input( " Vous avez deja fait ce choix. Entrer une lettre à nouveau: " )
        lettres_trouvees.append(lettre_joueur)
        positions_actuelle=lettre_dans_mot(lettre_joueur,mot_a_trouver)
        if positions_actuelle==[]:
            essais+=1
            """ print(essais)""" 
        positions_tout+=positions_actuelle
        mot_a_afficher=affiche_lettres_trouvees(positions_tout,mot_a_trouver)
        print(mot_a_afficher)
        print(pendaison[essais])
        if mot_a_afficher==mot_a_trouver:
            print( " vous avez gagné " )
            exit()
    if essais==6:
        print( "VOUS ETES PENDU !" )
        print("Voici le MOT SECRET "+ str(mot_a_trouver))

if niveau==3:
    print("Vous avez choisi le Niveau 3")
    print("Je pense à un mot de 10 lettres ou plus, à vous de deviner.")
    mot_a_trouver=choisir_mot("mots10p.txt")
    positions_tout=[]
    print(mot_a_trouver)
    essais=0
    lettres_trouvees=[]
    pendaison=['''
        +---+
        |   |
            |
            |
            |
            |
    ===========''','''
        +---+
        |   |
        O   |
            |
            |
            |
    ===========''' , '''
        +---+
        |   |
        O   |
       /    |
            |
            |
    ===========
    ''',
    '''
        +---+
        |   |
        O   |
       /|   |
            |
            |
    ===========
    ''',
    '''
        +---+
        |   |
        O   |
       /|\  |
            |
            |
    ===========
    ''',
    '''
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
    ===========
    ''',
    '''
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
    ===========
    ''']

    while essais<6:
        lettre_joueur=input( "Entrer une lettre: " )
        while lettre_joueur in lettres_trouvees:
            lettre_joueur=input( " Vous avez deja fait ce choix. Entrer une lettre à nouveau: " )
        lettres_trouvees.append(lettre_joueur)
        positions_actuelle=lettre_dans_mot(lettre_joueur,mot_a_trouver)
        if positions_actuelle==[]:
            essais+=1
            """ print(essais)""" 
        positions_tout+=positions_actuelle
        mot_a_afficher=affiche_lettres_trouvees(positions_tout,mot_a_trouver)
        print(mot_a_afficher)
        print(pendaison[essais])
        if mot_a_afficher==mot_a_trouver :
            print( " vous avez gagné " )
            exit()
    if essais==6:
        print( "VOUS ETES PENDU !" )
        print("voici le MOT SECRET :"+ str(mot_a_trouver))

    
        