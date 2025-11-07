def ingresar_nombre_carrera():
    carrera = input('Ingrese nombre carrera: ')
    return (carrera)

def ingresar_nuevo_nombre_carrera():
    carrera = input('Ingrese NUEVO nombre carrera: ')
    return (carrera)

def ingresar_cod_carrera():
    cod_carrera = input('Ingrese codigo carrera: ')
    return (cod_carrera)

def ingresar_nuevo_cod_carrera():
    cod_carrera = input('Ingrese NUEVO código carrera: ')
    return (cod_carrera)

def ingresar_creditos_max_semestre():
    entero = False
    while entero == False: 
        creditos_max_semestres = int(input('Ingrese creditos max por semestre: '))
        if isinstance(creditos_max_semestres,int):
            entero = True
            return creditos_max_semestres
        else: 
            print("Por favor ingrese números!.")

def ingresar_nuevo_creditos_max_semestre():
    entero = False
    while entero == False: 
        creditos_max_semestres = int(input('Ingrese nuevos creditos max por semestre: '))
        if isinstance(creditos_max_semestres,int):
            entero = True
            return creditos_max_semestres
        else: 
            print("Por favor ingrese números!.")

def ingresar_semestre_duracion():
    entero = False
    while entero == False: 
        semestre_duracion = int(input('Ingrese semestre de duración: '))
        if isinstance(semestre_duracion,int):
            entero = True
            return semestre_duracion
        else: 
            print("Por favor ingrese números.")

def ingresar_nuevo_semestre_duracion():
    entero = False
    while entero == False: 
        semestre_duracion = int(input('Ingrese nuevo semestre de duración: '))
        if isinstance(semestre_duracion,int):
            entero = True
            return semestre_duracion
        else: 
            print("Por favor ingrese números.")
