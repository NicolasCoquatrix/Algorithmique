##### COMPTEUR AVEC UN PAS D'INCRÉMENTATION  #####


# Définition des variables de base
title = "Le super compteur"
title_deco = "├"+"─"*int(73-(len(title)/2))+"┤"

if len(title)%2 == 0 :
    program_deco = "\n"+"═"*152+"\n"
else :
    program_deco = "\n"+"═"*151+"\n"

error_message = "\n⚠ Erreur ⚠ : Valeur non permise. Merci de saisir un nombre."

# Entête
print(program_deco+title_deco,title.upper(),title_deco,"\n")
print("ℹ : Quand une réponse vous est demandée, saisissez un nombre et appuyez sur la touche 'Entrée' pour valider.","\n","\n")


# Définition des variables du programme
decimal_table = ["0","1","2","3","4","5","6","7","8","9"]


# Programme
starting_point = input("Veuillez saisir la borne de départ : ")
decimal_verification = "KO"
while decimal_verification == "KO" :
    for location in range (len(starting_point)):
        if starting_point[location] not in decimal_table : 
            decimal_verification = "KO"
            break
        else :
            decimal_verification = "OK"
    if decimal_verification == "KO" :
        print(error_message)
        starting_point = input("Veuillez saisir la borne de départ : ")
starting_point = int(starting_point)

print()

end_terminal = input("Veuillez saisir la borne d'arrivée : ")
decimal_verification = "KO"
while decimal_verification == "KO" :
    for location in range (len(end_terminal)):
        if end_terminal[location] not in decimal_table : 
            decimal_verification = "KO"
            break
        else :
            decimal_verification = "OK"
    if decimal_verification == "KO" :
        print(error_message)
        end_terminal = input("Veuillez saisir la borne d'arrivée' : ")
end_terminal = int(end_terminal)

print()

increment = input("Veuillez saisir le pas d'incrémentation : ")
decimal_verification = "KO"
while decimal_verification == "KO" :
    for location in range (len(increment)):
        if increment[location] not in decimal_table : 
            decimal_verification = "KO"
            break
        else :
            decimal_verification = "OK"
    if decimal_verification == "KO" :
        print(error_message)
        increment = input("Veuillez saisir le pas d'incrémentation : ")
increment = int(increment)

result = ""
for i in range (starting_point,end_terminal+1,increment) :
    result += str(i)+" "

print(f"\n● {result}●\n",program_deco)