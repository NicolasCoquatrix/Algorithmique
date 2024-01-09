# Définir si un mot est un palindrome

print()
print("="*100)
print("-"*27, "Je vais définir si un mot est un palindrome.", "-"*27,"\n")

word = input("Veuillez saisir un mot (Appuyez sur 'Entrée' pour valider) : ")
print()

for loop in range (0,len(word)) :
    if word[loop] != word[len(word)-1-loop] :
        validation = 0
        break
    else :
        validation = 1

if validation == 1 :
    print("Le mot est un palindrome.","\n")
else : 
    print("Le mot n'est pas un palindrome.","\n")

print("="*100,"\n")