from datos.conexion import sesion
from sqlalchemy import func
from prettytable import PrettyTable
from modelos.carrera import Carrera
from modelos.estudiante import Estudiante
from auxiliares.normalizar_cadena import normalizar_cadena


def obtener_lista_objetos(objeto):
    listado_objetos = sesion.query(objeto).all()
    if listado_objetos:
        return listado_objetos
    
def obtener_nombre_carrera(nombre_carrera):
    listado_marcas = obtener_lista_objetos(Carrera)
    carrera_encontrada = None
    if listado_marcas:
        for carrera in listado_marcas:
            if normalizar_cadena(carrera.nombre_carrera) == normalizar_cadena(nombre_carrera):
                carrera_encontrada = carrera
                break
    return carrera_encontrada




