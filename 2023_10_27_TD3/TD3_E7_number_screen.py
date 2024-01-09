##### AFFICHER DE 10 À 55  #####


# Définition des variables de base
title = "L'écran des nombres"
title_deco = "├"+"─"*int(73-(len(title)/2))+"┤"

if len(title)%2 == 0 :
    program_deco = "\n"+"═"*152+"\n"
else :
    program_deco = "\n"+"═"*151+"\n"


# Entête
print(program_deco+title_deco,title.upper(),title_deco,"\n")
input("ℹ : Lancer le programme, veuillez appuyer sur la touche 'Entrée'.")


# Définition des variables du programme
starting_value = 10
screen = ""


# Programme
for i in range (5) :
    for i in range (6) : 
        screen += " " + str(starting_value+i)
        if i == 5 :
            save_value = starting_value+i
    starting_value = save_value+5
    screen += "\n"

print(f"\n\n{screen}",program_deco)