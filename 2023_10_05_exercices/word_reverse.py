# Inversser un mot

print()
print("="*100)
print("-"*36, "Je vais inversser un mot.", "-"*36,"\n")

word = input("Veuillez saisir un mot (Appuyez sur 'Entrée' pour valider) : ")
print()

reverse_word = ""

for loop in range (0,len(word)) :
    reverse_word += word[len(word)-1-loop]

print(reverse_word, "\n")

print("="*100,"\n")