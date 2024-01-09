# Calculer la moyenne des notes d'un élève

print("=== Je vais calculer pour vous la moyenne de vos notes. ===")
print()

french = float(input("Veuillez saisir votre note de français entre 0 et 20 (Appuyez sur 'Entrée' pour valider) : "))
math = float(input("Veuillez saisir votre note de math entre 0 et 20  (Appuyez sur 'Entrée' pour valider) : "))
geometry = float(input("Veuillez saisir votre note de géométrie entre 0 et 20  (Appuyez sur 'Entrée' pour valider) : "))
computer_science = float(input("Veuillez saisir votre note d'informatique entre 0 et 20  (Appuyez sur 'Entrée' pour valider) : "))

print()
print(f"Votre moyenne est de {(french+math+geometry+computer_science)/4}/20.")