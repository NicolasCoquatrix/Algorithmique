##### CLASSER DES NOMBRES #####


# Définition des variables de base
title = "Le classeur de nombre"
title_deco = "├"+"─"*int(73-(len(title)/2))+"┤"

if len(title)%2 == 0 :
    program_deco = "\n"+"═"*152+"\n"
else :
    program_deco = "\n"+"═"*151+"\n"


# Entête
print(program_deco+title_deco,title.upper(),title_deco,"\n")
print("ℹ : Quand une réponse vous est demandée, saisissez un nombre et appuyez sur la touche 'Entrée' pour valider.","\n","\n")


# Définition des variables du programme
biggest_number = 0
number = ""

# Programme
for i in range (20) :
    number = float(input("Veuillez saisir un nombre : "))
    if number > biggest_number :
        biggest_number = number

print(f"\n● Le plus grand des 20 nombres saisi est le {biggest_number}. ●\n",program_deco)