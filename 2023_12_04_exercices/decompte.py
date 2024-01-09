##### DÉCOMPTE #####


## IMPORTATIONS ##
import os #os.system("cls")
os.system("cls")


## DÉFINITION DES FONCTIONS ##
def input_string_not_empty(text_print, error_message):
    while True :
        try :
            text = input(text_print).lower()
            if text == "":
                raise Exception
            return text
        except Exception :
            print("\n╭─" + "─"*len(error_message) + "─╮\n" + f"│ {error_message} │\n" "╰─" + "─"*len(error_message) + "─╯\n")


## EN-TÊTE ##
title = "Décompte"
print("╔" + "═" * (len(title) + 2) + "╗" + "\n║ " + title.upper() + " ║\n" + "╚" + "═" * (len(title) + 2) + "╝")
print("💡 Quand une réponse vous est demandée, saissisez-la au clavier et appuyez sur la touche 'Entrée' pour valider.\n\n")


## PROGRAMME ##
# Saisie des noms
Nom = ""
NbNom = 0
while Nom != "fin" :
    Nom = input_string_not_empty(f"Nom n°{NbNom+1} : ", "⚠ Erreur ⚠ : Merci de saisir un nom.")
    if Nom != "fin" :
        NbNom += 1

#Affichage
print(f"\n• Vous avez saisi {NbNom} noms. •\n\n\n")



# Développé par Nicolas Coquatrix
