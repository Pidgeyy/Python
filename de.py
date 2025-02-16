#Créé par Joshua, le 24/01/2025 en Python 3.7
from random import randint

cpt = 0
de = 0 #valeur fictive, pour être sur de rentrer dans la boucle
liste_lancers = []

while de != 6:
    de = randint(1,6)
    liste_lancers.append(de)
    cpt += 1

print("Tu as effectué",cpt,"lancers avant d'obtenir un 6")
print("voici la liste des tentatives",liste_lancers)



somme = 0 #valeur fictive, pour s'assurer de rentrer dans la boucle
cpt = 0
de = 0

while somme <= 30:
    de = randint(1,6)
    cpt += 1
    somme += de
print("Total de points:",somme,"avec",cpt,"lancers")


de = 0 #valeur fictive
lancers = []
for _ in range(5):
    de = randint(1,6)
    lancers.append(de)
print("Voici le résultat de votre lancer",lancers)