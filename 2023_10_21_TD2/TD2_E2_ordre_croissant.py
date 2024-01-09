# Déterminer si 3 nombres sont dans un ordre croissant

print("=== Je vais déterminer pour vous si trois nombres sont classé par ordre croissant. ===")
print("Quand une valeur vous est demandée, saissisez-la au clavier et appuyez sur la touche 'Entrée' pour valider.")

print()

number_a = float(input("Veuillez saisir le premier nombre : "))
number_b = float(input("Veuillez saisir le deuxième nombre : "))
number_c = float(input("Veuillez saisir le troisième nombre : "))

print()

if number_a < number_b and number_b < number_c :
    print(f"{number_a}, {number_b}, {number_c} : votre liste est dans un ordre croissant")
else :
    print("Votre liste n'est pas dans un ordre croissant")