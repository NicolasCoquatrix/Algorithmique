##### VALEUR #####


## IMPORTATIONS ##
import os #os.system("cls")
os.system("cls")
import datetime


## DÉFINITION DES FONCTIONS ##
def input_int_positive(number_print, error_message):
    while True :
        try :
            number = int(input(number_print))
            return number
        except ValueError :
            print("\n╭─" + "─"*len(error_message) + "─╮\n" + f"│ {error_message} │\n" "╰─" + "─"*len(error_message) + "─╯\n")

def input_future_year(year_print, error_message, current_year):
    while True :
        try :
            sale_year = int(input(year_print))
            if sale_year < current_year :
                past_year = "⚠ Erreur ⚠ : L'année saisie en peux pas être dans le passé."
                print("\n╭─" + "─"*len(past_year) + "─╮\n" + f"│ {past_year} │\n" "╰─" + "─"*len(past_year) + "─╯\n")
            else :
                return sale_year
        except ValueError :
            print("\n╭─" + "─"*len(error_message) + "─╮\n" + f"│ {error_message} │\n" "╰─" + "─"*len(error_message) + "─╯\n")


## EN-TÊTE ##
title = "Valeur"
print("╔" + "═" * (len(title) + 2) + "╗" + "\n║ " + title.upper() + " ║\n" + "╚" + "═" * (len(title) + 2) + "╝")
print("💡 Quand une réponse vous est demandée, saissisez-la au clavier et appuyez sur la touche 'Entrée' pour valider.\n\n")


## PROGRAMME ##
# Saisie du prix d'achat de la voiture
purchase_price = input_int_positive("Prix d'achat de votre voiture : ", "⚠ Erreur ⚠ : Valeur non permise. Merci de saisir un nombre entier positif.")
current_year = datetime.date.today().year
sale_year = input_future_year("Année souhaité de vente de votre voiture : ", "⚠ Erreur ⚠ : Valeur non permise. Merci de saisir un nombre entier positif.", current_year)
number_of_years = sale_year - current_year

price = float(purchase_price)
for year in range (number_of_years) :
    price = price - price * 0.07


# Affichage
print(f"\n• En {sale_year} votre voiture vaudra {price}€ •\n\n\n")



# Développé par Nicolas Coquatrix
