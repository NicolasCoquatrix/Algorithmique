##### JEU DU LABYRINTHE #####

import os #os.system("cls")
import time #time.sleep()

## DÉFINITION DES VARIABLES DE BASE ##
title = "L'écran magique"
title_deco = "├"+"─"*int(20-(len(title)/2))+"┤"


## DÉFINITION DE L'ECRAN DU JEU ##
screen = "═"*45 + "\n" + title_deco + " " + title.upper() + " " + title_deco + "\n" + "═"*45 + "\n"
length_screen = 35
magic_screen_head = " "*int((45-length_screen)/2) + "╔" + "═"*length_screen + "╗\n"
magic_screen_foot = " "*int((45-length_screen)/2) + "╚" + "═"*length_screen + "╝\n" + "═"*45
text = ""
end_pwd = " "*length_screen + "STOP" + " "*length_screen


## PROGRAMME ##
# Affichage de l'écran de l'écran au démarrage
while text != end_pwd :
    os.system("cls")
    print(screen + magic_screen_head + " "*int((45-length_screen)/2) + "║" + " "*length_screen + "║\n" + magic_screen_foot + "\nSaissisez le texte à afficher au clavier et\nappuyez sur la touche 'Entrée' pour valider : \n")
    text = input().upper()
    text = " "*length_screen + text + " "*length_screen
    os.system("cls")
    if text != end_pwd :
        for letter in range (len(text)-length_screen+1) :
            time.sleep(0.1)
            os.system("cls")
            print(screen + magic_screen_head + " "*int((45-length_screen)/2) + "║", end='')
            for i in range (length_screen) :
                print(text[letter+i], end='')
            print("║\n" + magic_screen_foot)