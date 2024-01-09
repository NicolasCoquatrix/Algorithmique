##### VÉRIFICATION #####


## IMPORTATIONS ##
import os #os.system("cls")
os.system("cls")


## DÉFINITION DES FONCTIONS ##
def input_int_positive(number_print, error_message):
    while True :
        try :
            number = int(input(number_print))
            if number < 10 :
                bigger = "Plus grand !"
                print("\n╭─" + "─"*len(bigger) + "─╮\n" + f"│ {bigger} │\n" "╰─" + "─"*len(bigger) + "─╯\n")
            elif number > 20 :
                smaller = "Plus petit !"
                print("\n╭─" + "─"*len(smaller) + "─╮\n" + f"│ {smaller} │\n" "╰─" + "─"*len(smaller) + "─╯\n")
            else :
                return number
        except ValueError :
            print("\n╭─" + "─"*len(error_message) + "─╮\n" + f"│ {error_message} │\n" "╰─" + "─"*len(error_message) + "─╯\n")


## EN-TÊTE ##
title = "Vérification"
print("╔" + "═" * (len(title) + 2) + "╗" + "\n║ " + title.upper() + " ║\n" + "╚" + "═" * (len(title) + 2) + "╝")
print("💡 Quand une réponse vous est demandée, saissisez-la au clavier et appuyez sur la touche 'Entrée' pour valider.\n\n")


## PROGRAMME ##
# Saisie du nombre
number = input_int_positive("Veuillez saisir un nombre compris entre 10 et 20 : ", "⚠ Erreur ⚠ : Valeur non permise. Merci de saisir un nombre entier positif.")


# Affichage 
print("\n• Bravo •\n\n\n")



# Développé par Nicolas Coquatrix
