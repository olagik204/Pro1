from itertools import product

nombre_de_des = 5
somme_cible = 20

combinaisons = product(range(1, 7), repeat=nombre_de_des)

compte = sum(1 for combinaison in combinaisons if sum(combinaison) == somme_cible)

print(f"Nombre de façons d'obtenir {somme_cible} avec {nombre_de_des} dés : {compte}")
