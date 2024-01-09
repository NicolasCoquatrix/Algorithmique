##### JEU DU LABYRINTHE #####

import os #os.system("cls")
import time #time.sleep()

## DÉFINITION DES VARIABLES DE BASE ##
title = "L'écran magique"
title_deco = "├"+"─"*int(20-(len(title)/2))+"┤"


## DÉFINITION DES VARIABLES MODIFIABLES ##
length_screen = 35
speed = 0.1
end_pwd = "Stop"


## DÉFINITION DE L'ECRAN DU JEU ##
screen = "═"*45 + "\n" + title_deco + " " + title.upper() + " " + title_deco + "\n" + "═"*45 + "\n"
magic_screen_head = " "*int((45-length_screen)/2) + "╔" + "═"*length_screen + "╗\n"
magic_screen_foot = " "*int((45-length_screen)/2) + "╚" + "═"*length_screen + "╝\n" + "═"*45
text = ""
border = 0
end_pwd = " "*length_screen + end_pwd.upper() + " "*length_screen


## PROGRAMME ##
increment = 0
text = input().upper()
text = " "*length_screen + text + " "*length_screen
screen_tab = []
for box in range (length_screen) :
    screen_tab += [text[box+increment]]
print(screen_tab)
increment += 1
