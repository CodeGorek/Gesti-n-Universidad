from datos.conexion import sesion
from sqlalchemy import func
from prettytable import PrettyTable
from modelos.carrera import Carrera
from modelos.estudiante import Estudiante



def obtener_lista_objetos(objeto):
    listado_objetos = sesion.query(objeto).all()
    if listado_objetos:
        return listado_objetos
    
def obtener_nombre_carrera(nombre_carrera):
    listado_marcas = obtener_datos_objetos(nombre_carrera)
    marca_encontrada = None
    if listado_marcas:
        for marca in listado_marcas:
            if normalizar_cadena(marca.nombre_marca) == normalizar_cadena(nombre_marca):
                marca_encontrada = marca
                break
    return marca_encontrada




