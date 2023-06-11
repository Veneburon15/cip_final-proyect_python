"""
This is an app for help techers to get the averages of their students. 
The idea is that the teacher inputs the name of the students and the notes of three exams, and then the app will calculate the average of the students notes
"""

# MAIN DICTIONARY
estudiantes = []

# CONSTANTS
OPCION_ALUMNOS = 1
OPCION_ALUMNOS_PROMEDIOS = 2
OPCION_ALUMNOS_INGRESADOS = 3
OPCION_SALIR = 4

### MAIN FUNCTION
def main():
    permiso = input("Si desea ingresar las notas de un alumno, escriba 'Si'. De lo contrario, escriba cualquier letra para salir: ")
    while permiso.lower() == "si":
        student_prom()
        permiso = input("Si desea continuar promediando escriba 'Si', de lo contrario, escriba cualquier letra: ")
    mostrar_menu()
    print("Muchas gracias por usar nuestra plataforma")


####### FUNCTIONS
##### CORE FUNCTION
def student_prom():
    print("Gracias por usar nuestra plataforma de promediación")
    data_solicitation()

#### DATA SOLICITATION
##In this function the user will provide the info that the app will use
def data_solicitation():
    nombre_alumno = name_input()
    nota_1 = pedir_nota(1)
    nota_2 = pedir_nota(2)
    nota_3 = pedir_nota(3)
    promedio = calcular_promedio(nota_1, nota_2, nota_3)
    student_add(nombre_alumno, nota_1, nota_2, nota_3, promedio)
    print(f"El promedio del alumno {nombre_alumno} es: {promedio}")

# NAME INPUT
##This function ask the user to input the name of the student
def name_input():
    alumno = ""
    regex = r'^[a-zA-Z\s]+$'
    while not alumno:
        alumno = input("Ingrese el nombre del alumno: ")
    return alumno

# GRADE SOLICITATION AND VALIDATION
##This function will ask the user to provide the grade of three exams, and afterwards will verify if the grades are in a range of 1 to 20 (grade range for Venezuela -the country where I'm from-)
def pedir_nota(nota_num):
    nota = None
    while True:
        try:
            nota = float(input(f"Ingrese la nota del {nota_num}º examen: "))
            if nota < 0 or nota > 20:
                raise ValueError
            break
        except ValueError:
            print("Error: La nota debe estar entre 0 y 20")
    return nota

# AVERAGE CALCULATION
##This function does the calculation of the student's average
def calcular_promedio(nota_1, nota_2, nota_3):
    promedio = (nota_1 + nota_2 + nota_3) / 3
    return "{:.2f}".format(promedio)

# DATA ADDITTION
##This function sends the recopiled information to the mayn dictionary
def student_add(nombre, nota_1, nota_2, nota_3, promedio):
    estudiante = {"nombre": nombre, "nota1": nota_1, "nota2": nota_2, "nota3": nota_3, "promedio": promedio}
    estudiantes.append(estudiante)


#### DATA DEVOLUTION
##This function deploys a "switch" for the user to select a way to show the dictionary's information
def mostrar_menu():
    opcion = 0
    while opcion < OPCION_ALUMNOS or opcion > OPCION_SALIR:
        try:
            opcion = int(input(f"Ingrese una opción:\n{OPCION_ALUMNOS}. Mostrar nombres de los alumnos ingresados\n{OPCION_ALUMNOS_PROMEDIOS}. Mostrar nombres de los alumnos y sus promedios\n{OPCION_ALUMNOS_INGRESADOS}. Datos de todos los alumnos ingresados\n{OPCION_SALIR}. Salir\n"))
        except ValueError:
            opcion = 0
    
    if opcion == OPCION_ALUMNOS:
        names_dev()
    elif opcion == OPCION_ALUMNOS_PROMEDIOS:
        names_prom()
    elif opcion == OPCION_ALUMNOS_INGRESADOS:
        show_data()
    elif opcion == OPCION_SALIR:
        print("Saliendo del programa")
    else:
        print("Opción inválida")


##### DATA DEVOLUTION FUNCTIONS
# NAME DEVOLUTION
##This function shows every student's name
def names_dev():
    mensaje = "\n".join([estudiante["nombre"] for estudiante in estudiantes])
    print(mensaje)

# NAMES AND AVERAGES DEVOLUTION
##This function shows every student's name and averages
def names_prom():
    mensaje = "\n".join([f"{estudiante['nombre']} ---- {estudiante['promedio']}" for estudiante in estudiantes])
    print(mensaje)

# STUDENT LIST DEVOLUTION
##This function shows every student's lists that be inside the Main Dictionary
def show_data():
    mensaje = ""
    for i, estudiante in enumerate(estudiantes):
        mensaje += f"Estudiante #{i + 1}:\n" \
                   f"Nombre: {estudiante['nombre']}\n" \
                   f"Nota 1: {estudiante['nota1']}\n" \
                   f"Nota 2: {estudiante['nota2']}\n" \
                   f"Nota 3: {estudiante['nota3']}\n" \
                   f"Promedio: {estudiante['promedio']}\n\n"
    print(mensaje)
    
if __name__ == "__main__":
    main()

"""
Final code, code in place 
"""