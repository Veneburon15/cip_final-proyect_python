"""
This is an app for help techers to get the averages of their students. 
The idea is that the teacher inputs the name of the students and the notes of three exams, and then the app will calculate the average of the students notes
"""

# MAIN DICTIONARY
students = []

# CONSTANTS
OPCION_ALUMNOS = 1
OPCION_ALUMNOS_PROMEDIOS = 2
OPCION_ALUMNOS_INGRESADOS = 3
OPCION_SALIR = 4

### MAIN FUNCTION
def main():
    permiso = input("If you want to enter a student's grades, write 'Yes'. Otherwise, write any letter to exit.")
    while permiso.lower() == "yes":
        student_prom()
        permiso = input("If you want to continue averaging, write 'Yes'. Otherwise, write any letter.")
    show_menu()
    print("Thank you for using our averaging platform.")


####### FUNCTIONS
##### CORE FUNCTION
def student_prom():
    print("Thank you for using our averaging platform.")
    data_solicitation()

#### DATA SOLICITATION
##In this function the user will provide the info that the app will use
def data_solicitation():
    name_alumno = name_input()
    nota_1 = pedir_nota(1)
    nota_2 = pedir_nota(2)
    nota_3 = pedir_nota(3)
    average = calcular_average(nota_1, nota_2, nota_3)
    student_add(name_alumno, nota_1, nota_2, nota_3, average)
    print(f"The {name_alumno}'s average is: {average}")

# NAME INPUT
##This function ask the user to input the name of the student
def name_input():
    alumno = ""
    regex = r'^[a-zA-Z\s]+$'
    while not alumno:
        alumno = input("Please enter the name of the student:")
    return alumno

# GRADE SOLICITATION AND VALIDATION
##This function will ask the user to provide the grade of three exams, and afterwards will verify if the grades are in a range of 1 to 20 (grade range for Venezuela -the country where I'm from-)
def pedir_nota(nota_num):
    nota = None
    while True:
        try:
            nota = float(input(f"Please enter the grade for the {nota_num}º exam:"))
            if nota < 0 or nota > 20:
                raise ValueError
            break
        except ValueError:
            print("Error: The grade must be between 0 and 20.")
    return nota

# AVERAGE CALCULATION
##This function does the calculation of the student's average
def calcular_average(nota_1, nota_2, nota_3):
    average = (nota_1 + nota_2 + nota_3) / 3
    return "{:.2f}".format(average)

# DATA ADDITTION
##This function sends the recopiled information to the mayn dictionary
def student_add(name, nota_1, nota_2, nota_3, average):
    student = {"name": name, "nota1": nota_1, "nota2": nota_2, "nota3": nota_3, "average": average}
    students.append(student)


#### DATA DEVOLUTION
##This function deploys a "switch" for the user to select a way to show the dictionary's information
def show_menu():
    opcion = 0
    while opcion < OPCION_ALUMNOS or opcion > OPCION_SALIR:
        try:
            opcion = int(input(f"Please enter an option:\n{OPCION_ALUMNOS}. Show the names of the entered students\n{OPCION_ALUMNOS_PROMEDIOS}. Show the names of the entered students and their averages\n{OPCION_ALUMNOS_INGRESADOS}. Show data of all the entered students\n{OPCION_SALIR}. Exit\n"))
        except ValueError:
            opcion = 0
    
    if opcion == OPCION_ALUMNOS:
        names_dev()
    elif opcion == OPCION_ALUMNOS_PROMEDIOS:
        names_prom()
    elif opcion == OPCION_ALUMNOS_INGRESADOS:
        show_data()
    elif opcion == OPCION_SALIR:
        print("Exiting the program.")
    else:
        print("Invalid option.")


##### DATA DEVOLUTION FUNCTIONS
# NAME DEVOLUTION
##This function shows every student's name
def names_dev():
    message = "\n".join([student["name"] for student in students])
    print(message)

# NAMES AND AVERAGES DEVOLUTION
##This function shows every student's name and averages
def names_prom():
    message = "\n".join([f"{student['name']} ---- {student['average']}" for student in students])
    print(message)

# STUDENT LIST DEVOLUTION
##This function shows every student's lists that be inside the Main Dictionary
def show_data():
    message = ""
    for i, student in enumerate(students):
        message += f"student #{i + 1}:\n" \
                   f"name: {student['name']}\n" \
                   f"Grade 1: {student['nota1']}\n" \
                   f"Grade 2: {student['nota2']}\n" \
                   f"Grade 3: {student['nota3']}\n" \
                   f"average: {student['average']}\n\n"
    print(message)
    
if __name__ == "__main__":
    main()

"""
Final code, code in place 
"""