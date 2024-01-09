##### EDITEUR DE BULLETIN DE CLASSE #####


## DÉFINITION DES VARIABLES DE BASE ##
title = "Les bulletins de classe"
title_deco = "├"+"─"*int(73-(len(title)/2))+"┤"

if len(title)%2 == 0 :
    program_deco = "\n"+"═"*152+"\n"
else :
    program_deco = "\n"+"═"*151+"\n"


## ENTÊTE ##
print(program_deco+title_deco,title.upper(),title_deco,"\n")
print("ℹ : Quand une réponse vous est demandée, saissisez-la au clavier et appuyez sur la touche 'Entrée' pour valider.")


## PROGRAMME ##
# Définition des matières
number_of_subjects = int(input("\nVeuillez saisir le nombre de matières : "))
print()
table_subjects = []
for subjetc_number in range (number_of_subjects) :
    subject_name = input(f"Veuillez saisir le nom de la matière N°{subjetc_number+1} : ")
    table_subjects += [[subject_name]]

# Définition des élèves
number_of_students = int(input(f"\nVeuillez saisir le nombre d'élèves : "))
table_students_firstname = []
table_students_lastname = []
for student_number in range (number_of_students) :
    student_firstname = input(f"\nVeuillez saisir le prénom de l'élève N°{student_number+1} : ")
    table_students_firstname += [student_firstname]
    student_lastname = input(f"Veuillez saisir le nom de {student_firstname} : ")
    table_students_lastname += [student_lastname]

# Sasie des bulletins
print("\n\nℹ : Quand une note vous est demandée, saissisez un nombre entre 0 et 20 et appuyez sur la touche 'Entrée' pour valider.")
for student in range (number_of_students) :
    print(f"\nSaisie du bulletin de {table_students_firstname[student]} {table_students_lastname[student]} : ")
    for subject in range (number_of_subjects) :
        student_note = float(input(f"Veuillez saisir sa note de {table_subjects[subject][0]} : "))
        table_subjects[subject] += [student_note]
print()

# Calcul des moyennes
table_average_student = []
for student in range (number_of_students) :
    average = 0
    for subject in range (number_of_subjects) :
        average += table_subjects[subject][student+1]
    table_average_student += [average / number_of_subjects]

# Affichage des buttletins 
student_increment = 1
for student in range (number_of_students) :
    print(f"\n● Bulletin de {table_students_firstname[student]} {table_students_lastname[student]} ●")
    print(f"Moyenne générale : {round(table_average_student[student],2)}")
    for subject in range (number_of_subjects) :
        print(f"Note de {table_subjects[subject][0]} : {round(table_subjects[subject][student_increment],2)}")
    student_increment += 1
print()

# Calcul de la moyenne de la classe
table_average_class = []
for subject in range (number_of_subjects) :
    subjects_average = 0
    for note in range (number_of_students) :
        subjects_average += table_subjects[subject][note+1]
    subjects_average = subjects_average / number_of_students
    table_average_class += [subjects_average]
total_average = 0
for subject in range (number_of_subjects) :
    total_average += table_average_class[subject]
class_average = total_average / number_of_subjects

# Affichage de la moyenne de la classe par matière
print(f"\n● Bulletin de classe ●")
print(f"Moyenne générale : {round(class_average,2)}")
for subject in range (number_of_subjects) :
    print(f"Moyenne de {table_subjects[subject][0]} : {round(table_average_class[subject],2)}")

# Affichage du meilleur élève
best_average = 0
best_student = ""
many_best_students = False
for averange in range (len(table_average_student)) :
    if table_average_student[averange] > best_average :
        best_average = table_average_student[averange]
        best_student = table_students_firstname[averange] + " " + table_students_lastname[averange]
        many_best_students = False
    elif table_average_student[averange] == best_average :
        best_student += ", " + table_students_firstname[averange] + " " + table_students_lastname[averange]
        many_best_students = True
if many_best_students == False :
    print(f"\n\n🏆 Le meilleur élève est {best_student}. Félicitation à lui ! 🏆")
else :
    print(f"\n🏆 Les meilleurs élèves sont {best_student}. Félicitation à eux ! 🏆")

# Affichage du pire élève
worse_average = 21
worse_student = ""
many_worse_students = False
for averange in range (len(table_average_student)) :
    if table_average_student[averange] < worse_average :
        worse_average = table_average_student[averange]
        worse_student = table_students_firstname[averange] + " " + table_students_lastname[averange]
        many_worse_students = False
    elif table_average_student[averange] == worse_average :
        worse_student += ", " + table_students_firstname[averange] + " " + table_students_lastname[averange]
        many_worse_students = True
if many_worse_students == False :
    print(f"\n💩 Le pire élève est {worse_student}. Honte à lui ! 💩")
else :
    print(f"\n💩 Les pires élèves sont {worse_student}. Honte à eux ! 💩")

print(program_deco)