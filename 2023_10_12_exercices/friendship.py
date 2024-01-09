##### L'ALGORITHME DE L'AMITIÉ  #####


# Définition des variables de base
title = "L'algorithme de l'amitié, par le Docteur Sheldon Cooper"
title_deco = "├"+"─"*int(73-(len(title)/2))+"┤"

if len(title)%2 == 0 :
    program_deco = "\n"+"═"*152+"\n"
else :
    program_deco = "\n"+"═"*151+"\n"

final_message = "║ Félicitations, vous êtes maintenant ami avec cette personne. ║"
final_print = "╔"+"═"*(len(final_message)-2)+f"╗\n{final_message.upper()}\n╚"+"═"*(len(final_message)-2)+f"╝\n{program_deco}"

error_message = "⚠ Erreur ⚠ : Votre choix est invalide. Merci de saisir 'Oui' ou 'Non'."


# Entête
print(program_deco+title_deco,title.upper(),title_deco,"\n")
print("ℹ : Quand une réponse vous est demandée, saisissez 'Oui' ou 'Non' et appuyez sur la touche 'Entrée' pour valider.","\n","\n")


# Définition des variables du programme
home = ""
meal = ""
beverage = ""
interest = ""
interest_retry = ""


# Définition des tableaux de réponses
table_yes = ["Oui","oui","OUI","O","o","Yes","yes","YES","Y","y","1"]
table_no = ["Non","non","NON","N","n","No","no","NO","0"]


# Programme
print("Pour vous faire un ami, commencez par passer un appel à une personne (vivante).")
while home not in table_yes and home not in table_no :
    home = input("La personne à répondu à l'appel ? : ")
    print()
    if home in table_yes :
        print("Super, demandez lui si elle voudrait partager un repas avec vous.")
    elif home in table_no :
        print("Ce n'est pas grave, laissez un message sur son répondeur en lui demandant de vous rappeler.")
        print("Quand elle vous rappellera, demandez-lui si elle voudrait partager un repas avec vous.")
    else :
        print(error_message)

while meal not in table_yes and meal not in table_no :
    meal = input("Accepte-t-elle ? : ")
    print()
    if meal in table_yes :
        print("Génial, allez dîner avec elle.")
        print(final_print)
        exit()
    elif meal in table_no :
        print("Ne paniquez pas, demandez lui si elle veux boire une boisson chaude avec vous.")
        while beverage not in table_yes and beverage not in table_no :
            beverage = input("Accepte-t-elle ? : ")
            print()
            if beverage in table_yes :
                print("Pafait, proposez lui un thé, un café ou un chocolat chaud.")
                print(final_print)
                exit()
            elif beverage in table_no :
                print("Pas de soucis, demandez lui un de ses centres d'intérêt.")
                while interest not in table_yes and interest not in table_no :
                    interest = input("Partagez-vous ce centre d'intérêt ? : ")
                    print()
                    if interest in table_yes :
                        print("Magnifique, invitez-la à faire cette activité avec vous.")
                        print(final_print)
                    elif interest in table_no :
                        counter = 0
                        print("Rien est encore perdu, demandez lui un autre de ses centres d'intérêt.")
                        while interest_retry not in table_yes and interest_retry not in table_no:
                            interest_retry = input("Partagez-vous ce centre d'intérêt ? : ")
                            print()
                            if interest_retry in table_yes :
                                print("Magnifique, invitez-la à faire cette activité avec vous.")
                                print(final_print)
                                exit()
                            elif interest_retry in table_no :
                                if counter < 4 :
                                    print("Ne perdez pas espoir, demandez lui un autre de ses centres d'intérêt.")
                                    interest_retry = ""
                                counter += 1
                            else :
                                print(error_message)
                        print("Faite un petit effort... Invitez-la à faire la moins pénible de ces activités.")
                        print(final_print) 
                    else :
                        print(error_message) 
            else :
                print(error_message) 
    else :
        print(error_message)

# Fin du programme