##### TROUVER LE JOUR À PARTIR D'UNE DATE  #####


# Définition des variables de base
title = "Trouver le jour à partir d'une date"
title_deco = "├"+"─"*int(73-(len(title)/2))+"┤"

if len(title)%2 == 0 :
    program_deco = "\n"+"═"*152+"\n"
else :
    program_deco = "\n"+"═"*151+"\n"

error_message = "\n⚠ Erreur ⚠ : Votre saisie est invalide. Merci de saisir une date sous la forme 'AAAA/MM/JJ' (exemple : 2023/10/16 pour le 16 ocobre 2023)."


# Entête
print(program_deco+title_deco,title.upper(),title_deco,"\n")
print("ℹ : Quand une réponse vous est demandée, saisissez une date sous la forme 'AAAA/MM/JJ' et appuyez sur la touche 'Entrée' pour valider.","\n","\n")


# Définition des variables du programme
decimal_table = ["0","1","2","3","4","5","6","7","8","9"]
separator_table = ["/","-",".","_",","]



# Programme
date = input("Veuillez saisir une date : ")
while date[0] not in decimal_table or date[1] not in decimal_table or date[2] not in decimal_table or date[3] not in decimal_table or date[4] not in separator_table or date[5] not in decimal_table or date[6] not in decimal_table or date[7] not in separator_table or date[8] not in decimal_table or date[9] not in decimal_table :
    print(error_message)
    date = input("Veuillez saisir une date : ")

A = int(date[0]+date[1]+date[2]+date[3])
M = int(date[5]+date[6])
J = int(date[8]+date[9])

if M == 1 :
    month = "janvier"
elif M == 2 :
    month = "février"
elif M == 3 :
    month = "mars"
elif M == 4 :
    month = "avril"
elif M == 5 :
    month = "mai"
elif M == 6 :
    month = "juin"
elif M == 7 :
    month = "juillet"
elif M == 8 :
    month = "août"
elif M == 9 :
    month = "septembre"
elif M == 10 :
    month = "octobre"
elif M == 11 :
    month = "novembre"
else :
    month = "décembre"

year = A

if M == 1 or M == 2 :
    A -= 1
    M += 12

N = J+int((13*M+3)/5)+int(5*A/4)-int(A/100)+int(A/400)
N = N%7

if N == 0 :
    day = "Lundi"
elif N == 1 :
    day = "Mardi"
elif N == 2 :
    day = "Mercredi"
elif N == 3 :
    day = "Jeudi"
elif N == 4 :
    day = "Vendredi"
elif N == 5 :
    day = "Samedi"
else:
    day = "Dimanche"

print(f"\n\n● Le {J} {month} {year} est un {day}. ●\n",program_deco)