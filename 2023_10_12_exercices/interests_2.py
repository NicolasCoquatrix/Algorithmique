# Calcul des intérêts de Jean

print()
print("="*200)
print("-"*77, "Bonjour Jean, je vais calculer vos intérêts.", "-"*77,"\n")

money = 2000
duration = int(input("Veuillez saisir le nombre d'années : "))
print()
interests = float(input("Veuillez saisir le taux d'intérêts en pourcentage : "))
print()

for years in range (duration) :
    money += money*interests/100

final_print = f"║ Dans 10 ans, vous aurez {round(money,2)}€ sur votre livret A. ║"

print("╔"+"═"*(len(final_print)-2)+"╗")
print(final_print)
print("╚"+"═"*(len(final_print)-2)+"╝")

print("═"*200,"\n")