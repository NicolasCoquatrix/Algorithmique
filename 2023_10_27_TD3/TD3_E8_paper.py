##### CALCULER L'ÉPAISSEUR D'UNE FEUILLE #####


# Définition des variables de base
title = "Le calculateur de feuille"
title_deco = "├"+"─"*int(73-(len(title)/2))+"┤"

if len(title)%2 == 0 :
    program_deco = "\n"+"═"*152+"\n"
else :
    program_deco = "\n"+"═"*151+"\n"

error_message_int = "\n⚠ Erreur ⚠ : Valeur non permise. Merci de saisir un nombre entier positif."
error_message_float = "\n⚠ Erreur ⚠ : Valeur non permise. Merci de saisir un nombre positif."

# Entête
print(program_deco+title_deco,title.upper(),title_deco,"\n")
print("ℹ : Quand une réponse vous est demandée, saisissez un nombre positif et appuyez sur la touche 'Entrée' pour valider.","\n","\n")


# Définition des variables du programme
decimal_table = ["0","1","2","3","4","5","6","7","8","9"]
separator_table = [",","."]


# Programme
thickness = input("Veuillez saisir l'épaisseur de la feuille en cm : ")
decimal_verification = False
while decimal_verification == False :
    for location in range (len(thickness)):
        if thickness[location] not in decimal_table and thickness[location] not in separator_table :
            decimal_verification = False
            break
        else :
            decimal_verification = True
    separator_count = 0
    for location in range (len(thickness)):
        if thickness[location] in separator_table :
            separator_count += 1
        if separator_count > 1 :
            decimal_verification = False
            break
    if decimal_verification == False :
        print(error_message_float)
        thickness= input("Veuillez saisir l'épaisseur de la feuille en cm : ")
    else :
        thickness = float(thickness)
initial_thickness = thickness

folds = input("\nVeuillez saisir le nombre de plis : ")
decimal_verification = False
while decimal_verification == False :
    for location in range (len(folds)):
        if folds[location] not in decimal_table :
            decimal_verification = False
            break
        else :
            decimal_verification = True
    if decimal_verification == False :
        print(error_message_int)
        folds= input("Veuillez saisir l'épaisseur de la feuille en cm : ")
    else :
        folds = int(folds)

for i in range (folds) :
    thickness = thickness * 2

print(f"\n\n● Si on plie {folds} fois une feuille de {initial_thickness} cm, la feuille fera {thickness} cm d'épaisseur. ●\n",program_deco)

