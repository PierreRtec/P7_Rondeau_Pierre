import time

from utils import lecture_des_donnees_importees

PORTEFEUILLE = 500

def algo_optimized(data):

    budget_portefeuille = 500

    matrice = [[0 for x in range(budget_portefeuille * 100 + 1)] for x in range(len(data) + 1)]

    for i in range(1, len(data) + 1):
        price = float(data[i - 1][1]) * 100
        profit = price * float(data[i - 1][2]) / 100
        for w in range(1, budget_portefeuille * 100 + 1):
            try:
                if i == 0 or w == 0:
                    matrice[i][w] = 0
                elif price <= w:
                    matrice[i][w] = max(
                        profit
                        + matrice[i - 1][int(w - price)],
                        matrice[i - 1][w]
                    )
                else:
                    matrice[i][w] = matrice[i - 1][w]
            except:
                matrice[i][w] = matrice[i - 1][w]
                continue

    n = len(data)
    # tant qu'il y a des actions avec un profit supérieur à une valeur
    # ajouter ces actions dans une liste*
    actions_profit = matrice[n][budget_portefeuille * 100] / 100
    liste_des_meilleures_actions = []

    while actions_profit >= 15.00 and budget_portefeuille >= 0:
        actions_profit.append(liste_des_meilleures_actions)

    return liste_des_meilleures_actions

# actions les plus rentables = celles aux taux de profit supérieur ou égal à 15

# objectif >>> récup actions les plus rentables sur 2 ans donc par exemple
# liste = [action 1, action 2, action 3] <- sensé être les plus rentables

def main():
    data = lecture_des_donnees_importees()
    start = time.time()
    print("\n resultat")
    stop = time.time()
    print(algo_optimized(data))

main()