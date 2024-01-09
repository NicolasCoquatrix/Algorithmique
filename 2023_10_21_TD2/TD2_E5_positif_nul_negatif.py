# Définir si votre nombre est positif, nul ou négatif

print("=== Je vais définir si votre nombre est positif, nul ou négatif. ===")
print("Quand une valeur vous est demandée, saissisez-la au clavier et appuyez sur la touche 'Entrée' pour valider.")

print()

number = float(input("Veuillez saisir un nombre : "))

print()

if number > 0 :
    print(f"{number} est un nombre positif")
elif number == 0 :
    print(f"{number} est un nombre nul")
else :
    print(f"{number} est un nombre négatif")