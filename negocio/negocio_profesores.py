from modelos.profesor import Profesor
from datos.obtener_datos import obtener_lista_objetos
from prettytable import PrettyTable
from auxiliares.normalizar_cadena import normalizar_cadena
from iu.iu_profesor import ingresar_nombre_profesor,ingresar_cod_profesor,ingresar_correo_profesor, ingresar_especialidad, ingresar_nuevo_nombre_profesor, ingresar_nuevo_cod_profesor, ingresar_nuevo_correo_profesor, ingresar_nueva_especialidad
from datos.insertar_datos import insertar_objeto
from datos.modificar_datos import modificar_objeto
from datos.eliminar_datos import eliminar_objeto

def listado_profesores():
    tabla_profesor = PrettyTable()
    tabla_profesor.field_names = ['cod_profesor, nombre_profesor, correo_profesor, especialidad']
    listado_profesores = obtener_lista_objetos(Profesor)
    if listado_profesores:
        for profesor in listado_profesores:
            tabla_profesor.add_row(
                [profesor.cod_profesor, profesor.nombre_profesor, profesor.correo_profesor, profesor.especialidad])
            # print(f'{profesor.id} {marca.nombre_marca} {marca.pais_origen}')
        print(tabla_profesor)

def obtener_nombre_profesor(nombre_profesor):
    listado_profesores = obtener_lista_objetos(Profesor)
    profesor_encontrado = None
    if listado_profesores:
        for profesor in listado_profesores:
            if normalizar_cadena(profesor.nombre_profesor) == normalizar_cadena(nombre_profesor):
                profesor_encontrado = profesor
                break
    return profesor_encontrado

def obtener_cod_profesor(cod_profesor):
    listado_profesores = obtener_lista_objetos(Profesor)
    profesor_encontrado = None
    if listado_profesores:
        for profesor in listado_profesores:
            if normalizar_cadena(profesor.cod_profesor) == normalizar_cadena(cod_profesor):
                profesor_encontrado = profesor
                break
    return profesor_encontrado

def insertar_profesor():
    profesor = ingresar_nombre_profesor()

    profesor_encontrado = obtener_nombre_profesor(profesor)
    if profesor_encontrado == None:
        buscar_cod_profesor = ingresar_cod_profesor()
        cod_profesor_encontrado = obtener_cod_profesor(buscar_cod_profesor)
        if cod_profesor_encontrado == None:
            # INSTANCIA DE CLASE
            correo_profesor = ingresar_correo_profesor()
            especialidad = ingresar_especialidad()
            nuevo_profesor = profesor(nombre_profesor=profesor,
                                cod_profesor=buscar_cod_profesor  ,
                                especialidad = especialidad,
                                correo_profesor = correo_profesor,
                                habilitado=True)
            insertar_objeto(nuevo_profesor)
    else:
        print('El profesor YA existe en base de datos.')

def modificar_profesor():
    profesor = ingresar_nombre_profesor()

    profesor_encontrado = obtener_nombre_profesor(profesor)
    if profesor_encontrado:
        nuevo_nombre_profesor = ingresar_nuevo_nombre_profesor()
        nueva_especialidad = ingresar_nueva_especialidad()
        nuevo_correo_profesor = ingresar_nuevo_correo_profesor()
        if nuevo_nombre_profesor != '':
            profesor_encontrado.nombre_profesor = nuevo_nombre_profesor.title()
        if nueva_especialidad != '':
            profesor_encontrado.especialidad = nueva_especialidad.title()
        if nuevo_correo_profesor != '':
            profesor_encontrado.correo_profesor = nuevo_correo_profesor.title()
        modificar_objeto()


def eliminado_logico_profesor():
    profesor = ingresar_nombre_profesor()

    profesor_encontrado = obtener_nombre_profesor(profesor)
    if profesor_encontrado:
        profesor_encontrado.habilitado = False
        modificar_objeto()


def eliminado_fisico_profesor():
    while True:
        profesor = ingresar_nombre_profesor()

        profesor_encontrado = obtener_nombre_profesor(profesor)
        if profesor_encontrado:
            eliminar_objeto(profesor_encontrado)
            break
        else:
            print('Profesor NO existe, vuelva a intentarlo.')