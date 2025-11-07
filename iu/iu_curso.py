def ingresar_nombre_curso():
    curso = input('Ingrese nombre curso: ')
    return (curso)

def ingresar_nuevo_nombre_curso():
    curso = input('Ingrese NUEVO nombre curso: ')
    return (curso)

def ingresar_cod_curso():
    cod_curso = input('Ingrese cod carrera : ')
    return (cod_curso)

def ingresar_nuevo_cod_curso():
    cod_curso = input('Ingrese NUEVO código curso: ')
    return (cod_curso)

def ingresar_creditos():
    entero = False
    while entero == False: 
        creditos = int(input('Ingrese creditos: '))
        if isinstance(creditos,int):
            entero = True
            return creditos
        else: 
            print("Por favor ingrese números.")

def ingresar_nuevos_creditos():
    entero = False
    while entero == False: 
        creditos = int(input('Ingrese nuevos creditos: '))
        if isinstance(creditos,int):
            entero = True
            return creditos
        else: 
            print("Por favor ingrese números.")

def ingresar_pre_requisitos():
    pre_requisitos = input('Ingrese pre-requisitos: ')
    return (pre_requisitos)

def ingresar_nuevos_pre_requisitos():
    pre_requisitos = input('Ingrese nuevos pre-requisitos: ')
    return (pre_requisitos)