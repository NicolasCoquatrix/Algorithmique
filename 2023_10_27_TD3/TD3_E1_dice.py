##### JEU DU DÉ  #####

from random import*


# Définition des variables de base
title = "Le super jeu du dé"
title_deco = "├"+"─"*int(73-(len(title)/2))+"┤"

if len(title)%2 == 0 :
    program_deco = "\n"+"═"*152+"\n"
else :
    program_deco = "\n"+"═"*151+"\n"


# Entête
print(program_deco+title_deco,title.upper(),title_deco,"\n")
input("ℹ : Pour jouer, veuillez appuyer sur la touche 'Entrée'.")


# Définition des variables du programme
dice = randint(1,6)
face_dice = ""
text_decoration = ""


# Programme
if dice == 1 :
    dice = "UN"
    face_dice = "\n╔═════════╗\n║         ║\n║    ●    ║\n║         ║\n╚═════════╝"
    text_decoration = "●"
elif dice == 2 :
    dice = "DEUX"
    face_dice = "\n╔═════════╗\n║      ●  ║\n║         ║\n║  ●      ║\n╚═════════╝"
    text_decoration = "●●"
elif dice == 3 :
    dice = "TROIS"
    face_dice = "\n╔═════════╗\n║      ●  ║\n║    ●    ║\n║  ●      ║\n╚═════════╝"
    text_decoration = "●●●"
elif dice == 4 :
    dice = "QUATRE"
    face_dice = "\n╔═════════╗\n║  ●   ●  ║\n║         ║\n║  ●   ●  ║\n╚═════════╝"
    text_decoration = "●●●●"
elif dice == 5 :
    dice = "CINQ"
    face_dice = "\n╔═════════╗\n║  ●   ●  ║\n║    ●    ║\n║  ●   ●  ║\n╚═════════╝"
    text_decoration = "●●●●●"
else :
    dice = "SIX"
    face_dice = "\n╔═════════╗\n║  ●   ●  ║\n║  ●   ●  ║\n║  ●   ●  ║\n╚═════════╝"
    text_decoration = "●●●●●●"

print(f"\n\n{text_decoration} Vous avez fait un {dice} {text_decoration}",face_dice,"\n",program_deco)