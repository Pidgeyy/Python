# Créé par Joshua, le 02/12/2024 en Python 3.7
#EXERCICE 1
#Demande les données à l'utilisateur
naissance = int(input("Mettez votre année de naissance: "))
annee_actuelle = int(input("Année actuelle: "))

if naissance < annee_actuelle: #vérifie si l'âge n'est pas négatif
    age = annee_actuelle - naissance #calcul l'age
    print("vous avez entre ",naissance," et ",str(annee_actuelle),", ",age)
else:
    print("vous n'êtes pas encore né")


#EXERCICE 2
#Demande les données à l'utilisateur
distance= float(input("Distance parcourue en km: "))
temps = float(input("Temps pour parcourir cet distance en heure: "))

vitesse = distance / temps #calcul la vitesse
print("Vitesse: ",vitesse,"km/h")


#EXERCICE 3
#Défini les variables
chiffres = int(input("Insérez une suite de 3 chiffres: "))
somme = 0

#Parcour la suite
while chiffres > 0:
    somme += chiffres % 10
    chiffres //= 10
print(somme)
