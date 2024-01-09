##### LES OURS BRUNS #####


## IMPORTATIONS ##
import os #os.system("cls")
os.system("cls")


## DÉFINITION DES FONCTIONS ##
def input_int_positive(number_print, error_message):
    while True :
        try :
            number = int(input(number_print))
            return number
        except ValueError :
            print("\n╭─" + "─"*len(error_message) + "─╮\n" + f"│ {error_message} │\n" "╰─" + "─"*len(error_message) + "─╯\n")

def input_type_forfait(choice_print, error_message):
    while True :
        try :
            choice = int(input(choice_print))
            if choice == 1 or choice == 2 :
                return choice
            else :
                raise Exception
        except Exception :
            print("\n╭─" + "─"*len(error_message) + "─╮\n" + f"│ {error_message} │\n" "╰─" + "─"*len(error_message) + "─╯\n")


## EN-TÊTE ##
title = "Les Ours Brun"
print("╔" + "═" * (len(title) + 2) + "╗" + "\n║ " + title.upper() + " ║\n" + "╚" + "═" * (len(title) + 2) + "╝")
print("💡 Quand une réponse vous est demandée, saissisez-la au clavier et appuyez sur la touche 'Entrée' pour valider.\n\n")


## PROGRAMME ##

# Demande du type de forfait et de l'age
print("Voici les forfaits disonible :\n1 : Forfait à la journée\n2 : Forfait à la saison")
TypeForfait = input_type_forfait("Souhaitez vous acheter le forfait '1' ou le forfait '2' ? : ", "⚠ Erreur ⚠ : Valeur non permise. Merci de saisir '1' ou '2'.")
Age = input_int_positive("\nQuel est votre age ? : ", "⚠ Erreur ⚠ : Valeur non permise. Merci de saisir un nombre entier positif.")
if TypeForfait == 1 :
    Forfait = "forfait jour"
if TypeForfait == 2 :
    Forfait = "forfait saison"

# Calcul du statut
if Age < 12 :
    Statut = "enfant"
elif Age > 60 :
    Statut = "senior"
else :
    Statut = "adulte"

# Calcul du tarif
if Statut == "adulte" :
    if TypeForfait == 1 :
        Tarif = 28.8
    elif TypeForfait == 2 :
        Tarif = 510.0
if Statut == "enfant" :
    if TypeForfait == 1 :
        Tarif = 18.7
    elif TypeForfait == 2 :
        Tarif = 300.0
if Statut == "senior" :
    if TypeForfait == 1 :
        Tarif = 21.4
    elif TypeForfait == 2 :
        Tarif = 340.0

# Affichage
print(f"\n• Ayant un staut {Statut}, votre tarif pour un {Forfait} est de {Tarif}€. •\n\n\n") 



# Développé par Nicolas Coquatrix
