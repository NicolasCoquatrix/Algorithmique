##### JEU DU NOMBRE  #####

from random import*


# Définition des variables de base
title = "Trouvez le nombre magique"
title_deco = "├"+"─"*int(73-(len(title)/2))+"┤"

if len(title)%2 == 0 :
    program_deco = "\n"+"═"*152+"\n"
else :
    program_deco = "\n"+"═"*151+"\n"

error_message = "\n⚠ Erreur ⚠ : Valeur non permise. Merci de saisir un nombre compris entre 1 et 10."


# Entête
print(program_deco+title_deco,title.upper(),title_deco,"\n")
print("ℹ : Quand une réponse vous est demandée, saisissez un nombre compris entre 1 et 10 et appuyez sur la touche 'Entrée' pour valider.","\n","\n")


# Définition des variables du programme
choice_table = ["1","2","3","4","5","6","7","8","9","10"]
game_number = ""
attempt = 1


# Programme
magic_number = randint(1,10)

game_number = input("Veuillez saisir un nombre : ")
while game_number not in choice_table :
    print(error_message)
    game_number = input("Veuillez saisir un nombre : ")
game_number = int(game_number)

while game_number != magic_number :
    if game_number < magic_number :
        print(f"\nEssai N° {attempt} : Le nombre {game_number} est plus petit que le nombre magique.")
        game_number = input(f"Veuillez saisir un nombre PLUS GRAND que {game_number} : ")
        while game_number not in choice_table :
            print(error_message)
            game_number = input("Veuillez saisir un nombre : ")
        game_number = int(game_number)
        attempt += 1
    else :
        print(f"\nEssai N° {attempt} : Le nombre {game_number} est plus grand que le nombre magique.")
        game_number = input(f"Veuillez saisir un nombre PLUS PETIT que {game_number} : ")
        while game_number not in choice_table :
            print(error_message)
            game_number = input("Veuillez saisir un nombre : ")
        game_number = int(game_number)
        attempt += 1


print(f"\n● Bravo vous avez gagné en {attempt} essai, le nombre magique était {magic_number}. ●\n",program_deco)