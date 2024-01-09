# Définir si un mot est un palindrome

print()
print("="*100)
print("-"*27, "Je vais définir si un mot est un palindrome.", "-"*27,"\n")

word = input("Veuillez saisir un mot (Appuyez sur 'Entrée' pour valider) : ")
print()

first_letter = 0
last_letter = len(word) - 1

validation = 0

while first_letter <= len(word) - 1 and word[first_letter] == word[last_letter] :
    first_letter += 1
    last_letter -= 1
    if first_letter > last_letter :
        validation = 1

if validation == 1 :
    print("Le mot est un palindrome.","\n")
else : 
    print("Le mot n'est pas un palindrome.","\n")

print("="*100,"\n")