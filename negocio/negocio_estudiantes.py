from modelos.estudiante import Estudiante
from datos.obtener_datos import obtener_lista_objetos
from prettytable import PrettyTable
from auxiliares.normalizar_cadena import normalizar_cadena
from datos.insertar_datos import insertar_objeto
from datos.modificar_datos import modificar_objeto
from datos.eliminar_datos import eliminar_objeto
from iu.iu_estudiante import ingresar_nombre_estudiante,ingresar_matricula_estudiante,ingresar_correo_estudiante, ingresar_fecha_nacimiento_estudiante, ingresar_direccion_estudiante, ingresar_nuevo_nombre_estudiante, ingresar_nueva_matricula_estudiante, ingresar_nuevo_correo_estudiante, ingresar_nueva_fecha_nacimiento_estudiante, ingresar_nueva_direccion_estudiante


def listado_estudiantes():
    tabla_estudiante = PrettyTable()
    tabla_estudiante.field_names = ['matricula_estudiante, nombre_estudiante, correo_estudiante, fecha_nacimiento, direccion_estudiante']
    listado_estudiantes = obtener_lista_objetos(Estudiante)
    if listado_estudiantes:
        for estudiante in listado_estudiantes:
            tabla_estudiante.add_row(
                [estudiante.matricula_estudiante, estudiante.nombre_estudiante, estudiante.correo_estudiante, estudiante.fecha_nacimiento, estudiante.direccion_estudiante])
            # print(f'{estudiante.id} {marca.nombre_marca} {marca.pais_origen}')
        print(tabla_estudiante)



def obtener_nombre_estudiante(nombre_estudiante):
    listado_estudiantes = obtener_lista_objetos(Estudiante)
    estudiante_encontrado = None
    if listado_estudiantes:
        for estudiante in listado_estudiantes:
            if normalizar_cadena(estudiante.nombre_estudiante) == normalizar_cadena(nombre_estudiante):
                estudiante_encontrado = estudiante
                break
    return estudiante_encontrado

def obtener_matricula_estudiante(matricula_estudiante):
    listado_estudiantes = obtener_lista_objetos(Estudiante)
    estudiante_encontrado = None
    if listado_estudiantes:
        for estudiante in listado_estudiantes:
            if normalizar_cadena(estudiante.matricula_estudiante) == normalizar_cadena(matricula_estudiante):
                estudiante_encontrado = estudiante
                break
    return estudiante_encontrado

def insertar_estudiante():
    estudiante = ingresar_nombre_estudiante()

    estudiante_encontrado = obtener_nombre_estudiante(estudiante)
    if estudiante_encontrado == None:
        buscar_matricula_estudiante = ingresar_matricula_estudiante()
        matricula_estudiante_encontrado = obtener_matricula_estudiante(buscar_matricula_estudiante)
        if matricula_estudiante_encontrado == None:
            # INSTANCIA DE CLASE
            correo_estudiante = ingresar_correo_estudiante()
            direccion_estudiante = ingresar_direccion_estudiante()
            fecha_nacimieto = ingresar_fecha_nacimiento_estudiante()
            nuevo_estudiante = Estudiante(nombre_estudiante=estudiante,
                                matricula_estudiante=buscar_matricula_estudiante  ,
                                direccion_estudiante = direccion_estudiante,
                                fecha_nacimiento = fecha_nacimieto,
                                correo_estudiante = correo_estudiante,
                                habilitado=True)
            insertar_objeto(nuevo_estudiante)
    else:
        print('Su estudiante YA existe en base de datos.')

def modificar_estudiante():
    estudiante = ingresar_nombre_estudiante()

    estudiante_encontrado = obtener_nombre_estudiante(estudiante)
    if estudiante_encontrado:
        nuevo_nombre_estudiante = ingresar_nuevo_nombre_estudiante()
        nueva_direccion_estudiante = ingresar_nueva_direccion_estudiante()
        nuevo_correo_estudiante = ingresar_nuevo_correo_estudiante()
        nueva_fecha_nacimiento = ingresar_nueva_fecha_nacimiento_estudiante()
        if nuevo_nombre_estudiante != '':
            estudiante_encontrado.nombre_estudiante = nuevo_nombre_estudiante.title()
        if nueva_direccion_estudiante != '':
            estudiante_encontrado.direccion_estudiante = nueva_direccion_estudiante.title()
        if nuevo_correo_estudiante != '':
            estudiante_encontrado.correo_estudiante = nuevo_correo_estudiante.title()
        if nueva_fecha_nacimiento != '':
            estudiante_encontrado.fecha_nacimiento = nueva_fecha_nacimiento.title()
        modificar_objeto()


def eliminado_logico_estudiante():
    estudiante = ingresar_nombre_estudiante()
    estudiante_encontrado = obtener_nombre_estudiante(estudiante)

    if estudiante_encontrado:
        if estudiante_encontrado.habilitado:
            estudiante_encontrado.habilitado = False
            print(f"estudiante '{estudiante_encontrado.nombre_estudiante}' deshabilitado correctamente.")
        else:
            estudiante_encontrado.habilitado = True
            print(f"estudiante '{estudiante_encontrado.nombre_estudiante}' habilitado correctamente.") 
    
        modificar_objeto()
    else:
        print('estudiante NO existe, vuelva a intentarlo.')


def eliminado_fisico_estudiante():
    while True:
        estudiante = ingresar_nombre_estudiante()

        estudiante_encontrado = obtener_nombre_estudiante(estudiante)
        if estudiante_encontrado:
            eliminar_objeto(estudiante_encontrado)
            break
        else:
            print('Estudiante NO existe, vuelva a intentarlo.')