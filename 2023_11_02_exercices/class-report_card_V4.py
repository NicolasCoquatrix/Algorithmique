##### EDITEUR DE BULLETIN DE CLASSE #####


## IMPORTATIONS ##
import os #os.system("cls")
os.system("cls")


## DÉFINITION DES FONCTIONS ##
def input_int_positive(number_print):
    while True :
        try :
            number = int(input(number_print))
            return number
        except ValueError :
            print("\n⚠ Erreur ⚠ : Valeur non permise. Merci de saisir un nombre entier positif.")

def input_float_positive(number_print):
    while True :
        try :
            number = float(input(number_print))
            return number
        except ValueError :
            print("\n⚠ Erreur ⚠ : Valeur non permise. Merci de saisir un nombre positif.")

def input_note_on_20(note_print):
    while True :
        try :
            note = float(input(note_print))
            if not(0 <= note <= 20) :
                raise Exception
            return note
        except ValueError :
            print("\n⚠ Erreur ⚠ : Valeur non permise. Merci de saisir un nombre positif.")
        except Exception :
            print("\n⚠ Erreur ⚠ : Valeur non permise. Merci de saisir un nombre entre 0 et 20.")

def input_string_not_empty(text_print):
    while True :
        try :
            text = input(text_print)
            return text
        except ValueError :
            print("\n⚠ Erreur ⚠ :Valeur non permise. Merci de saisir un texte.")

def input_gender(gender_print):
    while True :
        possible_genders_list = [["masculin","homme","garcon","garçon","m","h","g"],["feminin","féminin","femme","fille","f"]]
        try :
            gender = input(gender_print).lower()
            if gender in possible_genders_list[0] or gender == "" :
                return "M"
            elif gender in possible_genders_list[1] :
                return "F"
        except ValueError :
            print("\n⚠ Erreur ⚠ : Valeur non permise. Merci de saisir 'M' pour un garçon, 'F' pour une fille ou laissez vide pour ne pas répondre.")

def starts_with_a_vowel(letter, word):
    connection = ["a","e","i","o","u","y","h",]
    if letter in connection :
        word_whith_pronoun = "d'" + word
        return word_whith_pronoun
    else :
        word_whith_pronoun = "de " + word
        return word_whith_pronoun

## DÉFINITION DES VARIABLES MODIFIABLES ##
title = "Éditeur de bulletin de classe"


## EN-TÊTE ##
print("╔" + "═" * (len(title) + 2) + "╗" + "\n║ " + title.upper() + " ║\n" + "╚" + "═" * (len(title) + 2) + "╝")
print("💡 Quand une réponse vous est demandée, saissisez-la au clavier et appuyez sur la touche 'Entrée' pour valider.")

## PROGRAMME ##
# Définition des matières
print("\n\n\n📘 DÉFINITION DES MATIÈRES : ")
number_of_subjects = input_int_positive("Nombre de matières : ")
print()
subjects_list = []
subjects_list_whith_pronoun = []
for subjetc in range (number_of_subjects) :
    subject_name = input_string_not_empty(f"Nom de la matière N°{subjetc+1} : ")
    subjects_list += [subject_name]
    first_letter = subject_name[0].lower()
    subjects_list_whith_pronoun += [starts_with_a_vowel(first_letter, subject_name)]

# Définition des élèves
print("\n\n\n👦 DÉFINITION DES ÉLÈVES : ")
number_of_students = input_int_positive("Nombre d'élèves : ")
students_informations_list = [] # Firstname, Lastname, Gender
for student in range (number_of_students) :
    print(f"\n⯈  Élève N°{student+1} : ")
    students_informations_list += [[]]
    students_informations_list[student] += [input_string_not_empty(f"Prénom de l'élève : ")]
    students_informations_list[student] += [input_string_not_empty(f"Nom de l'élève : ").upper()]
    students_informations_list[student] += [input_gender(f"Genre (Masculin / Féminin) de l'élève (optionnel) : ")]

# Sasie des bulletins
print("\n\n\n📋 SAISIE DES BULLETINS (note entre 0 et 20) : ")
notes_list = []
for student in range (number_of_students) :
    print(f"\n⯈  Bulletin de {students_informations_list[student][0]} {students_informations_list[student][1]} :")
    notes_list += [[]]
    for subject in range (number_of_subjects) :
        notes_list[student] += [input_note_on_20(f"Note {subjects_list_whith_pronoun[subject]} : ")]

# Calcul des moyennes des élèves
student_averages_list = []
for student in range (number_of_students) :
    average = 0
    for subject in range (number_of_subjects) :
        average += notes_list[student][subject]
    student_averages_list += [average / number_of_subjects]

# Calcul de la moyenne de la classe
class_averages_list = []
for subject in range (number_of_subjects) :
    subjects_average = 0
    for note in range (number_of_students) :
        subjects_average += notes_list[note][subject]
    subjects_average = subjects_average / number_of_students
    class_averages_list += [subjects_average]
total_average = 0
for subject in range (number_of_subjects) :
    total_average += class_averages_list[subject]
class_average = total_average / number_of_subjects

# Affichage des buttletins 
print("\n\n\n📌 AFFICHAGE DES BULLETINS : ")
for student in range (number_of_students) :
    print(f"\n⯈  Bulletin de {students_informations_list[student][0]} {students_informations_list[student][1]} :")
    print(f"Moyenne générale : {round(student_averages_list[student],2)}")
    for subject in range (number_of_subjects) :
        print(f"Note {subjects_list_whith_pronoun[subject]} : {round(notes_list[student][subject],2)}")

# Affichage de la moyenne de la classe par matière
print("\n⯈  Bulletin de la classe : ")
print(f"Moyenne générale : {round(class_average,2)}")
for subject in range (number_of_subjects) :
    print(f"Moyenne {subjects_list_whith_pronoun[subject]} : {round(class_averages_list[subject],2)}")

# Affichage du meilleur élève
best_average = -1
best_students = ""
best_students_list = [] # Prénom Nom, Genre
for student in range (number_of_students) :
    if student_averages_list[student] > best_average :
        best_average = student_averages_list[student]
        best_student_list = [[students_informations_list[student][0] + " " + students_informations_list[student][1],students_informations_list[student][2]]]
    elif student_averages_list[student] == best_average :
        best_student_list += [[students_informations_list[student][0] + " " + students_informations_list[student][1],students_informations_list[student][2]]]
for student in range (len(best_student_list)) :
    if student == 0 :
        best_students += best_student_list[student][0]
    elif student == len(best_student_list)-1 :
        best_students += " et " + best_student_list[student][0]
    else : 
        best_students += ", " + best_student_list[student][0]
if len(best_student_list) == 1 :
    if best_student_list[0][1] == "M" :
        agreement_list = ["Le","meilleur","élève","est","lui"]
    elif best_student_list[0][1] == "F" :
        agreement_list = ["La","meilleure","élève","est","elle"]
else :
    for student in range (len(best_student_list)) :
        if best_student_list[student][1] == "M" :
            agreement_list = ["Les","meilleurs","élèves","sont","eux"]
            break
        elif best_student_list[0][1] == "F" :
            agreement_list = ["Les","meilleures","élèves","sont","elles"]
print(f"\n\n\n🏆 {agreement_list[0]} {agreement_list[1]} {agreement_list[2]} {agreement_list[3]} {best_students}. Félicitation à {agreement_list[4]} !")

# Affichage du pire élève
worse_average = 21
worse_students = ""
worse_students_list = [] # Prénom Nom, Genre
for student in range (number_of_students) :
    if student_averages_list[student] < worse_average :
        worse_average = student_averages_list[student]
        worse_student_list = [[students_informations_list[student][0] + " " + students_informations_list[student][1],students_informations_list[student][2]]]
    elif student_averages_list[student] == worse_average :
        worse_student_list += [[students_informations_list[student][0] + " " + students_informations_list[student][1],students_informations_list[student][2]]]
for student in range (len(worse_student_list)) :
    if student == 0 :
        worse_students += worse_student_list[student][0]
    elif student == len(worse_student_list)-1 :
        worse_students += " et " + worse_student_list[student][0]
    else : 
        worse_students += ", " + worse_student_list[student][0]
if len(worse_student_list) == 1 :
    if worse_student_list[0][1] == "M" :
        agreement_list = ["Le","pire","élève","est","lui"]
    elif worse_student_list[0][1] == "F" :
        agreement_list = ["La","pire","élève","est","elle"]
else :
    for student in range (len(worse_student_list)) :
        if worse_student_list[student][1] == "M" :
            agreement_list = ["Les","pires","élèves","sont","eux"]
            break
        elif worse_student_list[0][1] == "F" :
            agreement_list = ["Les","pires","élèves","sont","elles"]
print(f"\n💩 {agreement_list[0]} {agreement_list[1]} {agreement_list[2]} {agreement_list[3]} {worse_students}. Honte à {agreement_list[4]} !\n\n\n")



# Développé par Nicolas Coquatrix