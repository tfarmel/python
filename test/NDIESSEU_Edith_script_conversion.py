# ========================================================================================================================================
#                                       SCRIPT DE CONVERSION DU FICHIER .pkl EN .mgf
# =========================================================================================================================================
# Le fichier d'entrée contient des bouts de peptides .POur la conversion,il faut ajouter tout en maintenant les espace entre chaque peptide:
                        # 1-les chaines de caratères 'COM=' et 'CHARGE=' 
                        # 2-Un entête à chaque peptide,
                        # 3-Un  '?' en fin de chaque ligne correspondant à la colonne de la charge
                        # 4-Une balise de fin de peptide:'END POINT'
# ========================================================================================================================================
#                                                 LE SCRIPT DE CONVERSION
# ========================================================================================================================================
#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
import os
import sys

# etape 1: OUVERTURE DES FICHIERS

pkl_f = open("ex-2.pkl", "r") # j'ouvre  le fichier d'entree en mode lecture 
mgf_f= open("ex-2_file.mgf", "a") # j'ouvre le fichier de sortie dans lequel je vais écrire le fichier d'entrée et les modifications .


# etape 2: LECTURE ET ECRITURE

pkl_in = pkl_f.readlines()# je parcoure mon fichier ligne par lgine
 # j'écris le contenu du fichier d'entrée dans le fichier de sortie en ajoutant des chaines de caractère en positions 0 et 1 
mgf_f.write("COM=\n"+"CHARGE=\n"+"\n")

# etape 3: AJOUT DES ELEMENTS 
# 

# =======================================================================================================================================
#dans le fichier .pkl, j'ai des element qui sont numérotés.Cela nécessite  donc un compteur 
# les indices 0 et 1 étant déja rempli,je commence à écrire sur les lignes 
#suivantes .Pour insérer des éléments en milieu de texte,je convertie les lignes
# de fichier d'entrée en une liste temporaire constituées de sou chaines.Cela
#me permettra de reperer facilment les différentes structures de mes sous listes.
#J'ai donc 3 types de sous listes.Le premier type de sous liste contient 3 éléments
#le second contient contient 2 éléments  et le dernier type contient 1 vide.
# =======================================================================================================================================
nblignes=0# j'initialise mon compteur de lignes
for line in pkl_in[1:]: #pour tout élément  situé après les éléments d'indices 0 et 1
    if len(line.split(" ")) == 3: #si je trouve une sous liste contenant trois élément 
        nblignes+=1 # itération du compteur
# j'ajoute dans mon fichier de sortie  après chaque ligne vide
        mgf_f.write("BEGIN IONS\n"+"TITLE=ex-2.pkl."+str(nblignes)+"\nPEPMASS="+line+"CHARGE="+line.rstrip("\n").split(" ")[2]+"+\n") 
    elif len(line.split(" ")) == 2: #sinon lorsque la sous liste contient deux elements,je supprime l'espace et je remplace le vide par un ?
        mgf_f.write(line.rstrip("\n")+" ?\n")
    elif len(line.split(" ")) == 1: # ce dernier cas, j'écris la chaine de caractère 'END IONS'
        mgf_f.write("END IONS\n\n")


# etape 4: FERMETURE DES FICHIERS
#Pour visualiser le résultat, il est nécessaire que je ferme mes ficiers.

mgf_f.close()
pkl_f.close()
"""
Created on Tue Oct 31 00:04:42 2017
@author: Edith NDIESSEU
"""