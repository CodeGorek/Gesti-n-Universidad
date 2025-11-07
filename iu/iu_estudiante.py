from auxiliares.fecha_validar import pedir_fecha_valida

def ingresar_nombre_estudiante():
    estudiante = input('Ingrese nombre estuadiante: ')
    return (estudiante)

def ingresar_nuevo_nombre_estudiante():
    estudiante = input('Ingrese NUEVO nombre estudiante: ')
    return (estudiante)

def ingresar_matricula_estudiante():
    matricula_estudiante = int(input('Ingrese matricula estudiante nuevo: '))
    return (matricula_estudiante)

def ingresar_nueva_matricula_estudiante():
    matricula_estudiante = int(input('Ingrese NUEVA matricula estudiante: '))
    return (matricula_estudiante)

def ingresar_correo_estudiante():
    correo = input('Ingrese correo de estudiante: ')
    return (correo)

def ingresar_nuevo_correo_estudiante():
    correo = input('Ingrese NUEVO correo de estudiante: ')
    return (correo)
            
def ingresar_direccion_estudiante():
    direccion = input('Ingrese dirección de estudiante: ')
    return (direccion)

def ingresar_nueva_direccion_estudiante():
    direccion = input('Ingrese NUEVA dirección de estudiante: ')
    return (direccion)

def ingresar_fecha_nacimiento_estudiante():
    fecha_nacimiento = pedir_fecha_valida("Ingrese una fecha (AAAA/MM/DD): ")
    return (fecha_nacimiento)

def ingresar_nueva_fecha_nacimiento_estudiante():
    fecha_nacimiento = pedir_fecha_valida("Ingrese una fecha (AAAA/MM/DD): ")
    return (fecha_nacimiento)