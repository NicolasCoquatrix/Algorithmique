##### TROUVER LA LETTRE LA PLUS PRÉSENTE #####


# Définition des variables de base
title = "La lettre la plus présente"
title_deco = "├"+"─"*int(73-(len(title)/2))+"┤"

if len(title)%2 == 0 :
    program_deco = "\n"+"═"*152+"\n"
else :
    program_deco = "\n"+"═"*151+"\n"


# Entête
print(program_deco+title_deco,title.upper(),title_deco,"\n")
print("ℹ : Quand une réponse vous est demandée, saissisez-la au clavier et appuyez sur la touche 'Entrée' pour valider.","\n","\n")


# Définition des variables de base
table_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
count_letter = 0
table_counter = 0


# Programme
text = input("Veuillez saisir votre texte : ")
text = text.upper()

for i in range (26) :
    number_letter = 0
    for i in range (len(text)) :
        if text[i] == table_letters[table_counter] :
            number_letter += 1
    if number_letter > count_letter :
        count_letter = number_letter
        letter = table_letters[table_counter]
    table_counter += 1

print(f"\n\n● La lettre '{letter}' apparaît {count_letter} fois. ●\n",program_deco)

