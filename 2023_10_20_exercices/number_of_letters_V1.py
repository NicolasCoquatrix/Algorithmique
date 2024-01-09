##### COMPTER LE NOMBRE DE LETTRE #####


# Définition des variables de base
title = "Le compteur de lettre"
title_deco = "├"+"─"*int(73-(len(title)/2))+"┤"

if len(title)%2 == 0 :
    program_deco = "\n"+"═"*152+"\n"
else :
    program_deco = "\n"+"═"*151+"\n"

error_message = "\n⚠ Erreur ⚠ : Valeur non permise. Merci de saisir un nombre entier positif."

# Entête
print(program_deco+title_deco,title.upper(),title_deco,"\n")
print("ℹ : Quand une réponse vous est demandée, saissisez-la au clavier et appuyez sur la touche 'Entrée' pour valider.","\n","\n")


# Définition des variables de base
number_letter = 0


# Programme
text = input("Veuillez saisir votre texte : ")

input_letter = input("\nVeuillez saisir la lettre à compter : ")

for letter in text :
    if letter == input_letter :
        number_letter += 1

print(f"\n\n● La lettre '{input_letter}' apparaît {number_letter} fois. ●\n",program_deco)

