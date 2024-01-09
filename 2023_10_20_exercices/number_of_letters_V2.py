##### COMPTER LE NOMBRE DE LETTRE #####


# Définition des variables de base
title = "Le compteur de lettre"
title_deco = "├"+"─"*int(73-(len(title)/2))+"┤"

if len(title)%2 == 0 :
    program_deco = "\n"+"═"*152+"\n"
else :
    program_deco = "\n"+"═"*151+"\n"

error_message = "\n⚠ Erreur ⚠ : Valeur non permise. Merci de saisir une lettre."

# Entête
print(program_deco+title_deco,title.upper(),title_deco,"\n")
print("ℹ : Quand une réponse vous est demandée, saissisez-la au clavier et appuyez sur la touche 'Entrée' pour valider.","\n","\n")


# Définition des variables de base
table_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
number_letter = 0


# Programme
text = input("Veuillez saisir votre texte : ")
text = text.upper()

letter = input("\nVeuillez saisir la lettre à compter : ")
letter = letter.upper()
letter_verification = False
while letter_verification == False :
    if len(letter) == 1 :
        if letter not in table_letters :
            letter_verification = False
        else :
            letter_verification = True
        if letter_verification == False :
            print(error_message)
            letter = input("Veuillez saisir la lettre à compter : ")
    else :
        print(error_message)
        letter = input("Veuillez saisir la lettre à compter : ")

for i in range (len(text)) :
    if text[i] == letter :
        number_letter += 1


print(f"\n\n● La lettre '{letter}' apparaît {number_letter} fois. ●\n",program_deco)

