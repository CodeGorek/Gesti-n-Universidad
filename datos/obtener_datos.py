from datos.conexion import Session
from modelos.carrera import Carrera
from sqlalchemy import func

sesion = Session()


def obtener_lista_objetos():
    listado_objetos = sesion.query(Carrera).all()
    if listado_objetos:
        return listado_objetos