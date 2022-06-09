import csv


def lecture_des_donnees_importees():
    try:
        file = open("../data/dataset1_Python+P7_echantillon_20.csv")
        csvreader = csv.reader(file)
        rows = []
        for row in csvreader:
            rows.append(row)
        file.close()
    except FileNotFoundError:
        print("Fichier non trouvé")

    return rows[1:]


lecture_des_donnees_importees()
