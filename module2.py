# Créé par Joshua, le 09/12/2024 en Python 3.7

#EXERCICE 1:
nombre = int(input("Inserez un nombre entier: "))
if nombre % 2 == 0:
    print("Nombre pair")
else:
    print("nombre impair")

#EXERCICE 2:
#matière de l'eau
temperature = float(input("Inserez la temperature de la matière: "))
if temperature >= 100:
    print("matière sous état gazeux")
elif 0 < temperature < 100:
    print("matière sous état liquide")
else:
    print("matière sous état solide")