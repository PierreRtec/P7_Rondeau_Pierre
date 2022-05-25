import csv
import itertools

def lecture_des_donnees_importees():
    file = open('../data/dataset1_Python+P7.csv') # ouverture du fichier
    csvreader = csv.reader(file) # lecture du fichier
    rows = []   # toutes les lignes du fichier
    for row in csvreader:   # pour chaque lignes du fichier
        rows.append(row) # ajout de ligne
    file.close() # fermeture du fichier

    return rows[1:]

lecture_des_donnees_importees()

def algo_brute():
    highest_benef = 0
    best_combinaison = None
    portefeuille = 500
    rows = lecture_des_donnees_importees()
    for i in range(len(rows)):
        for combinaison in itertools.combinations(rows, i):
            print(combinaison)
            total_prix = 0
            total_gains = 0
            for action in combinaison:
                total_prix += float(action[1])
                total_gains += float(action[1]) * float(action[2])
            if total_prix <= portefeuille and total_gains > highest_benef:
                best_combinaison = combinaison
                highest_benef = total_gains
    print(highest_benef)
    print(best_combinaison)

algo_brute()