# Résoudre l'équation "ax + b = 0"

print("=== Cherchons à résoudre l'équation 'ax + b = 0'. ===")
print("Quand une valeur vous est demandée, saissisez-la au clavier et appuyez sur la touche 'Entrée' pour valider.")

print()

a = float(input("Veuillez saisir la valeur de a : "))
b = float(input("Veuillez saisir la valeur de b : "))

print()

if a == 0 and b == 0 :
    print("L'ensemble des solutions est l'ensemble R.")
elif a == 0 and b != 0 :
    print("L'ensemble des solutions est l'ensemble vide.")
elif a != 0 :
    print(f"La solution est {-b/a}.")