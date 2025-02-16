#Exercice1
from random import randint

de = 0
tortue = 0
list_de = []

while (de < 6) and (tortue < 6) :
    de = randint(1,6)
    list_de.append(de)
    if de != 6:
        tortue += 1
        print("la tortue est à :",tortue)

print("Liste des résultats :",list_de)
if de == 6:
    print("le lièvre a gagné")
else:
    print("la tortue a gagné")


#Exercice 2
n=10
liste_gagnants = []
lievre_gagne = 0

for i in range(n):
    de = 0
    tortue = 0
    list_de = []

    while (de < 6) and (tortue < 6) :
        de = randint(1,6)
        list_de.append(de)
        if de != 6:
            tortue += 1

    print("Liste des résultats :",list_de)
    if de == 6:
        print("le lièvre a gagné")
        lievre_gagne += 1
        liste_gagnants.append('lievre')
    else:
        print("la tortue a gagné")
        liste_gagnants.append('tortue')

print("Résultats :",liste_gagnants)
print('la fréquence que le lièvre gagne est de :',lievre_gagne,'sur',n,'parties')