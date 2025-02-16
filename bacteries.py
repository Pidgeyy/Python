# Créé par Joshua, le 06/01/2025 en Python 3.7
seuil = int(input("Définir le seuil(nombre de bactéries max): "))
heures = 0
nombre_bacteries = 10

while nombre_bacteries < seuil:
    heures += 1
    nombre_bacteries *= 1.25
print("Il faut ",heures,"h pour atteindre le seuil")


#ICEBERG
seuil = 1
jours = 0
masse = 10

while masse > seuil:
    jours += 1
    masse *= 0.9
print("Il faut ",jours,"jours pour atteindre le seuil")

#CARRE PARFAIT
nombre_initial = int(input("Saisir nombre: "))

#version boucle FOR
for i in range(nombre_initial+1):
    carre_parfait = i**2
    if carre_parfait < nombre_initial:
        print(carre_parfait)

#Carré parfait
nombre = int(input("Saisir nombre: "))
i = 0
liste = []

while i**2 < nombre :
    carre_parfait = i ** 2
    i += 1
    liste.append(carre_parfait)
    print(carre_parfait)
print(liste)