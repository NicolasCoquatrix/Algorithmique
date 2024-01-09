# Mise en place d'une alarme pour le contrôle de votre centrale nucléaire

print("=== Je vais mettre en place une alarme pour le contrôle de votre centrale nucléaire. ===")
print("Quand une valeur vous est demandée, saissisez-la au clavier et appuyez sur la touche 'Entrée' pour valider.")

print()

ambient = float(input("Veuillez saisir la température ambiante en degré celsius : "))
cooling_pools = float(input("Veuillez saisir la température des bassins de refroidissements en degré celsius : "))

diff = abs(ambient - cooling_pools)

print()

if diff < 20 or diff > 40 :
    print(f"!! Alerte !! Il y a {diff}°C de différence entre la température ambiante et celle des bassins de refroidissement.")