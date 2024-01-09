# Calculer le montant TTC d'un prix avec un choix de TVA

print("=== Je vais calculer pour vous le montant TTC. ===")
print("Quand une valeur vous est demandée, saissisez-la au clavier et appuyez sur la touche 'Entrée' pour valider.")

print()

price = float(input("Veuillez saisir le prix HT du produit en euro : "))

print()

print("Pour une TVA de 5,5 %, saisissez 1")
print("Pour une TVA de 19,6 %, saisissez 2")
print("Pour une TVA de 33 %, saisissez 3")

choice = int(input("Veuillez saisir 1, 2 ou 3 en fonction de votre TVA : "))

print()

if choice == 1 :
    print(f"Le prix HT est de {price}€, la TVA est de 5.5 % et le prix TTC est de {round(price*1.055, 2)}€.")
elif choice == 2 :
    print(f"Le prix HT est de {price}€, la TVA est de 19.6 % et le prix TTC est de {round(price*1.196, 2)}€.")
elif choice == 3 :
    print(f"Le prix HT est de {price}€, la TVA est de 33 % et le prix TTC est de {round(price*1.33, 2)}€.")
else :
    print("/!\ Erreur : Votre choix de TVA est invalide. Merci de saisir un chiffre entre 1 et 3.")