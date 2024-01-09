# Déffinir de quelle catégorie est un coureur

print("="*99)
print("-"*20, "Je vais déterminer à quelle catégorie vous êtes rattaché.", "-"*20,"\n")

age = int(input("Veuillez saisir votre age et appuyez sur la touche 'Entrée' pour valider : "))
print()

category = ""

if age < 10 :
    category = "Eveil"
elif age == 10 or age == 11 :
    category = "Poussin"
elif age == 12 or age == 13 :
    category = "Benjamin"
elif age == 14 or age == 15 :
    category = "Minime"
elif age == 16 or age == 17 :
    category = "Cadet"
elif age == 18 or age == 19 :
    category = "Junior"
elif age >= 20 and age <= 22 :
    category = "Espoir"
elif age >= 23 and age <= 39 :
    category = "Senior"
else :
    category = "Vétéran"

print(f"Vous êtes dans la catégorie '{category}'.","\n")
print("="*99,"\n")

