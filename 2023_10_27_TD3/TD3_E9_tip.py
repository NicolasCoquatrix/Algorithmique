##### AFFICHER DES POINTES #####


# Définition des variables de base
title = "L'afficheur de pointe"
title_deco = "├"+"─"*int(73-(len(title)/2))+"┤"

if len(title)%2 == 0 :
    program_deco = "\n"+"═"*152+"\n"
else :
    program_deco = "\n"+"═"*151+"\n"

error_message = "\n⚠ Erreur ⚠ : Valeur non permise. Merci de saisir un nombre entier positif."

# Entête
print(program_deco+title_deco,title.upper(),title_deco,"\n")
print("ℹ : Quand une réponse vous est demandée, saisissez un nombre positif entier et appuyez sur la touche 'Entrée' pour valider.","\n","\n")


# Définition des variables du programme
decimal_table = ["0","1","2","3","4","5","6","7","8","9"]
separator_table = [",","."]


# Programme
dimention = input("Veuillez saisir la dimension de la pointe (la dimension est mesuré en '|') : ")
decimal_verification = False
while decimal_verification == False :
    for location in range (len(dimention)):
        if dimention[location] not in decimal_table :
            decimal_verification = False
            break
        else :
            decimal_verification = True
    if decimal_verification == False :
        print(error_message)
        dimention= input("Veuillez saisir la dimension de la pointe (la dimension est mesuré en '|') : ")
    else :
        dimention = int(dimention)

number = input("\nVeuillez saisir le nombre de pointe voulu : ")
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
        number= input("Veuillez saisir le nombre de pointe voulu : ")
    else :
        number = int(number)

display = "_ " * number

for i in range (dimention) : 
    display += "\n" + "| " * number

print(f"\n\n{display}\n",program_deco)

