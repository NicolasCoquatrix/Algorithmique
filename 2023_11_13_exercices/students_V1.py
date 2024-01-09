##### EDITEUR DE BULLETIN DE CLASSE #####


## IMPORTATIONS ##
import os #os.system("cls")
os.system("cls")


## DÉFINITION DES FONCTIONS ##
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
# Remplissage du tableau
print()
students_list = []
for student in range (2) :
    print()
    student_lastname = input_string_not_empty(f"NOM du stagiaire N°{student+1} : ")
    student_firstname = input_string_not_empty(f"Prénom du stagiaire N°{student+1} : ")
    student_promo = input_string_not_empty(f"Promo de {student_lastname} {student_firstname} : ")
    students_list += [[student_lastname, student_firstname, student_promo]]

# Affichage du tableau
print(f"\n{students_list}\n\n\n")



# Développé par Nicolas Coquatrix