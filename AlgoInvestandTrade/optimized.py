import time

from utils import lecture_des_donnees_importees


def algo_optimized(data: list[list[str]]) -> tuple[float, list]:
    """
    ALgorithme optimisé permettant de parcourir une liste de données
    dans une matrice et d'en ressortir les meilleures combinaisons
    possibles. Sachant qu'une action a un nom, un prix et un bénéfice.
    L'algorithme calcule également le profit d'une action.
    :param data: liste d'actions
    :return: meilleur_profit, liste_actions_combinaisons:
    """
    budget_portefeuille = 500

    matrice = [
        [0 for x in range(budget_portefeuille * 100 + 1)] for x in range(len(data) + 1)
    ]

    for i in range(1, len(data) + 1):
        price = float(data[i - 1][1]) * 100
        profit = price * float(data[i - 1][2]) / 100
        for w in range(1, budget_portefeuille * 100 + 1):
            try:
                if i == 0 or w == 0:
                    matrice[i][w] = 0
                elif price <= w:
                    matrice[i][w] = max(
                        profit + matrice[i - 1][int(w - price)], matrice[i - 1][w]
                    )
                else:
                    matrice[i][w] = matrice[i - 1][w]
            except Exception:
                matrice[i][w] = matrice[i - 1][w]
                continue

    n = len(data)
    liste_actions_combinaisons = []
    cout = 0
    budget = 500 * 100

    while n >= 0 and budget >= 0:
        action = data[n - 1]
        price = float(action[1]) * 100
        profit = price * float(action[2]) / 100
        if (
            matrice[n][budget] == matrice[n - 1][int(budget - price)] + profit
            and price > 0
        ):
            cout += float(action[1])
            liste_actions_combinaisons.append(action[0])
            budget -= int(price)
        n -= 1

    meilleur_profit = matrice[-1][-1] / 100

    return cout, meilleur_profit, liste_actions_combinaisons


def main():
    """
    Permet d'afficher dans le terminal les résultats de l'algorithme optimisé.
    """
    data = lecture_des_donnees_importees()
    start = time.time()
    print("\n en cours de chargement")
    cout, meilleur_profit, liste_actions_combinaisons = algo_optimized(data)
    print("la liste des combinaisons d'actions :", liste_actions_combinaisons)
    print("le meilleur profit est :", round(meilleur_profit, 2), "€")
    print("le coût total des actions est de :", round(cout, 2), "€")
    stop = time.time()
    temps = stop - start
    print("temps d'éxecution :", round(temps, 2), "secondes")


main()
