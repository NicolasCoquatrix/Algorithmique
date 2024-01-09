# Calculer la moyenne des notes d'un élève

print("=== Je vais calculer pour vous la moyenne de vos notes. ===")
print("Quand une valeur vous est demandée, saissisez-la au clavier et appuyez sur la touche 'Entrée' pour valider.")

print()

# Notes de français
note_french = float(input("Veuillez saisir votre note de français entre 0 et 20 : "))
coef_french = float(input("Veuillez saisir le coefficient de la note de français : "))

# Notes de maths
note_math = float(input("Veuillez saisir votre note de maths entre 0 et 20 : "))
coef_math = float(input("Veuillez saisir le coefficient de la note de maths : "))

# Notes de géométrie
note_geometry = float(input("Veuillez saisir votre note de géométrie entre 0 et 20 : "))
coef_geometry = float(input("Veuillez saisir le coefficient de la note de géométrie : "))

# Notes d'informatique
note_computer_science = float(input("Veuillez saisir votre note d'informatique entre 0 et 20 : "))
coef_computer_science = float(input("Veuillez saisir le coefficient de la note d'informatiqiue : "))

print()

print(f"Votre moyenne est de {round(((note_french*coef_french)+(note_math*coef_math)+(note_geometry*coef_geometry)+(note_computer_science*coef_computer_science))/(coef_french+coef_math+coef_geometry+coef_computer_science),1)}/20.")