# Calculer un age à partir de la date de naissance

import datetime

print("=== Je vais calculer votre âge à partir de votre date de naissance. ===")
print()

today = datetime.date.today()
year = today.year
birth = int(input("Veuillez saisir votre année de naissance (Appuyez sur 'Entrée' pour valider) : "))

print()
print(f"Vous avez {year-birth} ans.")