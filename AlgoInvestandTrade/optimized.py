import csv
import itertools

def lecture_des_donnees_importees():
    file = open('../data/dataset1_Python+P7_echantillon_20.csv') # ouverture du fichier
    csvreader = csv.reader(file) # lecture du fichier
    rows = []   # toutes les lignes du fichier
    for row in csvreader:   # pour chaque lignes du fichier
        rows.append(row) # ajout de ligne
    file.close() # fermeture du fichier

    return rows[1:]

lecture_des_donnees_importees()

def algo_optimized():
    # algo opti
    pass





