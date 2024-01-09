##### CONVERTIRE UN NOMBRE DE LA BASE 10 VERS LA BASE 2 #####


# Définition des variables de base
title = "Le convertisseur binaire"
title_deco = "├"+"─"*int(73-(len(title)/2))+"┤"

if len(title)%2 == 0 :
    program_deco = "\n"+"═"*152+"\n"
else :
    program_deco = "\n"+"═"*151+"\n"

error_message = "\n⚠ Erreur ⚠ : Valeur non permise. Merci de saisir un nombre entier positif."

# Entête
print(program_deco+title_deco,title.upper(),title_deco,"\n")
print("ℹ : Quand une réponse vous est demandée, saisissez un nombre entier positif et appuyez sur la touche 'Entrée' pour valider.","\n","\n")


# Définition des variables du programme
decimal_table = ["0","1","2","3","4","5","6","7","8","9"]
binary = ""


# Programme
number = input("Veuillez saisir un nombre entier positif : ")
decimal_verification = False
while decimal_verification == False :
    for location in range (len(number)):
        if number[location] not in decimal_table :
            decimal_verification = False
            break
        else :
            decimal_verification = True
    if decimal_verification == False :
        print(error_message)
        number= input("Veuillez saisir un nombre entier positif : ")
    else :
        number = int(number)

quotient = number

if number == 0 :
    binary = "0"

while quotient != 0 :
    remainder = quotient % 2
    binary = str(remainder) + binary
    quotient //= 2

print(f"\n● La converssion de {number} en binaire donne : {binary} ●\n",program_deco)

