# Calculer la mention des notes d'un élève


print("=== Je vais calculer pour vous votre mention. ===")
print("Quand une valeur vous est demandée, saissisez-la au clavier et appuyez sur la touche 'Entrée' pour valider.")

print()

french = float(input("Veuillez saisir votre note de français entre 0 et 20 : "))
if french < 0 or french > 20 :
    print("/!\ Erreur : Votre note de français est invalide. Merci de saisir une notre entre 0 et 20.")
    exit()

math = float(input("Veuillez saisir votre note de math entre 0 et 20 : "))
if math < 0 or math > 20 :
    print("/!\ Erreur : Votre note de mathématique est invalide. Merci de saisir une notre entre 0 et 20.")
    exit()

geometry = float(input("Veuillez saisir votre note de géométrie entre 0 et 20 : "))
if geometry < 0 or geometry > 20 :
    print("/!\ Erreur : Votre note de géométrie est invalide. Merci de saisir une notre entre 0 et 20.")
    exit()

computer_science = float(input("Veuillez saisir votre note d'informatique entre 0 et 20 : "))
if computer_science < 0 or computer_science > 20 :
    print("/!\ Erreur : Votre note d'informatique est invalide. Merci de saisir une notre entre 0 et 20.")
    exit()

print()

average = (french+math+geometry+computer_science)/4

if average >= 16 :
    print(f"Félicitation, vous avez la mention 'Très bien'")
elif average >= 12 and average < 16 :
    print(f"Bravo, vous avez la mention 'Bien'")
elif average >= 8 and average < 12 :
    print(f"Super, vous avez la mention 'Assez Bien'")
elif average >= 4 and average < 8 :
    print(f"Il faut redoubler d'efforts, vous avez la mention 'Insuffisant'")
else :
    print(f"Vous êtes stupide, vous avez la mention 'Nul'")