# Définir si une personne est invité à la soirée d'Alain et Catherine

error = "/!\ Erreur : Votre saisie est invalide. Merci de saissir '1' pour 'Oui' ou '0' pour 'Non'."

print("=== Êtes-vous invité(e) à la soirée d'Alain et Catherine ? ===")
print("Quand une valeur vous est demandée, saissisez '1' pour 'Oui' ou '0' pour 'Non' au clavier et appuyez sur la touche 'Entrée' pour valider.")

print()

a = int(input("Êtes-vous ami avec Alain ? : "))
if a != 1 and a != 0 :
    print(error)
    exit()

b = int(input("Jouez-vous au bridge ? : "))
if b != 1 and b != 0 :
    print(error)
    exit()

c = int(input("Êtes-vous ami avec Catherine ? : "))
if c != 1 and c != 0 :
    print(error)
    exit()

print()

if (a == 1 and c == 1) or (a == 0 and c == 1) or (c == 0 and b == 1) :
    print("Super, vous êtes invité(e) à la soirée, ramenez une bouteille.")
else :
    print("Dommage, vous n'êtes pas invité(e) à la soirée.")