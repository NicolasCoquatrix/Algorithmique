##### EDITEUR DE BULLETIN DE CLASSE #####


## DÉFINITION DES VARIABLES DE BASE ##
title = "Les bulletins de classe"
title_deco = "├"+"─"*int(73-(len(title)/2))+"┤"

if len(title)%2 == 0 :
    program_deco = "\n"+"═"*152+"\n"
else :
    program_deco = "\n"+"═"*151+"\n"


## ENTÊTE ##
print(program_deco+title_deco,title.upper(),title_deco,"\n")
print("ℹ : Quand une réponse vous est demandée, saissisez-la au clavier et appuyez sur la touche 'Entrée' pour valider.")

## DÉFINITION DES VARIABLES DU PROGRAMME ##
decimal_table = ["0","1","2","3","4","5","6","7","8","9"]
separator_table = [",","."]
gender_table = [["masculin","homme","garcon","garçon","m","h","g"],["feminin","féminin","femme","fille","f"]]

error_message_int = "\n⚠ Erreur ⚠ : Valeur non permise. Merci de saisir un nombre entier positif."
error_message_note = "\n⚠ Erreur ⚠ : Valeur non permise. Merci de saisir un nombre positif entre 0 et 20."
error_message_str = "\n⚠ Erreur ⚠ : Merci de saisir une valeure."
error_message_gender = "\n⚠ Erreur ⚠ : Valeur non permise. Merci de saisir 'Masculin', 'Féminin' ou laissez vide pour ne pas répondre."

## PROGRAMME ##
# Définition des matières
number_of_subjects = input("\nVeuillez saisir le nombre de matières : ")
decimal_verification = False
while decimal_verification == False :
    for location in range (len(number_of_subjects)):
        if number_of_subjects[location] not in decimal_table :
            decimal_verification = False
            break
        else :
            decimal_verification = True
    if decimal_verification == False :
        print(error_message_int)
        number_of_subjects= input("Veuillez saisir le nombre de matières : ")
    else :
        number_of_subjects = int(number_of_subjects)
print()
table_subjects = []
table_subjects_whith_pronoun = []
connection = ["a","e","i","o","u","y","h",]
for subjetc_number in range (number_of_subjects) :
    subject_name = input(f"Veuillez saisir le nom de la matière N°{subjetc_number+1} : ")
    str_verification = False
    while str_verification == False :
        if subject_name == "" :
            print(error_message_str)
            subject_name= input(f"Veuillez saisir le nom de la matière N°{subjetc_number+1} : ")
        else :
            str_verification = True
    table_subjects += [subject_name]
    if subject_name[0].lower() in connection :
        table_subjects_whith_pronoun += ["d'" + subject_name]
    else :
        table_subjects_whith_pronoun += ["de " + subject_name]
    table_subjects += [subject_name]

# Définition des élèves
number_of_students = input("\nVeuillez saisir le nombre d'élèves : ")
decimal_verification = False
while decimal_verification == False :
    for location in range (len(number_of_students)):
        if number_of_students[location] not in decimal_table :
            decimal_verification = False
            break
        else :
            decimal_verification = True
    if decimal_verification == False :
        print(error_message_int)
        number_of_students= input("Veuillez saisir le nombre d'élèves : ")
    else :
        number_of_students = int(number_of_students)
table_students_firstname = []
table_students_lastname = []
table_gender = []
for student_number in range (number_of_students) :
    student_firstname = input(f"\nVeuillez saisir le prénom de l'élève N°{student_number+1} : ")
    str_verification = False
    while str_verification == False :
        if student_firstname == "" :
            print(error_message_str)
            student_firstname= input(f"Veuillez saisir le prénom de l'élève N°{student_number+1} : ")
        else :
            str_verification = True
    table_students_firstname += [student_firstname]
    student_lastname = input(f"Veuillez saisir le NOM de {student_firstname} : ").upper()
    str_verification = False
    while str_verification == False :
        if student_lastname == "" :
            print(error_message_str)
            student_lastname= input(f"Veuillez saisir le NOM de {student_firstname} : ").upper()
        else :
            str_verification = True
    table_students_lastname += [student_lastname]
    student_gender = input(f"Veuillez saisir le genre (Masculin / Féminin) de {student_firstname} {student_lastname} (optionnel) : ").lower()
    gender_verification = False
    while gender_verification == False :
        if student_gender in gender_table[0] or student_gender == "" :
            table_gender += ["M"]
            gender_verification = True
        elif student_gender in gender_table[1] :
            table_gender += ["F"]
            gender_verification = True
        else :
            print(error_message_gender)
            student_gender = input(f"Veuillez saisir le genre (Masculin / Féminin) de {student_firstname} {student_lastname} : ").lower()

# Sasie des bulletins
table_note = []
for student in range (number_of_students) :
    table_note += [[]]
print("\n\nℹ : Quand une note vous est demandée, saissisez un nombre entre 0 et 20 et appuyez sur la touche 'Entrée' pour valider.")
for student in range (number_of_students) :
    print(f"\nSaisie du bulletin de {table_students_firstname[student]} {table_students_lastname[student]} : ")
    for subject in range (number_of_subjects) :
        student_note = input(f"Veuillez saisir sa note {table_subjects_whith_pronoun[subject]} : ")
        decimal_verification = False
        while decimal_verification == False :
            for location in range (len(student_note)):
                if student_note[location] not in decimal_table and student_note[location] not in separator_table :
                    decimal_verification = False
                    break
                else :
                    decimal_verification = True
            separator_count = 0
            for location in range (len(student_note)):
                if student_note[location] in separator_table :
                    separator_count += 1
                if separator_count > 1 :
                    decimal_verification = False
                    break
            if decimal_verification == True :
                student_note = float(student_note)
                if student_note < 0 or student_note > 20 :
                    student_note = str(student_note)
                    decimal_verification = False
            if decimal_verification == False :
                print(error_message_note)
                student_note= input(f"Veuillez saisir sa note {table_subjects_whith_pronoun[subject]} : ")
        table_note[student] += [student_note]
print()

# Calcul des moyennes
table_average_student = []
for student in range (number_of_students) :
    average = 0
    for subject in range (number_of_subjects) :
        average += table_note[student][subject]
    table_average_student += [average / number_of_subjects]

# Affichage des buttletins 
for student in range (number_of_students) :
    print(f"\n● Bulletin de {table_students_firstname[student]} {table_students_lastname[student]} ●")
    print(f"Moyenne générale : {round(table_average_student[student],2)}")
    for subject in range (number_of_subjects) :
        print(f"Note {table_subjects_whith_pronoun[subject]} : {round(table_note[student][subject],2)}")
print()

# Calcul de la moyenne de la classe
table_average_class = []
for subject in range (number_of_subjects) :
    subjects_average = 0
    for note in range (number_of_students) :
        subjects_average += table_note[note][subject]
    subjects_average = subjects_average / number_of_students
    table_average_class += [subjects_average]
total_average = 0
for subject in range (number_of_subjects) :
    total_average += table_average_class[subject]
class_average = total_average / number_of_subjects

# Affichage de la moyenne de la classe par matière
print(f"\n● Bulletin de classe ●")
print(f"Moyenne générale : {round(class_average,2)}")
for subject in range (number_of_subjects) :
    print(f"Moyenne {table_subjects_whith_pronoun[subject]} : {round(table_average_class[subject],2)}")

# Affichage du meilleur élève
conjugation = "Homme"
male_conjugation = False
best_average = -1
best_student_table = []
best_student = ""
for student in range (number_of_students) :
    if table_average_student[student] > best_average :
        best_average = table_average_student[student]
        best_student_table = [table_students_firstname[student] + " " + table_students_lastname[student]]
        if table_gender[student] == "M" :
            conjugation = "Homme"
            male_conjugation = True
        elif table_gender[student] == "F" :
            conjugation = "Femme"
            male_conjugation = False
    elif table_average_student[student] == best_average :
        best_student_table += [table_students_firstname[student] + " " + table_students_lastname[student]]
        if table_gender[student] == "M" :
            male_conjugation = True
        if male_conjugation == True :
            conjugation = "Hommes"
        else :
            conjugation = "Femmes"
if conjugation == "Homme" :
    table_conjugation = ["Le","meilleur","lui"]
elif conjugation == "Hommes" :
    table_conjugation = ["Les","meilleurs","eux"]
elif conjugation == "Femme" :
    table_conjugation = ["La","meilleure","elle"]
elif conjugation == "Femmes" :
    table_conjugation = ["Les","meilleures","elles"]
if len(best_student_table) == 1 :
    print(f"\n🏆 {table_conjugation[0]} {table_conjugation[1]} élève est {best_student_table[0]}. Félicitation à {table_conjugation[2]} ! 🏆")
else :
    for student in range (len(best_student_table)) :
        if student == 0 :
            best_student += best_student_table[student]
        elif student == len(best_student_table)-1 :
            best_student += " et " + best_student_table[student]
        else : 
            best_student += ", " + best_student_table[student]
    print(f"\n🏆 {table_conjugation[0]} {table_conjugation[1]} élèves sont {best_student}. Félicitation à {table_conjugation[2]} ! 🏆")


# Affichage du pire élève
conjugation = "Homme"
male_conjugation = False
worse_average = 21
worse_student_table = []
worse_student = ""
for student in range (number_of_students) :
    if table_average_student[student] < worse_average :
        worse_average = table_average_student[student]
        worse_student_table = [table_students_firstname[student] + " " + table_students_lastname[student]]
        if table_gender[student] == "M" :
            conjugation = "Homme"
            male_conjugation = True
        elif table_gender[student] == "F" :
            conjugation = "Femme"
            male_conjugation = False
    elif table_average_student[student] == worse_average :
        worse_student_table += [table_students_firstname[student] + " " + table_students_lastname[student]]
        if table_gender[student] == "M" :
            male_conjugation = True
        if male_conjugation == True :
            conjugation = "Hommes"
        else :
            conjugation = "Femmes"
if conjugation == "Homme" :
    table_conjugation = ["Le","lui"]
elif conjugation == "Hommes" :
    table_conjugation = ["Les","eux"]
elif conjugation == "Femme" :
    table_conjugation = ["La","elle"]
elif conjugation == "Femmes" :
    table_conjugation = ["Les","elles"]
if len(worse_student_table) == 1 :
    print(f"\n💩 {table_conjugation[0]} pire élève est {worse_student_table[0]}. Honte à {table_conjugation[1]} ! 💩")
else :
    for student in range (len(worse_student_table)) :
        if student == 0 :
            worse_student += worse_student_table[student]
        elif student == len(worse_student_table)-1 :
            worse_student += " et " + worse_student_table[student]
        else : 
            worse_student += ", " + worse_student_table[student]
    print(f"\n💩 {table_conjugation[0]} pires élèves sont {worse_student}. Honte à {table_conjugation[1]} ! 💩")

print(program_deco)