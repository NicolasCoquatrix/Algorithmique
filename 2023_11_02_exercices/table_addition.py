##### FONTION POUR ADDITIONNER DEUX NOMBRES #####

import os
os.system("cls")

def addition(numbers):
    sum = 0
    for i in range (len(numbers)) :
        sum += numbers[i]
    return sum

number_of_number = int(input("Veuillez saisir le nombre de nombre à additionner : "))
numbers = []
for i in range (number_of_number) :
    numbers += [int(input("Veuillez saisir un nombre : "))]
sum = addition(numbers)
print(f"La somme est de {sum}.")