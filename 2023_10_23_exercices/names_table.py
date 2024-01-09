##### TABLEAU DE NOMS #####


# Définition des variables de base
title = "Le tableau des noms"
title_deco = "├"+"─"*int(73-(len(title)/2))+"┤"

if len(title)%2 == 0 :
    program_deco = "\n"+"═"*152+"\n"
else :
    program_deco = "\n"+"═"*151+"\n"


# Entête
print(program_deco+title_deco,title.upper(),title_deco,"\n")
print("ℹ : Quand une réponse vous est demandée, saissisez-la au clavier et appuyez sur la touche 'Entrée' pour valider.","\n")


# Définition des variables de base
firstnames_table = []
lastnames_table = []


# Programme
for i in range (10) :
    firstnames = input("\nVeuillez saisir un prénom : ")
    firstnames_table += [firstnames]
    lastnames = input("Veuillez saisir un nom : ")
    lastnames_table += [lastnames]

print("\n")
for i in range (10) :
    print(f"● {lastnames_table[i]} {firstnames_table[i]} ●")
print(program_deco)

