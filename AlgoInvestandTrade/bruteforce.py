import csv

# Algorithme
# Algorithme suggestion liste d'actions les plus rentables (condition : après deux ans)
#
# DEBUT
# 	Parcours la liste des actions
# 	Parcours le prix des actions
# 	Parcours le pourcentage bénéfice après deux ans
# 	Tri par taux de bénéfice le plus elevé au plus faible
# 	Retourne les actions ayant le meilleur % de benef
# 	Renvoie la liste si % benef au dessus de 15%
# FIN

# Définition des variables

action = []
cout_par_action = []
benefice = []
toutes_les_actions = []
tous_les_cpa = []
tous_les_benefs = []


def lecture_des_donnees_importees():
    file = open('../data/actions.csv') # ouverture du fichier
    csvreader = csv.reader(file) # lecture du fichier
    rows = []   # toutes les lignes du fichier
    for row in csvreader:   # pour chaque lignes du fichier
        rows.append(row) # ajout de ligne
    file.close() # fermeture du fichier

lecture_des_donnees_importees()