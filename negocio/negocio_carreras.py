from modelos.carrera import Carrera
from datos.obtener_datos import obtener_lista_objetos
from prettytable import PrettyTable
from auxiliares.normalizar_cadena import normalizar_cadena
from iu.iu_carrera import ingresar_nombre_carrera,ingresar_cod_carrera,ingresar_creditos_max_semestre, ingresar_semestre_duracion, ingresar_nuevo_nombre_carrera, ingresar_nuevo_cod_carrera, ingresar_nuevo_creditos_max_semestre, ingresar_nuevo_semestre_duracion
from datos.insertar_datos import insertar_objeto
from datos.modificar_datos import modificar_objeto
from datos.eliminar_datos import eliminar_objeto


def listado_carreras():
    tabla_carreras = PrettyTable()
    tabla_carreras.field_names = ['Cod_carrera', 'Nombre_Carrera', 'Creditos_max','Semestres']
    listado_carreras = obtener_lista_objetos(Carrera)
    if listado_carreras:
        for carrera in listado_carreras:
            tabla_carreras.add_row(
                [carrera.cod_carrera, carrera.nombre_carrera, carrera.creditos_max_semestre, carrera.semestre_duracion])
            # print(f'{carrera.cod_carrera} {carrera.descripcion} {carrera.creditos_max_semestre},{carrera.semestre_duracion}')
        print(tabla_carreras)


def obtener_nombre_carrera(nombre_carrera):
    listado_carreras = obtener_lista_objetos(Carrera)
    carrera_encontrada = None
    if listado_carreras:
        for carrera in listado_carreras:
            if normalizar_cadena(carrera.nombre_carrera) == normalizar_cadena(nombre_carrera):
                carrera_encontrada = carrera
                break
    return carrera_encontrada

def obtener_cod_carrera(cod_carrera):
    listado_carreras = obtener_lista_objetos(Carrera)
    carrera_encontrada = None
    if listado_carreras:
        for carrera in listado_carreras:
            if normalizar_cadena(carrera.cod_carrera) == normalizar_cadena(cod_carrera):
                carrera_encontrada = carrera
                break
    return carrera_encontrada

def insertar_carrera():
    carrera = ingresar_nombre_carrera()

    carrera_encontrada = obtener_nombre_carrera(carrera)
    if carrera_encontrada == None:
        buscar_cod_carrera = ingresar_cod_carrera()
        cod_carrera_encontrado = obtener_cod_carrera(buscar_cod_carrera)
        if cod_carrera_encontrado == None:
            # INSTANCIA DE CLASE
            nuevo_creditos_max_semestre = ingresar_creditos_max_semestre()
            nuevo_semestre_duracion = ingresar_semestre_duracion()
            nueva_carrera = Carrera(nombre_carrera=carrera,
                                cod_carrera=buscar_cod_carrera  ,
                                creditos_max_semestre = nuevo_creditos_max_semestre,
                                semestre_duracion = nuevo_semestre_duracion,
                                habilitado=True)
            insertar_objeto(nueva_carrera)
    else:
        print('Su carrera YA existe en base de datos.')

def modificar_carrera():
    carrera = ingresar_nombre_carrera()

    carrera_encontrada = obtener_nombre_carrera(carrera)
    if carrera_encontrada:
        nuevo_nombre_carrera = ingresar_nuevo_nombre_carrera()
        nuevo_creditos_max = ingresar_nuevo_creditos_max_semestre()
        nuevo_semestre_duracion = ingresar_nuevo_semestre_duracion()
        if nuevo_nombre_carrera != '':
            carrera_encontrada.nombre_carrera = nuevo_nombre_carrera.title()
        if nuevo_creditos_max != '':
            carrera_encontrada.creditos_max_semestre = nuevo_creditos_max
        if nuevo_semestre_duracion != '':
            carrera_encontrada.semestre_duracion = nuevo_semestre_duracion.title()
        modificar_objeto()


def eliminado_logico_carrera():
    carrera = ingresar_nombre_carrera()

    carrera_encontrada = obtener_nombre_carrera(carrera)
    if carrera_encontrada:
        carrera_encontrada.habilitado = False
        modificar_objeto()


def eliminado_fisico_marca():
    while True:
        carrera = ingresar_nombre_carrera()

        carrera_encontrada = obtener_nombre_carrera(carrera)
        if carrera_encontrada:
            eliminar_objeto(carrera_encontrada)
            break
        else:
            print('Carrera NO existe, vuelva a intentarlo.')       