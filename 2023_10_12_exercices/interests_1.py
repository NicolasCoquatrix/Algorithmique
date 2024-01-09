# Calcul des intérêts de Jean dans 10 ans

print()
print("="*100)
print("-"*27, "Bonjour Jean, je vais calculer vos intérêts.", "-"*27,"\n")

money = 2000

for years in range (0,9) :
    money += money*0.02

print(f"Dans 10 ans, vous aurez {round(money,2)}€ sur votre livret A.","\n")

print("="*100,"\n")