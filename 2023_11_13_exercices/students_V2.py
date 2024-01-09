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
            error_message = "⚠ Erreur ⚠ : Valeur non permise. Merci de saisir un nombre entier positif."
            print("\n╭─" + "─"*len(error_message) + "─╮\n" + f"│ {error_message} │\n" "╰─" + "─"*len(error_message) + "─╯\n")

def input_string_not_empty(text_print):
    while True :
        try :
            text = input(text_print)
            if text == "":
                raise Exception
            return text
        except Exception :
            error_message = "⚠ Erreur ⚠ :Valeur non permise. Merci de saisir la valeur demandée."
            print("\n╭─" + "─"*len(error_message) + "─╮\n" + f"│ {error_message} │\n" "╰─" + "─"*len(error_message) + "─╯\n")

## DÉFINITION DES VARIABLES MODIFIABLES ##
title = "Tableau MNS"


## EN-TÊTE ##
print("╔" + "═" * (len(title) + 2) + "╗" + "\n║ " + title.upper() + " ║\n" + "╚" + "═" * (len(title) + 2) + "╝")
print("💡 Quand une réponse vous est demandée, saissisez-la au clavier et appuyez sur la touche 'Entrée' pour valider.")

## PROGRAMME ##
# Définition de la taille du tableau
column_head = ["NOM","PRÉNOM","PROMO"]
column_1_size = len(column_head[0])
column_2_size = len(column_head[1])
column_3_size = len(column_head[2])

# Remplissage du tableau
print()
number_of_students = input_int_positive("Nombre de stagiaires : ")
students_list = []
for student in range (number_of_students) :
    print()
    student_lastname = input_string_not_empty(f"NOM du stagiaire N°{student+1} : ")
    if len(student_lastname) > column_1_size :
        column_1_size = len(student_lastname)
    student_firstname = input_string_not_empty(f"Prénom du stagiaire N°{student+1} : ")
    if len(student_firstname) > column_2_size :
        column_2_size = len(student_firstname)
    student_promo = input_string_not_empty(f"Promo de {student_lastname} {student_firstname} : ")
    if len(student_promo) > column_3_size :
        column_3_size = len(student_promo)
    students_list += [[student_lastname, student_firstname, student_promo]]

# Affichage du tableau
print("\n╔" + "═"*(column_1_size+2) + "╦" + "═"*(column_2_size+2) + "╦" + "═"*(column_3_size+2) + "╗\n║ " + column_head[0] + " "*(column_1_size-len(column_head[0])) + " ║ " + column_head[1] + " "*(column_2_size-len(column_head[1])) + " ║ " + column_head[2] + " "*(column_3_size-len(column_head[2])) + " ║\n╠" + "═"*(column_1_size+2) + "╬" + "═"*(column_2_size+2) + "╬" + "═"*(column_3_size+2) + "╣")
for line in range (number_of_students):
    if line != number_of_students-1 :
        print("║ " + students_list[line][0] + " "*(column_1_size-len(students_list[line][0])) + " ║ " + students_list[line][1] + " "*(column_2_size-len(students_list[line][1])) + " ║ " + students_list[line][2] + " "*(column_3_size-len(students_list[line][2])) + " ║\n╠" + "═"*(column_1_size+2) + "╬" + "═"*(column_2_size+2) + "╬" + "═"*(column_3_size+2) + "╣")
    else :
        print("║ " + students_list[line][0] + " "*(column_1_size-len(students_list[line][0])) + " ║ " + students_list[line][1] + " "*(column_2_size-len(students_list[line][1])) + " ║ " + students_list[line][2] + " "*(column_3_size-len(students_list[line][2])) + " ║\n╚" + "═"*(column_1_size+2) + "╩" + "═"*(column_2_size+2) + "╩" + "═"*(column_3_size+2) + "╝\n\n\n")



# Développé par Nicolas Coquatrix
