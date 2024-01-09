##### TROUVER LA LETTRE LA MOINS PRÉSENTE #####


# Définition des variables de base
title = "La lettre la mois présente"
title_deco = "├"+"─"*int(73-(len(title)/2))+"┤"

if len(title)%2 == 0 :
    program_deco = "\n"+"═"*152+"\n"
else :
    program_deco = "\n"+"═"*151+"\n"


# Entête
print(program_deco+title_deco,title.upper(),title_deco,"\n")
print("ℹ : Quand une réponse vous est demandée, saissisez-la au clavier et appuyez sur la touche 'Entrée' pour valider.","\n","\n")


# Définition des variables de base
table_yes = ["Oui","oui","OUI","O","o","Yes","yes","YES","Y","y","1"]
table_no = ["Non","non","NON","N","n","No","no","NO","0"]

table_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

count_letter = 99999999999999999999999999
table_counter = 0
final_text = ""

new_text_verification = False

error_message = "\n⚠ Erreur ⚠ : Votre choix est invalide. Merci de saisir 'Oui' ou 'Non'."


# Programme
while new_text_verification == False :
    text = input("Veuillez saisir votre texte : ")
    final_text += text
    new_text = input("\nVoulez-vous ajouter un nouveau texte ? : ")
    new_text_verification_retry = False
    while new_text_verification_retry == False :
        if new_text in table_yes :
            new_text_verification_retry = True
        elif new_text in table_no :
            new_text_verification = True
            new_text_verification_retry = True
        else : 
            print(error_message)
            input("Voulez-vous ajouter un nouveau texte ? : ")
final_text = final_text.upper()

for i in range (26) :
    number_letter = 0
    for i in range (len(final_text)) :
        if final_text[i] == table_letters[table_counter] :
            number_letter += 1
    if number_letter < count_letter :
        count_letter = number_letter
        letter = table_letters[table_counter]
    table_counter += 1

print(f"\n\n● La lettre '{letter}' apparaît {count_letter} fois. ●\n",program_deco)

