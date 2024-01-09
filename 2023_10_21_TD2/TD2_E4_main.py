# Jeu de la main

print("=== Le jeu de la main. ===")
print("Quand une valeur vous est demandée, saissisez-la au clavier et appuyez sur la touche 'Entrée' pour valider.")

print()

hand_a = int(input("JOUEUR 1 : Veuillez saisir le nombre de doigts entre 1 et 5 : "))
hand_b = int(input("JOUEUR 2 : Veuillez saisir le nombre de doigts entre 1 et 5 : "))

print()

if (hand_a >= 0 and hand_a <= 5) and (hand_b >= 0 and hand_b <= 5) :
    if ((hand_a + hand_b) % 2) == 0 :
        print("Victoire du JOUEUR 1 !")
    else :
        print("Victoire du JOUEUR 2 !")
elif hand_a < 0 or hand_a > 5 :
    print("/!\ Erreur : Le JOUEUR 1 à joué un nombre de doigts invalide. Merci de saisir un chiffre entre 1 et 5.")
else :
    print("/!\ Erreur : Le JOUEUR 2 à joué un nombre de doigts invalide. Merci de saisir un chiffre entre 1 et 5.")