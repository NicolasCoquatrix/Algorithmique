##### CALCULER LA MENTION DES NOTES D'UN ÉLÉVE  #####


# Définition des variables de base
title = "Le calculateur de mention"
title_deco = "├"+"─"*int(73-(len(title)/2))+"┤"

if len(title)%2 == 0 :
    program_deco = "\n"+"═"*152+"\n"
else :
    program_deco = "\n"+"═"*151+"\n"

error_message = "\n⚠ Erreur ⚠ : Valeur non permise."

# Entête
print(program_deco+title_deco,title.upper(),title_deco,"\n")
print("ℹ : Quand une réponse vous est demandée, saisissez un nombre et appuyez sur la touche 'Entrée' pour valider.","\n")


# Définition des variables du programme
decimal_table = ["0","1","2","3","4","5","6","7","8","9"]
separator_table = [",","."]


# Programme
# Français
note_french = input("\nVeuillez saisir votre note de français entre 0 et 20 : ")
decimal_verification = False
while decimal_verification == False :
    for location in range (len(note_french)):
        if note_french[location] not in decimal_table and note_french[location] not in separator_table :
            decimal_verification = False
            break
        else :
            decimal_verification = True
    separator_count = 0
    for location in range (len(note_french)):
        if note_french[location] in separator_table :
            separator_count += 1
        if separator_count > 1 :
            decimal_verification = False
            break
    if decimal_verification == False :
        print(error_message)
        note_french= input("Veuillez saisir votre note de français entre 0 et 20 : ")
    else :
        note_french = float(note_french)
        if note_french > 20 :
            print(error_message)
            note_french= input("Veuillez saisir votre note de français entre 0 et 20 : ")
            decimal_verification = False
coef_french = input("Veuillez saisir votre coefficient de français entre 1 et 10 : ")
decimal_verification = False
while decimal_verification == False :
    for location in range (len(coef_french)):
        if coef_french[location] not in decimal_table :
            decimal_verification = False
            break
        else :
            decimal_verification = True
    if decimal_verification == False :
        print(error_message)
        coef_french= input("Veuillez saisir votre coefficient de français entre 1 et 10 : ")
    else :
        coef_french = float(coef_french)
        if coef_french == 0 or coef_french > 10 :
            print(error_message)
            coef_french= input("Veuillez saisir votre coefficient de français entre 1 et 10 : ")
            decimal_verification = False

# Maths
note_math = input("\nVeuillez saisir votre note de méthématique entre 0 et 20 : ")
decimal_verification = False
while decimal_verification == False :
    for location in range (len(note_math)):
        if note_math[location] not in decimal_table and note_math[location] not in separator_table :
            decimal_verification = False
            break
        else :
            decimal_verification = True
    separator_count = 0
    for location in range (len(note_math)):
        if note_math[location] in separator_table :
            separator_count += 1
        if separator_count > 1 :
            decimal_verification = False
            break
    if decimal_verification == False :
        print(error_message)
        note_math= input("Veuillez saisir votre note de méthématique entre 0 et 20 : ")
    else :
        note_math = float(note_math)
        if note_math > 20 :
            print(error_message)
            note_math= input("Veuillez saisir votre note de méthématique entre 0 et 20 : ")
            decimal_verification = False
coef_math = input("Veuillez saisir votre coefficient de méthématique entre 1 et 10 : ")
decimal_verification = False
while decimal_verification == False :
    for location in range (len(coef_math)):
        if coef_math[location] not in decimal_table :
            decimal_verification = False
            break
        else :
            decimal_verification = True
    if decimal_verification == False :
        print(error_message)
        coef_math= input("Veuillez saisir votre coefficient de méthématique entre 1 et 10 : ")
    else :
        coef_math = float(coef_math)
        if coef_math == 0 or coef_math > 10 :
            print(error_message)
            coef_math= input("Veuillez saisir votre coefficient de méthématique entre 1 et 10 : ")
            decimal_verification = False

# Géographie
note_geography = input("\nVeuillez saisir votre note de géographie entre 0 et 20 : ")
decimal_verification = False
while decimal_verification == False :
    for location in range (len(note_geography)):
        if note_geography[location] not in decimal_table and note_geography[location] not in separator_table :
            decimal_verification = False
            break
        else :
            decimal_verification = True
    separator_count = 0
    for location in range (len(note_geography)):
        if note_geography[location] in separator_table :
            separator_count += 1
        if separator_count > 1 :
            decimal_verification = False
            break
    if decimal_verification == False :
        print(error_message)
        note_geography= input("Veuillez saisir votre note de géographie entre 0 et 20 : ")
    else :
        note_geography = float(note_geography)
        if note_geography > 20 :
            print(error_message)
            note_geography= input("Veuillez saisir votre note de géographie entre 0 et 20 : ")
            decimal_verification = False
coef_geography = input("Veuillez saisir votre coefficient de géographie entre 1 et 10 : ")
decimal_verification = False
while decimal_verification == False :
    for location in range (len(coef_geography)):
        if coef_geography[location] not in decimal_table :
            decimal_verification = False
            break
        else :
            decimal_verification = True
    if decimal_verification == False :
        print(error_message)
        coef_geography= input("Veuillez saisir votre coefficient de géographie entre 1 et 10 : ")
    else :
        coef_geography = float(coef_geography)
        if coef_geography == 0 or coef_geography > 10 :
            print(error_message)
            coef_geography= input("Veuillez saisir votre coefficient de géographie entre 1 et 10 : ")
            decimal_verification = False

# Informatique
note_computer_science = input("\nVeuillez saisir votre note d'informatique entre 0 et 20 : ")
decimal_verification = False
while decimal_verification == False :
    for location in range (len(note_computer_science)):
        if note_computer_science[location] not in decimal_table and note_computer_science[location] not in separator_table :
            decimal_verification = False
            break
        else :
            decimal_verification = True
    separator_count = 0
    for location in range (len(note_computer_science)):
        if note_computer_science[location] in separator_table :
            separator_count += 1
        if separator_count > 1 :
            decimal_verification = False
            break
    if decimal_verification == False :
        print(error_message)
        note_computer_science= input("Veuillez saisir votre note de d'informatique entre 0 et 20 : ")
    else :
        note_computer_science = float(note_computer_science)
        if note_computer_science > 20 :
            print(error_message)
            note_computer_science= input("Veuillez saisir votre note de d'informatique entre 0 et 20 : ")
            decimal_verification = False
coef_computer_science = input("Veuillez saisir votre coefficient de d'informatique entre 1 et 10 : ")
decimal_verification = False
while decimal_verification == False :
    for location in range (len(coef_computer_science)):
        if coef_computer_science[location] not in decimal_table :
            decimal_verification = False
            break
        else :
            decimal_verification = True
    if decimal_verification == False :
        print(error_message)
        coef_computer_science= input("Veuillez saisir votre coefficient de d'informatique entre 1 et 10 : ")
    else :
        coef_computer_science = float(coef_computer_science)
        if coef_computer_science == 0 or coef_computer_science > 10 :
            print(error_message)
            coef_computer_science= input("Veuillez saisir votre coefficient de d'informatique entre 1 et 10 : ")
            decimal_verification = False

average = round(((note_french*coef_french)+(note_math*coef_math)+(note_geography*coef_geography)+(note_computer_science*coef_computer_science))/(coef_french+coef_math+coef_geography+coef_computer_science),1)

if average >= 16 :
    print(f"\n● Félicitation, avec une moyenne de {average}, vous avez la mention 'Très bien'. ●\n",program_deco)
elif average >= 12 and average < 16 :
    print(f"\n● Bravo, avec une moyenne de {average}, vous avez la mention 'Bien'. ●\n",program_deco)
elif average >= 8 and average < 12 :
    print(f"\n● Super, avec une moyenne de {average}, vous avez la mention 'Assez Bien'. ●\n",program_deco)
elif average >= 4 and average < 8 :
    print(f"\n● Il faut redoubler d'efforts, avec une moyenne de {average}, vous avez la mention 'Insuffisant'. ●\n",program_deco)
else :
    print(f"\n● Vous êtes stupide, avec une moyenne de {average}, vous avez la mention 'Nul'. ●\n",program_deco)