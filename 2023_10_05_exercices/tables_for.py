# Afficher une table de multiplication

print("="*123)
print("-"*31, "Je vais afficher la table de multiplication de votre choix.", "-"*31,"\n")

table = int(input("Veuillez saisir le numéro de la table de multiplication que vous souhaitez afficher (Appuyez sur 'Entrée' pour valider) : "))

print()
for loop in range (0,11) :
    print(f"{table} x {loop} = {table * loop}")

print()
print("="*123,"\n")