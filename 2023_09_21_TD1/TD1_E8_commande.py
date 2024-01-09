# Calculer le montant TTC d'une commande avec une remise de 15%

print("=== Je vais calculer pour vous le montant TTC d'une commande avec une remise de 15%. ===")
print()

price = float(input("Veuillez saisir le prix unitaire HT du produit en euro (Appuyez sur 'Entrée' pour valider) : "))
quantity = int(input("Veuillez saisir la quantité de produits commandés (Appuyez sur 'Entrée' pour valider) : "))
vat = float(input("Veuillez saisir le montant de la TVA en pourcentage (Appuyez sur 'Entrée' pour valider) : "))

total_price = price * quantity
discount = total_price * .15
price_discount = total_price-discount

print()
print(f"Le montant de votre commande est de {total_price}€ HT.")
print(f"Avec une réduction de 15%, le montant de votre commande est de {price_discount}€ HT, vous économisez {discount}€ HT.")
print(f"Le montant de votre commande est de {price_discount+price_discount*vat/100}€ TTC.")