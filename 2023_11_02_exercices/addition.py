##### FONTION POUR ADDITIONNER DEUX NOMBRES #####

import os
os.system("cls")

def addition(number_a,number_b):
    sum = number_a + number_b
    return sum

number_a = int(input("Veuillez saisir le premier nombre : "))
number_b = int(input("Veuillez saisir le deuxième nombre : "))
sum = addition(number_a,number_b)
print(f"La somme de {number_a} + {number_b} est égale à {sum}.")