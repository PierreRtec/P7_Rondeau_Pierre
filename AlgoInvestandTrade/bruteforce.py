import itertools
from utils import lecture_des_donnees_importees

def algo_brute():
    highest_benef = 0
    best_combinaison = None
    portefeuille = 500
    rows = lecture_des_donnees_importees()
    for i in range(len(rows)):
        for combinaison in itertools.combinations(rows, i):
            total_prix = 0
            total_gains = 0
            for action in combinaison:
                total_prix += float(action[1])
                total_gains += (float(action[1]) * float(action[2])) / 100
            if total_prix <= portefeuille and total_gains > highest_benef:
                best_combinaison = combinaison
                highest_benef = total_gains
    print(round(highest_benef, 2))
    print(best_combinaison)

algo_brute()