# Savoir si un enfant à moins de 3 ans

import datetime

print("=== SI votre enfant à moins de 3 ans, il a le droit à une palette de petits pots. ===")
print("Quand une valeur vous est demandée, saissisez-la au clavier et appuyez sur la touche 'Entrée' pour valider.")

print()

birth = int(input("Veuillez saisir l'année de naissance de l'enfant : "))
age = datetime.date.today().year-birth

old = "ans"
if age <= 1 :
    old = "an"

print()

if age < 3 :
    print(f"Votre enfant de {age} {old} à le droit à une palette de petits pots.")
else :
    print(f"Je suis désolé, votre enfant de {age} ans est trop agé pour avoir le droit à une palette de petits pots.")