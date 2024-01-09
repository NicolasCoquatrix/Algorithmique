# Appliquer une remise en fonction du prix

print("=== Je vais appliquer une remise à votre commande en fonction de son montant TTC. ===")
print("Quand une valeur vous est demandée, saissisez-la au clavier et appuyez sur la touche 'Entrée' pour valider.")

print()

price = float(input("Veuillez saisir le prix TTC de la commande en euro : "))
discount = 0
print()

if price < 500 :
    print("Désolé, vous n'avez le droit à aucune remise.")
elif price >= 500 and price < 1000 :
    discount = 2
elif price >= 1000 and price < 2000 :
    discount = 5
else :
    discount = 10

print(f"Avec une remise de {discount}%, le nouveau montant de votre commande est de {price*(1-discount/100)}€ TTC.")