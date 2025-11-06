from datos.conexion import sesion
<<<<<<< HEAD
from sqlalchemy import func
from prettytable import PrettyTable
from modelos.carrera import Carrera
from modelos.estudiante import Estudiante
from auxiliares.normalizar_cadena import normalizar_cadena

=======
>>>>>>> f48ecc4ae1222754bec3ef15dda8244016d1ba74

def obtener_lista_objetos(objeto):
    listado_objetos = sesion.query(objeto).all()
    if listado_objetos:
        return listado_objetos
    
<<<<<<< HEAD
def obtener_nombre_carrera(nombre_carrera):
    listado_marcas = obtener_lista_objetos(Carrera)
    carrera_encontrada = None
    if listado_marcas:
        for carrera in listado_marcas:
            if normalizar_cadena(carrera.nombre_carrera) == normalizar_cadena(nombre_carrera):
                carrera_encontrada = carrera
                break
    return carrera_encontrada
=======

>>>>>>> f48ecc4ae1222754bec3ef15dda8244016d1ba74




